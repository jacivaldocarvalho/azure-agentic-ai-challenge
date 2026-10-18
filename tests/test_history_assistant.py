"""Offline behavior checks for the history assistant."""

import importlib.util
import io
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import MagicMock, patch


SCRIPT = Path(__file__).resolve().parents[1] / "exercises" / "01-history-assistant.py"
spec = importlib.util.spec_from_file_location("history_assistant", SCRIPT)
assistant = importlib.util.module_from_spec(spec)
spec.loader.exec_module(assistant)


class HistoryAssistantTests(unittest.TestCase):
    def setUp(self):
        self.environment = patch.dict(
            assistant.os.environ,
            {
                "AZURE_OPENAI_ENDPOINT": "https://example.openai.azure.com/",
                "AZURE_OPENAI_API_KEY": "fake-test-key",
            },
            clear=True,
        )
        self.environment.start()
        self.addCleanup(self.environment.stop)
        dotenv = patch.object(assistant, "load_dotenv")
        dotenv.start()
        self.addCleanup(dotenv.stop)
        client_patch = patch.object(assistant, "AzureOpenAI")
        self.client_factory = client_patch.start()
        self.addCleanup(client_patch.stop)
        self.client = self.client_factory.return_value.__enter__.return_value
        self.client.chat.completions.create.return_value = SimpleNamespace(
            choices=[SimpleNamespace(message=SimpleNamespace(content="A historical answer."))]
        )

    def run_main(self, question="When did Rome fall?"):
        stdout, stderr = io.StringIO(), io.StringIO()
        with patch("builtins.input", return_value=question), redirect_stdout(stdout), redirect_stderr(stderr):
            code = assistant.main()
        return code, stdout.getvalue(), stderr.getvalue()

    def test_import_has_no_interactive_or_client_side_effects(self):
        module = importlib.util.module_from_spec(spec)
        with patch("builtins.input") as user_input, patch("openai.AzureOpenAI") as client:
            spec.loader.exec_module(module)
        user_input.assert_not_called()
        client.assert_not_called()

    def test_missing_or_blank_configuration_stops_before_input_or_client(self):
        for variable in ("AZURE_OPENAI_ENDPOINT", "AZURE_OPENAI_API_KEY"):
            for value in (None, "  "):
                with self.subTest(variable=variable, value=value):
                    with patch.dict(assistant.os.environ):
                        if value is None:
                            del assistant.os.environ[variable]
                        else:
                            assistant.os.environ[variable] = value
                        stdout, stderr = io.StringIO(), io.StringIO()
                        with patch("builtins.input") as user_input, redirect_stdout(stdout), redirect_stderr(stderr):
                            code = assistant.main()
                        self.assertEqual(code, 1)
                        self.assertIn(variable, stderr.getvalue())
                        self.assertEqual(stdout.getvalue(), "")
                        user_input.assert_not_called()
                        self.client_factory.assert_not_called()

    def test_success_preserves_request_contract_and_closes_client(self):
        code, stdout, stderr = self.run_main()
        self.assertEqual(code, 0)
        self.assertIn("A historical answer.", stdout)
        self.assertEqual(stderr, "")
        kwargs = self.client.chat.completions.create.call_args.kwargs
        self.assertEqual(kwargs["model"], "gpt-4o")
        self.assertEqual(kwargs["max_tokens"], 4096)
        self.assertEqual(kwargs["temperature"], 1.0)
        self.assertEqual(kwargs["top_p"], 1.0)
        self.assertEqual(kwargs["messages"][1], {"role": "user", "content": "When did Rome fall?"})
        self.assertIn("Você é um professor de história", kwargs["messages"][0]["content"])
        self.assertEqual(self.client_factory.call_args.kwargs["api_version"], "2024-12-01-preview")
        self.client_factory.return_value.__exit__.assert_called_once()

    def test_blank_question_does_not_create_client(self):
        code, _, stderr = self.run_main("  ")
        self.assertEqual(code, 1)
        self.assertIn("non-empty question", stderr)
        self.client_factory.assert_not_called()

    def test_api_errors_are_sanitized_and_close_client(self):
        sensitive = "fake-test-key https://private.example/internal"
        response = MagicMock(status_code=401)
        errors = (
            (assistant.APITimeoutError(request=MagicMock()), "timed out"),
            (assistant.APIConnectionError(message=sensitive, request=MagicMock()), "Could not connect"),
            (assistant.APIStatusError(sensitive, response=response, body={"secret": sensitive}), "HTTP 401"),
        )
        for error, expected in errors:
            with self.subTest(error=type(error).__name__):
                self.client_factory.reset_mock()
                self.client.chat.completions.create.side_effect = error
                code, stdout, stderr = self.run_main()
                self.assertEqual(code, 1)
                self.assertIn(expected, stderr)
                self.assertNotIn(sensitive, stderr)
                self.assertNotIn("fake-test-key", stderr)
                self.assertEqual(stdout, "")
                self.client_factory.return_value.__exit__.assert_called_once()

    def test_empty_model_output_is_reported(self):
        for choices in ([], [SimpleNamespace(message=SimpleNamespace(content=None))]):
            with self.subTest(choices=choices):
                self.client.chat.completions.create.return_value = SimpleNamespace(choices=choices)
                code, _, stderr = self.run_main()
                self.assertEqual(code, 1)
                self.assertIn("no text response", stderr)

    def test_invalid_client_configuration_is_sanitized(self):
        self.client_factory.side_effect = ValueError("fake-test-key")
        code, _, stderr = self.run_main()
        self.assertEqual(code, 1)
        self.assertIn("Invalid Azure OpenAI configuration", stderr)
        self.assertNotIn("fake-test-key", stderr)

    def test_cancelled_input_returns_130_without_creating_client(self):
        for error in (EOFError, KeyboardInterrupt):
            with self.subTest(error=error.__name__):
                with patch("builtins.input", side_effect=error), redirect_stderr(io.StringIO()):
                    self.assertEqual(assistant.main(), 130)
                self.client_factory.assert_not_called()


if __name__ == "__main__":
    unittest.main()

"""Regression checks for documentation validation failures and Markdown context."""

import tempfile
import unittest
from pathlib import Path

from tools.check_docs import check_documents


class DocumentationChecksTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        self.readme = self.root / "README.md"

    def check(self, content):
        self.readme.write_text(content, encoding="utf-8")
        return check_documents([self.readme], self.root)

    def test_nested_badge_links_and_duplicate_headings(self):
        errors, count = self.check(
            "# Guide\n\n[![Badge](https://example.com/badge.svg)](#guide-1)\n"
            "\n# Guide\n\n[Section](#guide)\n"
        )
        self.assertEqual(errors, [])
        self.assertEqual(count, 2)

    def test_missing_target_and_anchor_are_both_reported(self):
        errors, _ = self.check("# Guide\n\n[Missing](absent.md)\n[Missing anchor](#absent)\n")
        self.assertEqual(len(errors), 2)
        self.assertIn("missing local target", errors[0])
        self.assertIn("missing heading anchor", errors[1])

    def test_root_relative_and_encoded_targets(self):
        (self.root / "a file.md").write_text("# Target\n", encoding="utf-8")
        errors, count = self.check("# Guide\n\n[Target](/a%20file.md#target)\n")
        self.assertEqual(errors, [])
        self.assertEqual(count, 1)

    def test_missing_image_is_reported(self):
        errors, _ = self.check("# Guide\n\n![Image](missing.png)\n")
        self.assertEqual(len(errors), 1)
        self.assertIn("missing local target", errors[0])

    def test_links_and_headings_inside_fences_are_ignored(self):
        errors, count = self.check("# Guide\n\n```text\n# Hidden\n[Example](missing.md)\n```\n")
        self.assertEqual(errors, [])
        self.assertEqual(count, 0)
        errors, _ = self.check("# Guide\n\n```text\n# Hidden\n```\n\n[Hidden](#hidden)\n")
        self.assertEqual(len(errors), 1)

    def test_invalid_python_and_json_are_reported_without_execution(self):
        errors, _ = self.check("```python\ndef invalid(\n```\n\n```json\n{bad}\n```\n")
        self.assertEqual(len(errors), 2)
        self.assertIn("invalid python excerpt", errors[0])
        self.assertIn("invalid json excerpt", errors[1])
        errors, _ = self.check("```python\nraise RuntimeError('must not execute')\n```\n")
        self.assertEqual(errors, [])

    def test_async_fragment_is_accepted(self):
        errors, _ = self.check("```python\nasync for item in source:\n    await consume(item)\n```\n")
        self.assertEqual(errors, [])

    def test_unclosed_fence_and_embedded_shorter_fences(self):
        errors, _ = self.check("```text\nUnfinished\n")
        self.assertEqual(len(errors), 1)
        self.assertIn("unclosed code fence", errors[0])
        errors, _ = self.check("````text\n```\n[Example](missing.md)\n````\n")
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()

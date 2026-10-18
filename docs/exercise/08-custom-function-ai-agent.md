# Use custom functions in an AI agent

> Study notes from the 2025 challenge. See the [documentation scope and compatibility notes](../README.md#scope-and-compatibility) before following portal instructions or SDK examples.
> Python SDK excerpts use the historical connection-string API; they are not compatible examples for an arbitrary current SDK installation.

## Contents

- [Objective and prerequisites](#objective-and-prerequisites)
- [Prepare the project and workspace](#prepare-the-project-and-workspace)
- [Define a custom function](#define-a-custom-function)
- [Register the function with the historical SDK](#register-the-function-with-the-historical-sdk)
- [Run and inspect the external lab](#run-and-inspect-the-external-lab)
- [Cleanup and outcome](#cleanup-and-outcome)
- [Original learning references](#original-learning-references)

## Objective and prerequisites

Explore a technical-support agent that collects an email address and problem description, then creates a local ticket through a custom function. The course estimated about 30 minutes and assumed basic Python knowledge, Azure access, and a compatible project and model deployment.

## Prepare the project and workspace

The original portal exercise used a hub-based project, an AI resource, and a GPT-4o deployment. It showed Global Standard, a 50K TPM example allocation, and the DefaultV2 filter. Verify the supported region, model, tools, and quota for the actual lab environment.

Clone the starter repository into a new directory without deleting an existing checkout:

```bash
git clone https://github.com/MicrosoftLearning/mslearn-ai-agents ai-agents
```

The historical Python path was `ai-agents/Labfiles/03-ai-agent-functions/Python`. Consult the matching upstream revision or the [current exercise index](https://microsoftlearning.github.io/mslearn-ai-agents/) before relying on that path or installing dependencies.

In the selected Linux or Cloud Shell Bash lab directory:

```bash
python3 -m venv labenv
source labenv/bin/activate
```

The original lab used `python-dotenv`, `azure-identity`, and the historical project SDK. Those dependencies are separate from the history assistant maintained in this repository.

## Define a custom function

The following example belongs in the external lab's `user_functions.py`. Missing standard-library imports from the original notes are included here. Calling the function writes a file beside that module; this documentation update does not call it.

```python
import json
import uuid
from pathlib import Path
from typing import Any, Callable, Set


def submit_support_ticket(email_address: str, description: str) -> str:
    """Create a local support ticket and return a JSON confirmation.

    :param email_address: Requester's email address.
    :param description: Description of the technical problem.
    :return: JSON message containing the ticket reference.
    """
    script_dir = Path(__file__).parent
    ticket_number = str(uuid.uuid4()).replace('-', '')[:6]
    file_name = f"ticket-{ticket_number}.txt"
    file_path = script_dir / file_name
    text = f"Support ticket: {ticket_number}\nSubmitted by: {email_address}\nDescription:\n{description}"
    file_path.write_text(text, encoding="utf-8")
    message_json = json.dumps({"message": f"Support ticket {ticket_number} submitted."})
    return message_json


user_functions: Set[Callable[..., Any]] = {submit_support_ticket}
```

The six-character reference follows the original lab and is not collision-proof. A production ticket system would require persistence, validation, access controls, and handling of duplicate identifiers. The text file contains personal information, so use fictitious values in the exercise.

## Register the function with the historical SDK

This fragment assumes a matching connection-string SDK and a local `user_functions.py` module. Configure the external lab's variables before using it:

```python
import os

from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import FunctionTool, ToolSet
from user_functions import user_functions

load_dotenv()
PROJECT_CONNECTION_STRING = os.environ["PROJECT_CONNECTION_STRING"]
MODEL_DEPLOYMENT = os.environ["MODEL_DEPLOYMENT"]

# Conexão com o projeto
project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=PROJECT_CONNECTION_STRING,
)

# Criação do agente
with project_client:
    functions = FunctionTool(user_functions)
    toolset = ToolSet()
    toolset.add(functions)
    project_client.agents.enable_auto_function_calls(toolset=toolset)
    agent = project_client.agents.create_agent(
        model=MODEL_DEPLOYMENT,
        name="support-agent",
        instructions="Collect the email address and problem description before submitting a support ticket.",
        toolset=toolset,
    )
    thread = project_client.agents.create_thread()
```

This corrects the original incomplete credential placeholder and makes local automatic function execution explicit for the historical SDK. A complete external application still needs a message-and-run loop, argument validation, user interaction, and cleanup. Creating an agent and thread alone does not submit a ticket.

## Run and inspect the external lab

From the completed upstream project directory:

```bash
az login
python agent.py
```

Use a fictitious email address and a test problem description. Confirm that the agent collects both inputs, invokes the tool through the configured execution path, and returns the resulting ticket reference. Inspect the generated file and verify its contents against the supplied inputs.

The external `agent.py` is not part of this repository. Its Azure integration and filesystem side effects have not been exercised here.

## Cleanup and outcome

Remove local tickets containing test personal data and delete temporary agent, thread, and other cloud artifacts. Remove only dedicated lab resources after checking the resource group's contents.

The exercise demonstrates a declared Python function becoming an agent capability. The implementation and permissions behind the tool determine what the agent can actually do.

## Original learning references

- [Ai.azure.com](https://ai.azure.com)
- [03 agent custom functions](https://microsoftlearning.github.io/mslearn-ai-agents/Instructions/03-agent-custom-functions.html)

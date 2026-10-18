# Develop an AI agent with Code Interpreter

> Study notes from the 2025 challenge. See the [documentation scope and compatibility notes](../README.md#scope-and-compatibility) before following portal instructions or SDK examples.
> Python SDK excerpts use the historical connection-string API; they are not compatible examples for an arbitrary current SDK installation.

## Contents

- [Objective and prerequisites](#objective-and-prerequisites)
- [Prepare Azure resources](#prepare-azure-resources)
- [Prepare the external workspace](#prepare-the-external-workspace)
- [Configure the historical client](#configure-the-historical-client)
- [Upload data and create the agent](#upload-data-and-create-the-agent)
- [Process a conversation turn](#process-a-conversation-turn)
- [Retrieve artifacts and clean up agent state](#retrieve-artifacts-and-clean-up-agent-state)
- [Run the external lab](#run-the-external-lab)
- [Resource cleanup](#resource-cleanup)
- [Original learning references](#original-learning-references)

## Objective and prerequisites

Explore an agent that analyzes an uploaded dataset and generates charts with Code Interpreter. The course estimated about 30 minutes for the original lab. You need compatible Azure resources, a model deployment, access to the external starter project, and permission to upload the lab data.

## Prepare Azure resources

The historical exercise created a hub-based project and a GPT-4o deployment. Its example settings included Global Standard, automatic model-version updates, up to 50K TPM, and the DefaultV2 filter. Check actual model, tool, region, and quota support instead of assuming those settings remain available.

## Prepare the external workspace

Clone into a new folder. The destructive workspace deletion command from the original guide has been removed:

```bash
git clone https://github.com/MicrosoftLearning/mslearn-ai-agents ai-agents
```

The 2025 Python lab was under `ai-agents/Labfiles/02-build-ai-agent/Python`. Confirm the path and dependency versions for the matching upstream revision before changing directories or installing packages.

For a Linux or Cloud Shell Bash workspace, create an isolated environment from the selected lab directory:

```bash
python3 -m venv labenv
source labenv/bin/activate
```

The original dependency set included `python-dotenv`, `azure-identity`, and the historical `azure-ai-projects` preview. Follow the upstream revision's dependency instructions; a current project SDK uses a different API.

## Configure the historical client

In the external lab, populate `PROJECT_CONNECTION_STRING` and `MODEL_DEPLOYMENT` and authenticate with `az login`. These are external lab variables, not additions to the history assistant's root configuration.

The following historical excerpt assumes the corresponding SDK version and an uploaded-data path. It is not a standalone script or a tested current SDK example.

```python
import os
from pathlib import Path

from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import FilePurpose, CodeInterpreterTool

load_dotenv()
PROJECT_CONNECTION_STRING = os.environ["PROJECT_CONNECTION_STRING"]
MODEL_DEPLOYMENT = os.environ["MODEL_DEPLOYMENT"]

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(
        exclude_environment_credential=True,
        exclude_managed_identity_credential=True,
    ),
    conn_str=PROJECT_CONNECTION_STRING,
)
```

The credential exclusions reproduce the development-oriented lab setup. They are not a general production authentication policy.

## Upload data and create the agent

Historical excerpt, continuing with the configured `project_client`. Define `file_path` as the external lab's dataset path before using it:

```python
file = project_client.agents.upload_file_and_poll(
    file_path=file_path, purpose=FilePurpose.AGENTS
)
code_interpreter = CodeInterpreterTool(file_ids=[file.id])
agent = project_client.agents.create_agent(
    model=MODEL_DEPLOYMENT,
    name="data-agent",
    instructions="Analyze the file data. If the user requests a chart, create and save it as a PNG.",
    tools=code_interpreter.definitions,
    tool_resources=code_interpreter.resources,
)
thread = project_client.agents.create_thread()
```

Inspect the dataset before uploading it. Code Interpreter runs generated Python in the service environment; it does not run arbitrary code on this repository's host.

## Process a conversation turn

Historical excerpt; `user_prompt` is a string supplied by the external application's input loop:

```python
message = project_client.agents.create_message(
    thread_id=thread.id,
    role="user",
    content=user_prompt,
)
run = project_client.agents.create_and_process_run(
    thread_id=thread.id,
    agent_id=agent.id,
)
if run.status == "failed":
    print("The agent run failed. Review the run in the Azure portal.")
else:
    messages = project_client.agents.list_messages(thread_id=thread.id)
    last_msg = messages.get_last_text_message_by_role("assistant")
```

The complete application must handle other non-success states and the possibility of no assistant message. It must also provide the surrounding input loop and display logic.

## Retrieve artifacts and clean up agent state

Historical fragment, after a successful run with file annotations:

```python
for file_path_annotation in messages.file_path_annotations:
    project_client.agents.save_file(
        file_id=file_path_annotation.file_path.file_id,
        file_name=Path(file_path_annotation.text).name,
    )

project_client.agents.delete_agent(agent.id)
project_client.agents.delete_thread(thread.id)
```

In a complete application, use failure-safe cleanup and remove uploaded files and other temporary artifacts too. Deleting the agent and thread alone is not a guarantee that every billable resource or stored file has been removed. Review generated filenames before saving over local files.

## Run the external lab

From the completed upstream lab directory, authenticate and execute its application:

```bash
az login
python agent.py
```

Try “Which category has the highest cost?” and “Create a pie chart showing cost by category.” Inspect the calculations and resulting chart. The external lab's chat loop uses `quit` to exit.

`agent.py` and its dataset are not included in this repository. These steps have not been executed against Azure as part of the documentation update.

## Resource cleanup

Remove lab-only deployments, compute, agent artifacts, and other resources. Before deleting the dedicated resource group, inspect its contents and preserve anything shared or needed later.

## Original learning references

- [Ai.azure.com](https://ai.azure.com)
- [Portal.azure.com](https://portal.azure.com)
- [02 build ai agent](https://microsoftlearning.github.io/mslearn-ai-agents/Instructions/02-build-ai-agent.html)

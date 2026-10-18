# Develop an AI application with the Azure AI Foundry SDK

> Study notes from the 2025 challenge. See the [documentation scope and compatibility notes](../README.md#scope-and-compatibility) before following portal instructions or SDK examples.
> Python SDK excerpts use the historical connection-string API; they are not compatible examples for an arbitrary current SDK installation.

## Contents

- [SDK purpose](#sdk-purpose)
- [Historical package setup](#historical-package-setup)
- [Connect to a project](#connect-to-a-project)
- [Work with project connections](#work-with-project-connections)
- [Create an inference chat client](#create-an-inference-chat-client)
- [Create an Azure OpenAI chat client](#create-an-azure-openai-chat-client)
- [Summary](#summary)
- [Original learning references](#original-learning-references)

## SDK purpose

The project SDK in the 2025 course provided a common entry point to project connections, inference clients, and agent operations. Python and C# examples combined that SDK with service-specific libraries.

This module records the historical design. The runnable Azure OpenAI example maintained in this repository is [the history assistant](../../exercises/01-history-assistant.py), which uses its own resource endpoint and API key.

## Historical package setup

The following package list explains the dependencies used by the original excerpts. It is not an installation recipe for current SDK releases:

```text
azure-ai-projects   # historical preview API
azure-identity
azure-ai-inference # inference excerpt only
azure-ai-textanalytics # sentiment excerpt only
openai             # Azure OpenAI excerpt only
```

Use the SDK version and resource type required by the original lab when reproducing it. Do not install these packages into the history assistant environment merely to read the notes.

## Connect to a project

Historical Python excerpt; this connection-string factory belongs to the older SDK. It requires project configuration and an authenticated Azure identity with the necessary access. It is not executed by this repository's tests.

```python
import os

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

project_connection_string = os.environ["PROJECT_CONNECTION_STRING"]
project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=project_connection_string,
)
```

![Ai project overview](https://learn.microsoft.com/pt-br/training/wwl-data-ai/ai-foundry-sdk/media/ai-project-overview.png)

For CLI-based development authentication, use `az login` in the intended Azure tenant and subscription. Authentication alone does not grant authorization to the project or connected services.

## Work with project connections

Connections describe external resources such as AI services, storage, and search. The historical API exposed `connections.list()`, `connections.get()`, and `connections.get_default()`.

![Ai project connections](https://learn.microsoft.com/pt-br/training/wwl-data-ai/ai-foundry-sdk/media/ai-project-connections.png)

Historical excerpt, assuming `project_client` from the previous section and a matching SDK:

```python
from azure.ai.projects.models import ConnectionType
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

connection = project_client.connections.get_default(
    connection_type=ConnectionType.AZURE_AI_SERVICES,
    include_credentials=True,
)
with TextAnalyticsClient(
    endpoint=connection.endpoint_url,
    credential=AzureKeyCredential(connection.key),
) as text_analytics_client:
    text = "I hated the movie. It was so slow!"
    sentimentAnalysis = text_analytics_client.analyze_sentiment(documents=[text])[0]
    print(f"Text: {text}\nSentiment: {sentimentAnalysis.sentiment}")
```

Request credentials only when the application needs them, and do not print connection objects containing secrets. This excerpt assumes key-based access; it does not cover every connection authentication type.

## Create an inference chat client

The original course distinguished Azure AI model inference, Azure OpenAI, serverless APIs, and managed compute deployments. The appropriate client depends on the deployment's endpoint and protocol.

Historical inference excerpt, continuing with the configured project client:

```python
from azure.ai.inference.models import SystemMessage, UserMessage

chat = project_client.inference.get_chat_completions_client()
response = chat.complete(
    model="phi-4-model",
    messages=[
        SystemMessage("You are a helpful AI assistant that answers questions."),
        UserMessage(input("Enter a question: ")),
    ],
)
print(response.choices[0].message.content)
```

`phi-4-model` is an example deployment name, not a model provisioned by this repository.

## Create an Azure OpenAI chat client

Historical excerpt showing a project connection used to obtain an Azure OpenAI client:

```python
openai_client = project_client.inference.get_azure_openai_client(
    api_version="2024-06-01"
)
response = openai_client.chat.completions.create(
    model="gpt-4-model",
    messages=[
        {"role": "system", "content": "You are a helpful AI assistant that answers questions."},
        {"role": "user", "content": input("Enter a question: ")},
    ],
)
print(response.choices[0].message.content)
```

The API version and deployment name reflect the original material. They must match the service you use. The excerpts omit application-level validation and full lifecycle management; use the repository example for the maintained local CLI behavior.

## Summary

Project connections were used to discover resources and create clients in the historical SDK. Keep project access, service access, deployment configuration, and SDK compatibility distinct when reading or adapting the examples.

## Original learning references

- [Sdk overview](https://learn.microsoft.com/pt-br/azure/ai-foundry/how-to/develop/sdk-overview?tabs=sync&pivots=programming-language-python)

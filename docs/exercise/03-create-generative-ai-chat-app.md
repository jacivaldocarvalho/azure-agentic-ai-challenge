# Create a generative AI chat application

> Study notes from the 2025 challenge. See the [documentation scope and compatibility notes](../README.md#scope-and-compatibility) before following portal instructions or SDK examples.
> Python SDK excerpts use the historical connection-string API; they are not compatible examples for an arbitrary current SDK installation.

## Contents

- [Objective and prerequisites](#objective-and-prerequisites)
- [Project and deployment setup](#project-and-deployment-setup)
- [Prepare the external lab workspace](#prepare-the-external-lab-workspace)
- [Historical Python example](#historical-python-example)
- [Historical C# excerpt](#historical-c-excerpt)
- [Run and inspect the conversation](#run-and-inspect-the-conversation)
- [Optional direct Azure OpenAI client](#optional-direct-azure-openai-client)
- [Cleanup](#cleanup)
- [Original learning references](#original-learning-references)

## Objective and prerequisites

Explore a conversational client using the historical Azure AI Foundry project SDK. You need a compatible project, deployment, identity, and lab workspace. The code below documents the old connection-string API and is not a current SDK quickstart.

## Project and deployment setup

The 2025 lab created a hub-based project and a model deployment, then used that project's connection string and deployment name in the client configuration. Deployment settings such as region, quota, version policy, and content filtering must match the available service. The original walkthrough used GPT-4o and a 50K TPM example allocation.

## Prepare the external lab workspace

The chat application belongs to the Microsoft Learning repository, not this repository. Clone it into a new directory; do not delete an existing workspace to rerun the instructions:

```bash
git clone https://github.com/MicrosoftLearning/mslearn-ai-studio mslearn-ai-foundry
```

The historical lab used these paths beneath that checkout:

```text
labfiles/chat-app/python
labfiles/chat-app/c-sharp
```

Paths on an upstream branch can change. Locate the matching exercise in the [Microsoft Learning exercise index](https://microsoftlearning.github.io/mslearn-ai-studio/) and use its dependency instructions for the selected revision. The original C# notes referenced preview packages, including `Azure.AI.Projects` and `Azure.AI.Inference` version `1.0.0-beta.3`; they were not verified in this repository.

## Historical Python example

Dependencies used by this excerpt are `python-dotenv`, `azure-identity`, `azure-ai-projects`, and `azure-ai-inference`, with a historical project SDK matching the connection-string API. In the external lab, configure `PROJECT_CONNECTION_STRING` and `MODEL_DEPLOYMENT` in `.env` and authenticate with `az login`.

This excerpt includes the missing `os` import from the original notes. It illustrates the conversation loop and is not covered by the repository's executable-example tests.

```python
import os

from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.inference.models import SystemMessage, UserMessage, AssistantMessage

# Carrega configurações
load_dotenv()
project_connection = os.environ["PROJECT_CONNECTION_STRING"]
model_deployment = os.environ["MODEL_DEPLOYMENT"]

# Conecta ao projeto
with DefaultAzureCredential() as credential:
    with AIProjectClient.from_connection_string(
        conn_str=project_connection,
        credential=credential,
    ) as projectClient:
        # Cria cliente de chat
        chat = projectClient.inference.get_chat_completions_client()
        # Inicia a conversa
        prompt = [SystemMessage("You are a helpful AI assistant.")]
        while True:
            input_text = input("You: ")
            if input_text.lower() == "quit":
                break
            prompt.append(UserMessage(input_text))
            response = chat.complete(model=model_deployment, messages=prompt)
            completion = response.choices[0].message.content
            print(f"AI: {completion}")
            prompt.append(AssistantMessage(completion))
```

These configuration variables belong to the external lab, not the root `.env.example` for the history assistant. The excerpt omits error handling and conversation-length limits to focus on the learning pattern.

## Historical C# excerpt

This fragment assumes an existing .NET project, the original preview SDKs, and a populated `config` object from the lab's configuration setup. It is not a complete compilable application. The collection initializer adds messages to the SDK options instead of assigning a read-only message collection.

```csharp
using Azure.Identity;
using Azure.AI.Projects;
using Azure.AI.Inference;
using System;
using System.Collections.Generic;

var project_connection = config["ProjectConnectionString"];
var model_deployment = config["ModelDeployment"];

// Conecta ao projeto
var projectClient = new AIProjectClient(project_connection, new DefaultAzureCredential());
// Cria cliente de chat
var chat = projectClient.GetChatCompletionsClient();
// Inicia a conversa
var prompt = new List<ChatRequestMessage> {
    new ChatRequestSystemMessage("You are a helpful AI assistant.")
};

while (true)
{
    Console.Write("You: ");
    string? input_text = Console.ReadLine();
    if (input_text is null || input_text.ToLowerInvariant() == "quit") break;
    prompt.Add(new ChatRequestUserMessage(input_text));
    var options = new ChatCompletionsOptions { Model = model_deployment };
    foreach (var message in prompt) options.Messages.Add(message);
    var response = chat.Complete(options);
    Console.WriteLine($"AI: {response.Value.Content}");
    prompt.Add(new ChatRequestAssistantMessage(response.Value.Content));
}
```

## Run and inspect the conversation

In the external lab's selected language directory, run its completed application:

```bash
python chat-app.py
```

For the .NET project, use `dotnet run`. Try “What is the fastest animal in the world?” followed by “Where can I see one?” Inspect whether the follow-up uses the prior context. Type `quit` to end the conversation.

These filenames refer to the external lab checkout. They are not executable entry points in this repository.

## Optional direct Azure OpenAI client

The original guide also discussed calling Azure OpenAI directly instead of using project-based inference. For the maintained local example, use [the history assistant](../../exercises/01-history-assistant.py) and its [configuration instructions](../../README.md#run-the-python-example). It sends one question rather than implementing the multi-turn loop above.

## Cleanup

Remove resources created only for the exercise when finished. Review the resource group's contents before deleting it. Keep credentials out of committed configuration and shared terminal output.

## Original learning references

- [Ai.azure.com](https://ai.azure.com)
- [Portal.azure.com](https://portal.azure.com)
- [02a ai foundry sdk](https://microsoftlearning.github.io/mslearn-ai-studio/Instructions/02a-AI-foundry-sdk.html)

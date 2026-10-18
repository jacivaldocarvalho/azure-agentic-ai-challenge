# Learning documentation

## Scope and compatibility

These guides document the Microsoft AI Skills Challenge 2025. They have been edited into English and reviewed for local consistency. They preserve historical product names, portal screenshots, and learning topics; they are not a set of deployment procedures validated against every current Azure service.

The only executable application maintained in this repository is [the history assistant](../exercises/01-history-assistant.py). Its [offline tests](../tests/test_history_assistant.py) validate local behavior with a simulated client. Other Python and C# excerpts are learning fragments or examples for external Microsoft Learning labs. Their prerequisites and omitted context are stated in each guide.

The root `.env.example` and `requirements.txt` configure only the history assistant. Dependencies, variables, data files, and entry points mentioned in external labs belong to those labs and should use separate workspaces and environments.

### Project SDK generations

Some excerpts use `AIProjectClient.from_connection_string` and methods under `project_client.inference` or `project_client.agents`. Those examples belong to the historical project SDK. The [tagged Azure AI Projects preview documentation](https://github.com/Azure/azure-sdk-for-python/blob/azure-ai-projects_1.0.0b10/sdk/ai/azure-ai-projects/README.md) provides a reference for that API generation; it is not a tested dependency lock for these guides.

The [current Azure AI Projects documentation](https://learn.microsoft.com/en-us/python/api/overview/azure/ai-projects-readme?view=azure-python) describes an endpoint-based client. Do not mix that constructor and operation model with the connection-string excerpts. Reproducing an old lab requires matching its resource type, SDK version, data, and configuration; adapting it to a new API is a separate implementation task.

### Semantic Kernel orchestration

Microsoft's [archived AgentChat documentation](https://learn.microsoft.com/en-us/semantic-kernel/support/archive/agent-chat) identifies `AgentGroupChat` as an experimental feature that is no longer maintained. The [group chat orchestration migration guide](https://learn.microsoft.com/en-us/semantic-kernel/support/migration/group-chat-orchestration-migration-guide) explains the replacement pattern.

The module and exercise retain this older pattern for historical learning. No migration to a different runtime or provider API is implemented in this repository.

### Portal, upstream labs, and screenshots

Portal navigation, model availability, quotas, and upstream repository paths can change. Numbers such as TPM allocations, VM sizes, and instance counts record original lab settings rather than current requirements. Original lab URLs are retained as historical references; some may have moved. Use these verified upstream indexes to find the maintained material:

- [Microsoft Learning generative AI exercises](https://microsoftlearning.github.io/mslearn-ai-studio/).
- [Microsoft Learning agent exercises](https://microsoftlearning.github.io/mslearn-ai-agents/).

Screenshots retain their original language and content. Image filenames, captions, and surrounding documentation use English. No screenshot pixels were edited.

### Retrieval terminology

The notes distinguish vector retrieval from keyword retrieval and semantic reranking. Refer to the official [vector search overview](https://learn.microsoft.com/en-us/azure/search/vector-search-overview) and [hybrid search overview](https://learn.microsoft.com/en-us/azure/search/hybrid-search-overview) when adapting the RAG exercises.

## Modules

| Module | Guide |
| --- | --- |
| 01 | [Plan Azure AI solutions](module/01-planning-azure-ai-solutions.md) |
| 02 | [Explore and deploy models](module/02-explore-and-deploy-models-azure-ai-foundry.md) |
| 03 | [Develop with the project SDK](module/03-develop-ai-app-azure-ai-foundry.md) |
| 04 | [Introduction to prompt flow](module/04-intro-prompt-flow-develop-language-model-app-azure-ai-studio.md) |
| 05 | [Build a RAG solution](module/05-build-rag-data-azure-ai-studio.md) |
| 06 | [AI agent fundamentals](module/06-basic-ai-agents-azure.md) |
| 07 | [Agent security controls](module/07-intro-ai-agent-service-security-controls.md) |
| 08 | [Develop an Azure AI agent](module/08-develop-ai-agent-azure-service.md) |
| 09 | [Integrate custom tools](module/09-integrate-custom-tools-into-agent.md) |
| 10 | [Orchestrate multiple agents](module/10-orchestrate-multi-agent-solution-semantic-kernel.md) |

## Exercises

| Exercise | Guide |
| --- | --- |
| 01 | [Prepare an AI development project](exercise/01-ai-development-project.md) |
| 02 | [Choose and deploy a model](exercise/02-choose-deploy-language-model.md) |
| 03 | [Create a generative chat application](exercise/03-create-generative-ai-chat-app.md) |
| 04 | [Manage a conversation with prompt flow](exercise/04-prompt-flow-manage-conversation-chat-app.md) |
| 05 | [Use your own data with RAG](exercise/05-create-generative-ai-app-data-rag.md) |
| 06 | [Explore agent development](exercise/06-explore-ai-agent-development.md) |
| 07 | [Develop an agent with Code Interpreter](exercise/07-develop-ai-agent.md) |
| 08 | [Use custom functions](exercise/08-custom-function-ai-agent.md) |
| 09 | [Explore a multi-agent solution](exercise/09-develop-multi-agent-solution.md) |

## Validation boundaries

The documentation review checks local links, heading anchors, image references, code fences, and syntax of Python and JSON excerpts. These checks do not execute cloud operations, compile C#, validate portal steps, or establish SDK runtime compatibility for external labs. Live resources are not provisioned or changed as part of these checks.

Cloud exercises may incur charges. Use fictitious data where possible and remove only resources dedicated to the lab after checking for shared dependencies.

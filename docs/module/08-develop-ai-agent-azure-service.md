# Develop an agent with Azure AI Agent Service

> Study notes from the 2025 challenge. See the [documentation scope and compatibility notes](../README.md#scope-and-compatibility) before following portal instructions or SDK examples.
> Python SDK excerpts use the historical connection-string API; they are not compatible examples for an arbitrary current SDK installation.

## Contents

- [Purpose and use cases](#purpose-and-use-cases)
- [Agent capabilities](#agent-capabilities)
- [Resource configurations](#resource-configurations)
- [Historical application lifecycle](#historical-application-lifecycle)
- [Knowledge tools](#knowledge-tools)
- [Action tools](#action-tools)
- [Design considerations](#design-considerations)
- [Summary](#summary)
- [Original learning references](#original-learning-references)

## Purpose and use cases

An AI agent uses a model, instructions, knowledge, and tools to perform a task. Potential uses include scheduling, document-based support, research, sales assistance, data analysis, and development workflows.

The 2025 course introduced a managed agent service to reduce the code required for conversation state and tool integration. Managed infrastructure does not guarantee application correctness, unrestricted availability, or compliance by itself.

## Agent capabilities

The learning material covered configurable instructions, model deployments, conversation state, file retrieval, code execution, search, and custom functions. Availability and configuration depend on the selected model, service, and API version.

A tool-equipped agent can automate repetitive steps or help users make decisions. It also introduces failure modes: incorrect tool selection, invalid arguments, unsupported answers, and actions outside the intended workflow. Application controls and evaluation remain necessary.

## Resource configurations

The historical basic setup combined an AI hub, project, and AI services resource.

![Basic agent setup resources](https://learn.microsoft.com/pt-br/training/wwl-data-ai/develop-ai-agent-azure/media/basic-agent-setup-resources.png)

The historical standard setup added services such as storage, search, and Key Vault to support more explicit resource control.

![Standard agent setup resources](https://learn.microsoft.com/pt-br/training/wwl-data-ai/develop-ai-agent-azure/media/standard-agent-setup-resources.png)

These diagrams document the course environment. The repository does not provision either architecture, and they should not be interpreted as mandatory current deployment templates.

## Historical application lifecycle

The course used this sequence for a thread-and-run agent:

![Ai agent code pattern](https://learn.microsoft.com/pt-br/training/wwl-data-ai/develop-ai-agent-azure/media/ai-agent-code-pattern.png)

1. Connect to the project using the matching SDK and an authorized identity.
2. Create an agent or retrieve an existing one.
3. Configure its deployment, instructions, tools, and associated resources.
4. Create a thread for the conversation.
5. Add a user message and start a run.
6. Inspect the run status, retrieve messages, and process generated artifacts.
7. Repeat for additional questions.
8. Delete temporary agent, thread, file, and other lab resources when finished.

A thread stores conversation messages; a run represents processing by an agent. Check the run status rather than assuming a submitted request has completed successfully. Client-side functions require execution support in the application or SDK, rather than being executed merely because their names are declared.

## Knowledge tools

The course introduced tools for retrieving evidence from files, Azure AI Search, Bing grounding, and Microsoft Fabric. These provide information used to answer questions; their usefulness depends on the data, permissions, and retrieval behavior.

![Portal tools](https://learn.microsoft.com/pt-br/training/wwl-data-ai/develop-ai-agent-azure/media/portal-tools.png)

## Action tools

| Tool | Role |
| --- | --- |
| Code Interpreter | Run model-generated Python in a supported sandbox and work with uploaded files. |
| Custom function | Execute application-defined code through a declared tool interface. |
| Azure Functions | Integrate a supported deployed function workflow. |
| OpenAPI tool | Expose supported external HTTP operations from an API description. |

The original notes incorrectly suggested MATLAB execution for Code Interpreter; the course tool runs Python. Tool declarations must be paired with the correct execution mechanism and resource access.

## Design considerations

Keep instructions focused on the task and make each tool's purpose and parameters explicit. Validate arguments and outputs in application code. Keep generated artifacts and thread data only as long as needed, and distinguish a proposed action from one that has actually been executed.

## Summary

The historical agent workflow combined a deployed model, instructions, tools, threads, and runs. Learn the lifecycle and resource responsibilities before extending it with custom knowledge or actions.

## Original learning references

- [Microsoft.azure ai agent service](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.azure-ai-agent-service)

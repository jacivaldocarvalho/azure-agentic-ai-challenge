# Plan and prepare Azure AI solutions

> Study notes from the 2025 challenge. See the [documentation scope and compatibility notes](../README.md#scope-and-compatibility) before following portal instructions or SDK examples.

## Contents

- [Introduction](#introduction)
- [AI capabilities](#ai-capabilities)
- [Azure AI services](#azure-ai-services)
- [Hubs and projects](#hubs-and-projects)
- [Access and governance](#access-and-governance)
- [Developer tools and SDKs](#developer-tools-and-sdks)
- [Responsible AI](#responsible-ai)
- [Summary](#summary)
- [Original learning references](#original-learning-references)

## Introduction

Planning an AI application starts with its intended users, inputs, outputs, data, and operational constraints. A solution may combine machine learning models, hosted AI services, prompt engineering, and application code. Select the services needed for the problem before provisioning resources.

## AI capabilities

| Capability | Purpose | Example |
| --- | --- | --- |
| Generative AI | Generate content from instructions and context. | Draft a property listing. |
| Agents | Combine a generative model, knowledge, and actions. | Schedule travel and prepare an expense claim. |
| Computer vision | Interpret images and video. | Identify products at checkout. |
| Speech | Recognize, synthesize, or translate speech. | Provide a voice interface. |
| Natural language processing | Analyze, classify, or summarize language. | Classify customer feedback. |
| Information extraction | Extract structured information from content. | Read purchase details from receipts. |
| Decision support | Use learned patterns to inform predictions. | Estimate demand from historical data. |

## Azure AI services

The original course surveyed these service families:

| Service | Capability |
| --- | --- |
| Azure OpenAI | Hosted generative models. |
| Azure AI Vision | Image analysis, captions, and text recognition. |
| Azure AI Speech | Speech recognition, synthesis, and translation. |
| Azure AI Language | Entities, sentiment, summarization, and conversational language. |
| Azure AI Content Safety | Detection of potentially harmful content. |
| Azure AI Translator | Text translation. |
| Azure AI Face | Face detection and analysis, with access restrictions for some features. |
| Azure AI Custom Vision | Custom image classification and object detection. |
| Azure AI Document Intelligence | Extraction of document fields and structure. |
| Azure AI Content Understanding | Analysis of multimodal content. |
| Azure AI Search | Indexing and retrieval, including retrieval for generative applications. |

A standalone service resource can isolate access and billing. A multi-service resource can simplify management when the application needs several supported services. Do not assume that every capability, pricing tier, or region is available for a particular subscription.

Evaluate regional availability, model capacity, quotas, data residency, authentication, and cost. Estimate model usage as well as storage, search, development compute, and deployed endpoints.

## Hubs and projects

The 2025 material used hub-based projects. A hub grouped shared resources and governance; a project organized the assets and development work of an individual solution. Connections exposed services such as storage, search, and AI resources to the project.

![Ai foundry hub](https://learn.microsoft.com/pt-br/training/wwl-data-ai/prepare-azure-ai-development/media/ai-foundry-hub.png)

Plan shared connections at the hub level and add project-specific resources only where needed. Separate hubs when teams require different governance or network boundaries. Project assets may include model deployments, data, indexes, prompt flows, evaluations, and development environments.

![Ai foundry project](https://learn.microsoft.com/pt-br/training/wwl-data-ai/prepare-azure-ai-development/media/ai-foundry-project.png)

## Access and governance

Identify who needs to administer infrastructure, develop applications, deploy models, or only inspect resources. The course discussed these roles:

| Role | Intended responsibility in the historical setup |
| --- | --- |
| Owner | Manage resources and access assignments. |
| Contributor | Manage resources without assigning access. |
| Azure AI Developer | Develop project assets within the assigned scope. |
| Azure AI Inference Deployment Operator | Perform deployment-related operations. |
| Reader | Inspect resources. |

Role definitions and automatic assignments depend on the resource model. Verify the actual assignments rather than assuming project membership grants every required data-plane permission. Check user access, service identities, connected-resource permissions, and network reachability separately.

## Developer tools and SDKs

Choose tools that fit the team's language and workflow: Visual Studio for .NET development, VS Code for a broader set of languages, and GitHub for source control and review. GitHub Copilot can assist development but does not replace testing or review.

The course also demonstrated a hosted VS Code container environment with SDKs preinstalled. That was a development option in the learning environment, not a repository requirement.

![Vs code](https://learn.microsoft.com/pt-br/training/wwl-data-ai/prepare-azure-ai-development/media/vs-code.png)

SDK categories covered in the course include:

- Project SDKs for accessing project assets and connections.
- Service SDKs and REST APIs for individual AI capabilities.
- Agent SDKs and frameworks such as Semantic Kernel and AutoGen.
- Prompt flow for organizing model interactions into workflows.

Keep examples aligned with the installed SDK version. A current project endpoint is different from the connection string used in historical samples.

## Responsible AI

| Principle | Engineering consideration |
| --- | --- |
| Fairness | Evaluate outcomes across relevant user groups and representative data. |
| Reliability and safety | Test failures, uncertainty, and the consequences of incorrect predictions. |
| Privacy and security | Protect training data, prompts, outputs, and access to tools. |
| Inclusiveness | Include diverse users and accessibility needs in design and testing. |
| Transparency | Explain the system's purpose, limitations, and use of data. |
| Accountability | Assign responsibility for decisions, validation, and operation. |

These considerations belong throughout the development lifecycle. Tools can help assess risks, but the team remains responsible for the application and its effects.

## Summary

Define the AI capability first, then select services, resource boundaries, development tools, access controls, and evaluation criteria. Plan costs and quotas alongside functional requirements.

## Original learning references

- [What are ai services](https://learn.microsoft.com/pt-br/azure/ai-services/what-are-ai-services#available-azure-ai-services?azure-portal=true)
- [Table](https://azure.microsoft.com/pt-br/explore/global-infrastructure/products-by-region/table)
- [Cognitive services](https://azure.microsoft.com/pt-br/pricing/details/cognitive-services/)
- [Calculator](https://azure.microsoft.com/pt-br/pricing/calculator/)
- [Ai resources](https://learn.microsoft.com/pt-br/azure/ai-foundry/concepts/ai-resources)
- [Connections](https://learn.microsoft.com/pt-br/azure/ai-foundry/concepts/connections)
- [Rbac azure ai foundry](https://learn.microsoft.com/pt-br/azure/ai-foundry/concepts/rbac-azure-ai-foundry)
- [Region support](https://learn.microsoft.com/pt-br/azure/ai-foundry/reference/region-support)
- [Costs plan manage](https://learn.microsoft.com/pt-br/azure/ai-foundry/how-to/costs-plan-manage)
- [Quota](https://learn.microsoft.com/pt-br/azure/ai-foundry/how-to/quota)
- [Vscode](https://learn.microsoft.com/pt-br/azure/ai-foundry/how-to/develop/vscode)
- [Sdk overview](https://learn.microsoft.com/pt-br/azure/ai-foundry/how-to/develop/sdk-overview?tabs=sync&pivots=programming-language-python)
- [Sdk package resources](https://learn.microsoft.com/pt-br/azure/ai-services/reference/sdk-package-resources?pivots=programming-language-csharp)
- [Getting started](https://microsoft.github.io/autogen/0.2/docs/Getting-Started/)
- [Overview](https://learn.microsoft.com/pt-br/semantic-kernel/overview/)
- [Index](https://microsoft.github.io/promptflow/index.html)
- [Official learning resource](https://azure.microsoft.com/pt-br/solutions/ai)

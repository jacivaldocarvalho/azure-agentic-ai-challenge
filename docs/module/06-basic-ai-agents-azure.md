# AI agent fundamentals in Azure

> Study notes from the 2025 challenge. See the [documentation scope and compatibility notes](../README.md#scope-and-compatibility) before following portal instructions or SDK examples.

## Contents

- [What is an AI agent?](#what-is-an-ai-agent)
- [Development options in the 2025 course](#development-options-in-the-2025-course)
- [Choose an approach](#choose-an-approach)
- [Agent components](#agent-components)
- [Summary](#summary)

## What is an AI agent?

An agent combines a generative model, contextual information, and tools to carry out a task. It can interpret a request, retrieve knowledge, and propose or perform an action through application code. Its authority and capabilities come from the tools and permissions provided by the application.

In an expense-management example:

1. An employee asks which expenses can be reimbursed.
2. The agent retrieves the relevant expense policy.
3. The model generates an answer using that policy.
4. A tool can prepare or submit an expense claim when the workflow permits it.

A travel agent could collaborate with the expense agent by handing over receipts and booking details. This is a conceptual workflow, not functionality implemented in this repository.

## Development options in the 2025 course

| Technology | Role in the original learning material |
| --- | --- |
| Azure AI Agent Service | Managed creation and use of agents integrated with Azure resources. |
| OpenAI Assistants API | Assistant-oriented model and tool interactions available at the time. |
| Semantic Kernel | Application SDK and agent collaboration patterns. |
| AutoGen | Agent experimentation and research workflows. |
| Microsoft 365 Agents SDK | Custom agent applications delivered through supported channels. |
| Microsoft Copilot Studio | Visual, low-code agent development. |
| Agent builder in Microsoft 365 Copilot | Declarative agents for business users. |

This table records the course landscape, not a recommendation to start a new project with every listed API. Check the provider's lifecycle and migration documentation before choosing a framework.

## Choose an approach

Consider the audience, implementation skills, channels, data sources, hosting needs, and required control over application logic. A visual tool can suit a focused business workflow. A code-based approach can be appropriate for custom integrations and application-specific behavior.

Start with a single agent when it can solve the task. Multiple agents add routing, shared-state, termination, evaluation, and cost considerations. Add them only when task specialization or coordination provides a clear benefit.

## Agent components

An agent in the course had three main components:

- A deployed generative model for interpreting requests and producing responses.
- Knowledge sources such as documents, a search index, or supported web grounding.
- Tools such as custom functions, Azure Functions, or a code interpreter.

The historical service organized conversations into threads, retaining exchanged messages and generated artifacts. The application created runs to process those messages and retrieved the results afterward.

Tool descriptions tell the model what a function can do, but application code still controls execution, validation, and permissions. A model-generated request does not itself authorize a real-world action.

## Summary

Agents extend conversational applications with knowledge and actions. Choose an implementation approach that matches the workflow, define its authority, and keep collaboration as simple as the task allows.

# Introduction to prompt flow for language model applications

> Study notes from the 2025 challenge. See the [documentation scope and compatibility notes](../README.md#scope-and-compatibility) before following portal instructions or SDK examples.

## Contents

- [Introduction](#introduction)
- [Application lifecycle](#application-lifecycle)
- [Flow structure and tools](#flow-structure-and-tools)
- [Connections and runtimes](#connections-and-runtimes)
- [Variants and deployment](#variants-and-deployment)
- [Evaluation and monitoring](#evaluation-and-monitoring)
- [Summary](#summary)
- [Original learning references](#original-learning-references)

## Introduction

An LLM application combines model calls, application logic, and sometimes external data. Prompt flow organizes these operations into a workflow that can be developed, tested, evaluated, and deployed. The course used the Azure AI Studio experience; screenshots and labels belong to that environment.

![Prompt flow feature](https://learn.microsoft.com/pt-br/training/wwl-data-ai/get-started-prompt-flow-ai-studio/media/prompt-flow-feature.png)

A prompt expresses a task or question. A flow describes the sequence of operations that produces an application result from its inputs.

## Application lifecycle

The course divided development into initialization, experimentation, evaluation and refinement, and production.

![Development lifecycle](https://learn.microsoft.com/pt-br/training/wwl-data-ai/get-started-prompt-flow-ai-studio/media/development-lifecycle.png)

### Initialization

Define the task, expected outputs, and success criteria. For a news classifier, identify categories and collect a small, representative set of articles. Include edge cases and remove sensitive data that is unnecessary for the task. Build an initial prompt and flow.

![Initialization](https://learn.microsoft.com/pt-br/training/wwl-data-ai/get-started-prompt-flow-ai-studio/media/initialization.png)

### Experimentation

Run the flow on the small dataset, inspect failures, and change prompts or workflow steps. Repeat until the flow is ready for broader evaluation. Keep comparisons tied to the same inputs and evaluation criteria.

![Experimentation](https://learn.microsoft.com/pt-br/training/wwl-data-ai/get-started-prompt-flow-ai-studio/media/experimentation.png)

### Evaluation and refinement

Evaluate on a larger, representative dataset to measure generalization and identify bottlenecks. After a change, use the smaller dataset for quick feedback before repeating the broader evaluation.

### Production

Optimize the flow, deploy an endpoint, collect usage signals and user feedback, and revisit experiments when quality or operating conditions change.

![Production](https://learn.microsoft.com/pt-br/training/wwl-data-ai/get-started-prompt-flow-ai-studio/media/production.png)

![Detailed lifecycle](https://learn.microsoft.com/pt-br/training/wwl-data-ai/get-started-prompt-flow-ai-studio/media/detailed-lifecycle.png)

## Flow structure and tools

A flow contains inputs, processing nodes, and outputs. A node may consume a flow input or another node's result.

![Flow pipeline](https://learn.microsoft.com/pt-br/training/wwl-data-ai/get-started-prompt-flow-ai-studio/media/flow-pipeline.png)

| Tool | Role |
| --- | --- |
| LLM | Call a language model with a configured prompt. |
| Python | Execute custom application logic. |
| Prompt | Build a prompt string for another step. |

The original material described standard flows for general tasks, chat flows for conversations, and evaluation flows for measuring results. Declare expected inputs and outputs explicitly so data can move between nodes consistently.

## Connections and runtimes

Connections hold the endpoint and authentication details needed for external services. The learning environment used managed secret storage for those connections. Configure access for the identity running the flow and avoid exposing keys in prompt text or logs.

![Connections](https://learn.microsoft.com/pt-br/training/wwl-data-ai/get-started-prompt-flow-ai-studio/media/connections.png)

| Connection in the course | Example tools |
| --- | --- |
| Azure OpenAI or OpenAI | LLM and Python tools. |
| Azure AI Search | Search and retrieval tools. |
| Serp | Search API tools. |
| Custom | Python integrations. |

A runtime combines compute with an environment containing the packages required by the flow. A managed default environment can help experimentation; custom code may require an explicitly configured environment.

![Runtimes](https://learn.microsoft.com/pt-br/training/wwl-data-ai/get-started-prompt-flow-ai-studio/media/runtimes.png)

## Variants and deployment

Variants compare configurations of a node, such as prompt text, connection, or model settings. Run variants against the same evaluation data to decide whether a change improves quality.

The course deployed flows to online endpoints, which callers could invoke from an application. Deployment also introduces authentication, compute, scaling, cost, and data-collection decisions. This repository does not contain a deployed flow.

## Evaluation and monitoring

| Metric | Question |
| --- | --- |
| Groundedness | Is the answer supported by the supplied source? |
| Relevance | Does it address the user's request? |
| Coherence | Is it logically organized? |
| Fluency | Is it linguistically clear? |
| Similarity | Does it agree with the expected answer under the chosen evaluator? |

Combine evaluations with latency, failures, resource use, and user feedback. When performance falls short, return to experimentation instead of assuming deployment completes development.

## Summary

Prompt flow connects inputs, tools, models, and outputs. Its value comes from making experiments and evaluation repeatable throughout the application lifecycle.

## Original learning references

- [How to customize session base image](https://learn.microsoft.com/pt-br/azure/machine-learning/prompt-flow/how-to-customize-session-base-image?view=azureml-api-2)

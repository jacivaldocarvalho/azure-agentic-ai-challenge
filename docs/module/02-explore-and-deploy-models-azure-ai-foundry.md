# Explore and deploy models in Azure AI Foundry

> Study notes from the 2025 challenge. See the [documentation scope and compatibility notes](../README.md#scope-and-compatibility) before following portal instructions or SDK examples.

## Contents

- [Language model fundamentals](#language-model-fundamentals)
- [Explore the model catalog](#explore-the-model-catalog)
- [Compare evaluation metrics](#compare-evaluation-metrics)
- [Deploy a model to an endpoint](#deploy-a-model-to-an-endpoint)
- [Test in the playground](#test-in-the-playground)
- [Improve prompts](#improve-prompts)
- [Choose an optimization strategy](#choose-an-optimization-strategy)
- [Summary](#summary)
- [Learning material illustrations](#learning-material-illustrations)
- [Original learning references](#original-learning-references)

## Language model fundamentals

Natural language processing includes translation, classification, entity extraction, summarization, question answering, and language generation. Transformer architectures use attention and positional information to model relationships between tokens. The 2017 paper *Attention Is All You Need* introduced the transformer architecture discussed in the course.

Pretrained foundation models provide a starting point for many tasks. The original notes compared these families:

| Family | Learning focus |
| --- | --- |
| BERT | Bidirectional representations for language understanding tasks. |
| GPT | Autoregressive text generation and conversational applications. |
| Llama | Open model families used for generation and chat. |
| Phi | Smaller models intended for scenarios with tighter resource constraints. |

Capabilities, context lengths, licenses, and supported deployments vary by specific model and version.

## Explore the model catalog

Use the catalog to filter by task, provider, language support, and deployment options. Read the model card to understand training data, intended use, limitations, license terms, and evaluation results. The original course also introduced models distributed through Hugging Face.

![Model catalog](https://learn.microsoft.com/pt-br/training/wwl-data-ai/explore-models-azure-ai-studio/media/model-catalog.png)

Compare shortlisted models against representative application inputs rather than relying on a catalog ranking alone.

![Model benchmarks](https://learn.microsoft.com/pt-br/training/wwl-data-ai/explore-models-azure-ai-studio/media/model-benchmarks.png)

## Compare evaluation metrics

| Metric | What to examine |
| --- | --- |
| Accuracy | Correctness on a defined task; exact-match and code pass rates measure different things. |
| Coherence | Logical structure and consistency. |
| Fluency | Readability and grammatical quality. |
| Similarity | Agreement with an expected answer under the evaluator's definition. |
| Groundedness | Support for the answer in the provided evidence. |
| Relevance | Whether the answer addresses the question. |

Record the dataset, evaluator, model version, latency, and cost when comparing results. Scores from different benchmarks are not automatically comparable. An answer can be fluent and still be factually wrong.

## Deploy a model to an endpoint

An application calls a deployed model through an endpoint. Depending on the service, multiple deployments can share a resource endpoint, and the request identifies the deployment to use. A deployment name is an application-facing identifier and need not be identical to the model family name.

The 2025 course covered Azure OpenAI deployments, Azure AI model inference, serverless APIs, and managed compute. Availability, billing, authentication, and quotas differ across these options. Check the selected model's deployment instructions and the subscription's regional capacity before creating resources.

Historical request shape, shown only to explain the URL components:

```text
https://your-resource.openai.azure.com/openai/deployments/your-deployment/chat/completions?api-version=your-api-version
```

Keep keys out of source code. Use the authentication mechanism supported by the resource and SDK, with permissions scoped to the application.

## Test in the playground

The chat playground lets you choose a deployment, set system instructions, vary model parameters, and inspect responses before integrating the model into application code. Save representative prompts and expected behavior so comparisons can be repeated.

![Chat playground](https://learn.microsoft.com/pt-br/training/wwl-data-ai/explore-models-azure-ai-studio/media/chat-playground.png)

## Improve prompts

Use clear task instructions, delimiters, output constraints, and examples. Provide relevant context where the model needs information that is absent from its training data.

![Chat with model](https://learn.microsoft.com/pt-br/training/wwl-data-ai/explore-models-azure-ai-studio/media/chat-with-model.png)

![Clear instructions](https://learn.microsoft.com/pt-br/training/wwl-data-ai/explore-models-azure-ai-studio/media/clear-instructions.png)

![Format instructions](https://learn.microsoft.com/pt-br/training/wwl-data-ai/explore-models-azure-ai-studio/media/format-instructions.png)

System instructions define the assistant's role and expected behavior. One-shot or few-shot examples demonstrate the desired output pattern.

![Use cues](https://learn.microsoft.com/pt-br/training/wwl-data-ai/explore-models-azure-ai-studio/media/use-cues.png)

![Chat json](https://learn.microsoft.com/pt-br/training/wwl-data-ai/explore-models-azure-ai-studio/media/chat-json.png)

For reasoning tasks, compare the final answer and a concise explanation against known constraints; a plausible explanation is not proof of correctness.

![Use shots](https://learn.microsoft.com/pt-br/training/wwl-data-ai/explore-models-azure-ai-studio/media/use-shots.png)

Add grounding information explicitly when an answer must refer to a specific source.

![Chain of thought](https://learn.microsoft.com/pt-br/training/wwl-data-ai/explore-models-azure-ai-studio/media/chain-of-thought.png)

## Choose an optimization strategy

Prompt engineering can improve instructions and formatting. RAG supplies retrieved information at request time. Fine-tuning changes model behavior using training examples and may help with consistent task performance or style. These techniques address different needs and can be combined after evaluation establishes a benefit.

![Add context](https://learn.microsoft.com/pt-br/training/wwl-data-ai/explore-models-azure-ai-studio/media/add-context.png)

## Summary

Select models by task fit, evaluate them on relevant inputs, deploy with an appropriate hosting option, and improve measured behavior through prompts, retrieval, or training. Treat portal screenshots and model examples as historical learning material.

## Learning material illustrations

Historical illustrations retained from the original notes.

![Model optimization](https://learn.microsoft.com/pt-br/training/wwl-data-ai/explore-models-azure-ai-studio/media/model-optimization.png)

## Original learning references

- [1706.03762](https://arxiv.org/abs/1706.03762)
- [Models](https://huggingface.co/models)
- [Bert](https://huggingface.co/docs/transformers/main/model_doc/bert)
- [Models](https://learn.microsoft.com/pt-br/azure/ai-services/openai/concepts/models?tabs=global-standard%2Cstandard-chat-completions#model-summary-table-and-region-availability?azure-portal=true)
- [Models](https://learn.microsoft.com/pt-br/azure/ai-services/openai/concepts/models?tabs=global-standard%2Cstandard-chat-completions)
- [Models](https://learn.microsoft.com/pt-br/azure/ai-foundry/model-inference/concepts/models)
- [Model catalog overview](https://learn.microsoft.com/pt-br/azure/ai-foundry/how-to/model-catalog-overview#content-safety-for-models-deployed-via-serverless-apis?azure-portal=true)
- [Model catalog overview](https://learn.microsoft.com/pt-br/azure/ai-foundry/how-to/model-catalog-overview#availability-of-models-for-deployment-as-managed-compute?azure-portal=true)

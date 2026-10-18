# Build a RAG solution with your own data

> Study notes from the 2025 challenge. See the [documentation scope and compatibility notes](../README.md#scope-and-compatibility) before following portal instructions or SDK examples.

## Contents

- [Grounding model responses](#grounding-model-responses)
- [Retrieval-augmented generation](#retrieval-augmented-generation)
- [Make the data searchable](#make-the-data-searchable)
- [Build a chat flow with retrieval](#build-a-chat-flow-with-retrieval)
- [Summary](#summary)
- [Original learning references](#original-learning-references)

## Grounding model responses

A model can generate fluent answers without knowing a particular organization's documents or product catalog. Ungrounded answers may be generic or incorrect.

![Ungrounded](https://learn.microsoft.com/pt-br/training/wwl-data-ai/build-copilot-ai-studio/media/ungrounded.png)

Grounding supplies relevant source information with the request so the model can use evidence that was not available in its training data.

![Grounded](https://learn.microsoft.com/pt-br/training/wwl-data-ai/build-copilot-ai-studio/media/grounded.png)

For example, a travel assistant should use the organization's actual brochures when describing hotels. Grounding improves access to evidence; it does not guarantee that every generated claim is correct.

## Retrieval-augmented generation

RAG separates retrieval from generation:

1. Retrieve passages relevant to the user's question.
2. Add the passages and source information to the prompt.
3. Generate an answer using that context.

![Rag pattern](https://learn.microsoft.com/pt-br/training/wwl-data-ai/build-copilot-ai-studio/media/rag-pattern.png)

The source may be a file collection, database, or search index. The original environment supported uploaded data and connections such as Azure Blob Storage, Azure Data Lake Storage Gen2, and Microsoft OneLake.

![Add data](https://learn.microsoft.com/pt-br/training/wwl-data-ai/build-copilot-ai-studio/media/add-data.png)

## Make the data searchable

Azure AI Search was the retrieval component in the course. An index organizes searchable fields and references to source content. Preparing an index includes deciding how to split content, which metadata to keep, and which fields need text or vector search.

![Index](https://learn.microsoft.com/pt-br/training/wwl-data-ai/build-copilot-ai-studio/media/index.png)

### Vector embeddings

An embedding represents content as a numeric vector. Semantically related passages can have similar vectors even when they use different words, such as children playing in a park and children running around a playground.

![Vector embeddings](https://learn.microsoft.com/pt-br/training/wwl-data-ai/build-copilot-ai-studio/media/vector-embeddings.jpg)

Vector search compares query and document vectors using an appropriate similarity metric. Cosine similarity is one such measure; it measures vector direction rather than literal word overlap. Use compatible embedding models and dimensions for indexed content and queries.

![Vector index](https://learn.microsoft.com/pt-br/training/wwl-data-ai/build-copilot-ai-studio/media/vector-index.png)

### Create an index

The course used a data asset and an embedding deployment to build a search index through the portal. The resulting searchable content lived in Azure AI Search and could be queried from a chat flow.

![Create index](https://learn.microsoft.com/pt-br/training/wwl-data-ai/build-copilot-ai-studio/media/create-index.png)

### Query strategies

| Strategy | Retrieval behavior |
| --- | --- |
| Keyword search | Matches terms in indexed text. |
| Vector search | Finds content with similar vector representations. |
| Hybrid search | Combines text and vector retrieval. |
| Semantic ranking | Reranks candidate results for semantic relevance. |

Select and evaluate the strategy against the actual questions and documents. Hybrid retrieval can combine exact terminology with semantic matches; it should not be assumed to win on every dataset.

## Build a chat flow with retrieval

A flow connects the user question and history to retrieval and response generation.

![Prompt flow](https://learn.microsoft.com/pt-br/training/wwl-data-ai/build-copilot-ai-studio/media/prompt-flow.png)

The retrieval step must run before the generation step so the model receives relevant evidence.

![Rag prompt flow](https://learn.microsoft.com/pt-br/training/wwl-data-ai/build-copilot-ai-studio/media/rag-prompt-flow.png)

The original multi-round question-answering sample used these steps:

![Chat flow](https://learn.microsoft.com/pt-br/training/wwl-data-ai/build-copilot-ai-studio/media/chat-flow.png)

1. **Rewrite the question using history.** Convert a follow-up such as “What can I do there?” into a query with the relevant destination included.
2. **Retrieve relevant information.** Query the index and select the useful passages.
3. **Build prompt context.** Combine retrieved passages and their source references into a suitable string.
4. **Compare prompt variants.** Test instructions for using evidence and handling insufficient information.
5. **Generate a contextual answer.** Return the model result and preserve source information where supported by the application.

Keep the rewritten query faithful to the user request. Retrieving unrelated or unauthorized content undermines the quality and access controls of the entire workflow.

## Summary

RAG adds external evidence at request time. Index preparation, query formulation, retrieval, and prompt construction all affect the answer. Evaluate retrieval quality and answer groundedness separately.

## Original learning references

- [Understand embeddings](https://learn.microsoft.com/pt-br/azure/ai-services/openai/concepts/understand-embeddings)
- [Vector search overview](https://learn.microsoft.com/pt-br/azure/search/vector-search-overview)
- [Hybrid search overview](https://learn.microsoft.com/pt-br/azure/search/hybrid-search-overview)

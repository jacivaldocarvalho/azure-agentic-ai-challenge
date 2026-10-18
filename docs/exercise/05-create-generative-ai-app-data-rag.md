# Create a generative AI application with your own data

> Study notes from the 2025 challenge. See the [documentation scope and compatibility notes](../README.md#scope-and-compatibility) before following portal instructions or SDK examples.
> Python SDK excerpts use the historical connection-string API; they are not compatible examples for an arbitrary current SDK installation.

## Contents

- [Objective and prerequisites](#objective-and-prerequisites)
- [Create the project and deploy models](#create-the-project-and-deploy-models)
- [Add the brochures](#add-the-brochures)
- [Create a search index](#create-a-search-index)
- [Compare answers with and without grounding](#compare-answers-with-and-without-grounding)
- [Prepare the external SDK lab](#prepare-the-external-sdk-lab)
- [Run the external application](#run-the-external-application)
- [Outcome and cleanup](#outcome-and-cleanup)
- [Original learning references](#original-learning-references)

## Objective and prerequisites

Use travel brochures as grounding data for a conversational assistant. The original exercise combined a hub-based Azure AI Foundry project, Azure AI Search, an embedding deployment, and a chat deployment. It assumed familiarity with Python or C# and an Azure subscription with suitable permissions and quota.

## Create the project and deploy models

Create a dedicated project and resource group with an AI resource and Azure AI Search. Choose a region and service configuration that support the required deployments.

The historical example used `text-embedding-ada-002` for embeddings and `gpt-4` for response generation, with example Standard deployments and 5K TPM limits. These names and settings are part of the 2025 walkthrough. They are not current deployment recommendations or guaranteed available capacity.

## Add the brochures

The original data came from the [Microsoft Learning brochure archive](https://github.com/MicrosoftLearning/mslearn-ai-studio/raw/main/data/brochures.zip). Download it from the upstream lab, extract the documents into a `brochures` folder, and inspect them before uploading.

In the historical portal, **Data + indexes** provided a data-asset upload experience. Add only data intended for the lab and verify which project identities can access it.

## Create a search index

The example created `brochures-index` from the uploaded data with vector search enabled and a matching embedding deployment. Index preparation turns the source content into searchable passages and metadata. Wait for indexing to complete and inspect results before using them in a chat application.

The index and embedding configuration must agree on vector dimensions and the embedding representation. Index creation, storage, and queries can incur charges.

## Compare answers with and without grounding

In the chat playground, ask “Where can I stay in New York?” before attaching the index. Then connect the indexed data and repeat the question. Compare the answer against the brochures rather than assuming a changed response is automatically more accurate.

Look for supported details, source references, and an appropriate response when the documents do not contain an answer. Grounding supplies evidence but does not guarantee correctness.

## Prepare the external SDK lab

The complete RAG application is maintained upstream, not in this repository:

```bash
git clone https://github.com/MicrosoftLearning/mslearn-ai-studio mslearn-ai-foundry
```

Find the matching own-data exercise in the [upstream exercise index](https://microsoftlearning.github.io/mslearn-ai-studio/). In its Python or C# project directory, use the dependencies and configuration expected by that revision. Do not apply this repository's history-assistant `requirements.txt` to an unrelated RAG application.

The historical Python package list included `python-dotenv`, `azure-ai-projects`, `azure-identity`, and `openai`. The C# lab used `Azure.Identity`, `Azure.AI.Projects`, and `Azure.AI.OpenAI`, including preview packages. A current unpinned installation is not a substitute for the versions used by that lab.

Configure the external lab's `.env` or `appsettings.json` with its project access, model deployment, and search settings. Historical connection strings differ from the endpoint-based API described by current SDK documentation.

## Run the external application

After completing the upstream lab's code and configuration, run its Python application from that lab directory:

```bash
python rag-app.py
```

For C#, use `dotnet run`. Test “Where should I stay in London?” and then “What can I do there?” Verify that retrieval, conversational context, and generated answers remain tied to the brochures.

`rag-app.py`, the .NET project, and the brochure data are not included in this repository. These instructions describe the external learning workflow, not an integration validated by the local test suite.

## Outcome and cleanup

The exercise demonstrates a retrieval-and-generation workflow: prepare data, retrieve relevant passages, and use them as model context. Remove lab-only indexes, deployments, compute, and other resources when finished. Confirm the contents before deleting an entire resource group.

## Original learning references

- [Ai.azure.com](https://ai.azure.com)
- [Portal.azure.com](https://portal.azure.com)
- [04 use own data](https://microsoftlearning.github.io/mslearn-ai-studio/Instructions/04-Use-own-data.html)

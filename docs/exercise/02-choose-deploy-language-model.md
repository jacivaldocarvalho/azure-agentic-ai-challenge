# Choose and deploy a language model

> Study notes from the 2025 challenge. See the [documentation scope and compatibility notes](../README.md#scope-and-compatibility) before following portal instructions or SDK examples.

## Contents

- [Objective](#objective)
- [Prepare the project](#prepare-the-project)
- [Explore inference and the catalog](#explore-inference-and-the-catalog)
- [Deploy the candidates](#deploy-the-candidates)
- [Compare answers in the playground](#compare-answers-in-the-playground)
- [Additional challenge](#additional-challenge)
- [Cleanup and outcome](#cleanup-and-outcome)
- [Original learning references](#original-learning-references)

## Objective

Compare models for a problem-solving assistant, deploy suitable candidates, and evaluate them in the chat playground. The original candidates were GPT-4o and Phi-3.5-mini-instruct. They are historical examples, not a statement about current availability or the best model for a new application.

## Prepare the project

In the 2025 portal, create a project and a new hub with an appropriate subscription, resource group, region, and AI resource. The original example did not require Azure AI Search. Verify model availability and quota before provisioning.

Example resource names for a new lab are `my-ai-project`, `my-ai-hub`, and `my-ai-resources`; they are placeholders rather than existing resources.

## Explore inference and the catalog

The original lab enabled a preview option called **Deploy models to Azure AI model inference service**. This describes the old portal and should not be assumed to exist in another version.

Open **Model catalog**, inspect each candidate's model card, and compare supported tasks, licensing, deployment options, benchmarks, and price. Use **Compare models** where the interface provides it.

Review quality, accuracy, coherence, fluency, and relevance, but also measure latency and cost for your own workload.

## Deploy the candidates

The original workflow offered deployment through the catalog or **Models + endpoints**. It used names such as `gpt-4o` and `phi-3.5-mini-instruct`, Global Standard where supported, an automatic version update policy, and the DefaultV2 filter.

The historical example requested 50K tokens per minute for GPT-4o. That is an example quota allocation, not a requirement or an entitlement. Use settings supported by the model and subscription, and understand version-update behavior before choosing it.

## Compare answers in the playground

Configure a problem-solving assistant with this illustrative system instruction:

```text
You are an AI assistant that helps solve problems.
```

Try the same questions with each deployment and record the full configuration. First test a river-crossing problem:

```text
I have a fox, a chicken, and a bag of grain that I need to take over a river in a boat. I can only take one thing at a time. If I leave the chicken and the grain unattended, the chicken will eat the grain. If I leave the fox and the chicken unattended, the fox will eat the chicken. How can I get all three things across the river without anything being eaten?
```

Ask for a concise explanation and verify that every crossing respects the constraints. A convincing explanation can still contain an invalid step.

## Additional challenge

```text
I have 53 socks in my drawer: 21 identical blue, 15 identical black, and 17 identical red. The lights are out, and it is completely dark. How many socks must I take out to make 100 percent certain I have at least one pair of black socks?
```

The answer is **40 socks**: the worst case is drawing all 38 non-black socks before two black socks. Compare correctness as well as response length and cost.

## Cleanup and outcome

The exercise demonstrates selection, deployment, and comparison rather than a production model recommendation. Remove deployments and resources created only for the lab when finished. Inspect a resource group before deleting it so shared resources are preserved.

## Original learning references

- [Ai.azure.com](https://ai.azure.com)
- [02 explore model catalog](https://microsoftlearning.github.io/mslearn-ai-studio/Instructions/02-Explore-model-catalog.html)

# Manage a chat conversation with prompt flow

> Study notes from the 2025 challenge. See the [documentation scope and compatibility notes](../README.md#scope-and-compatibility) before following portal instructions or SDK examples.

## Contents

- [Objective](#objective)
- [Create the project and model deployment](#create-the-project-and-model-deployment)
- [Configure the travel assistant](#configure-the-travel-assistant)
- [Create a chat flow](#create-a-chat-flow)
- [Deploy the flow](#deploy-the-flow)
- [Outcome and cleanup](#outcome-and-cleanup)
- [Original learning references](#original-learning-references)

## Objective

Build a travel-assistant chat flow around an Azure OpenAI deployment. The exercise covers project setup, assistant instructions, flow configuration, testing, and endpoint deployment in the 2025 hub-based portal experience.

## Create the project and model deployment

Create a lab project and hub with an appropriate subscription, dedicated resource group, region, and AI resource. The original exercise did not use Azure AI Search. It selected GPT-4 through **Models + endpoints**, with a Standard deployment and a 5K TPM example limit.

Model names, available versions, filter labels, quota, and portal navigation must be verified for the environment you use. Keep deployment names consistent between the playground and flow connection.

## Configure the travel assistant

In the playground, define the intended travel-assistant behavior. This illustrative prompt expresses a role and expected behavior; it does not give the model live travel data or booking capabilities:

```text
Objective: Help users plan travel and understand destination options.
Capabilities: Explain itinerary options, transportation, accommodation,
packing considerations, and common travel disruptions.
Instructions:
- Ask about preferences, budget, and travel dates when relevant.
- Use available evidence and distinguish general guidance from verified facts.
- Do not claim access to current prices, schedules, or bookings without a tool.
- Offer practical next steps and invite follow-up questions.
```

Try “What can you do?” and inspect whether the response matches the capabilities actually configured. This prompt is a documentation example, not a change to the repository's history-assistant prompt.

## Create a chat flow

The original playground offered a **Prompt flow** action to create a flow folder such as `Travel-Chat`. Its basic structure included a question and chat-history input, an LLM node, and a response output.

Start the compute session and configure the LLM node with the intended connection, chat API, deployment name, and text response format. Confirm that the prompt includes the travel-assistant instructions and that the chat-history input is connected correctly.

Save the flow and test: “I have one day in London, what should I do?” Follow with a question that relies on the previous destination and inspect the resulting context.

## Deploy the flow

The historical exercise deployed an online endpoint and configured a deployment name, VM size, instance count, and inference data collection. Its example used `Standard_DS3_v2` and three instances; those were lab settings rather than a minimum requirement for a travel assistant.

Choose capacity and data collection deliberately for the lab. Review what request and response data will be retained before enabling collection. Deployment creates billable infrastructure; this repository contains no endpoint or deployment template.

Test the endpoint with questions such as “What is there to do in San Francisco?” and “Where else could I go?” The **Consume** experience in the original portal provided client connection information.

## Outcome and cleanup

The flow connects conversational inputs to a model and exposes the result through an endpoint. It does not implement a travel booking system. Stop compute and remove endpoint deployments and other dedicated lab resources after use. Inspect the resource group before deleting shared infrastructure or data.

## Original learning references

- [Ai.azure.com](https://ai.azure.com)
- [Portal.azure.com](https://portal.azure.com)
- [03 use prompt flow chat](https://microsoftlearning.github.io/mslearn-ai-studio/Instructions/03-Use-prompt-flow-chat.html)

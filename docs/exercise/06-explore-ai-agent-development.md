# Explore AI agent development in Azure AI Foundry

> Study notes from the 2025 challenge. See the [documentation scope and compatibility notes](../README.md#scope-and-compatibility) before following portal instructions or SDK examples.

## Contents

- [Objective and prerequisites](#objective-and-prerequisites)
- [Create a lab project](#create-a-lab-project)
- [Deploy a model](#deploy-a-model)
- [Configure the expenses agent](#configure-the-expenses-agent)
- [Test against the document](#test-against-the-document)
- [Cleanup and outcome](#cleanup-and-outcome)
- [Original learning references](#original-learning-references)

## Objective and prerequisites

Create an expenses-policy assistant using the portal's agent experience and file-based knowledge. You need an Azure subscription, access to the portal, permissions for the project, and the expense-policy document used by the external lab.

## Create a lab project

The 2025 walkthrough created a hub-based project with a dedicated resource group and AI resource. It listed example regions including `eastus`, `eastus2`, `swedencentral`, `westus`, and `westus3`. Those are historical choices; verify current model and tool availability for the subscription before provisioning.

The original portal flow did not require an Azure AI Search connection for this file-search exercise.

## Deploy a model

The course selected GPT-4o from **Models + endpoints** and used an example Global Standard deployment, automatic version updates, a 50K TPM allocation where available, and the DefaultV2 content filter. These are recorded lab settings, not fixed requirements or guaranteed capacity.

Keep the deployment name consistent with the model selected by the agent.

## Configure the expenses agent

Obtain [Expenses_Policy.docx](https://raw.githubusercontent.com/MicrosoftLearning/mslearn-ai-agents/main/Labfiles/01-agent-fundamentals/Expenses_Policy.docx) from the original lab or locate its replacement through the [upstream exercise index](https://microsoftlearning.github.io/mslearn-ai-agents/). Asset paths on an upstream branch can change.

In the historical agent configuration experience:

1. Create an agent named `ExpensesAgent`.
2. Select the deployed model.
3. Provide task instructions, such as “Answer questions about expense reimbursements using the supplied policy.”
4. Add file knowledge and create a vector store, such as `Expenses_Vector_Store`.
5. Upload the policy document and wait for processing to complete.

This is an illustrative English instruction for the external lab, not a modification to any agent deployed by this repository.

## Test against the document

Open the agent playground and ask:

- “What is the maximum amount I can claim for meals?”
- “What about accommodation?”

Check the answers against the policy and verify that the second question uses the prior context. Test a question whose answer is absent from the document and inspect whether the agent acknowledges the limitation.

The repository does not contain a configured agent, policy document, or vector store. Its offline Python tests do not validate this portal exercise.

## Cleanup and outcome

Remove temporary agent data, uploaded files, vector stores, and deployments where applicable. Delete a resource group only after confirming it is dedicated to the lab. This exercise illustrates model instructions and file grounding; it does not implement expense submission.

## Original learning references

- [Ai.azure.com](https://ai.azure.com)
- [Portal.azure.com](https://portal.azure.com)

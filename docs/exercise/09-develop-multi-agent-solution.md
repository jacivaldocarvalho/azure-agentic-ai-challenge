# Explore a multi-agent solution with Semantic Kernel

> Study notes from the 2025 challenge. See the [documentation scope and compatibility notes](../README.md#scope-and-compatibility) before following portal instructions or SDK examples.
> Python SDK excerpts use the historical connection-string API; they are not compatible examples for an arbitrary current SDK installation.
> `AgentGroupChat` examples document an archived experimental API; see the [orchestration compatibility notes](../README.md#semantic-kernel-orchestration).

## Contents

- [Objective and scope](#objective-and-scope)
- [Prepare Azure resources and the external workspace](#prepare-azure-resources-and-the-external-workspace)
- [Create and wrap the agent definitions](#create-and-wrap-the-agent-definitions)
- [Define historical selection and termination strategies](#define-historical-selection-and-termination-strategies)
- [Configure the group chat](#configure-the-group-chat)
- [Inspect results and limitations](#inspect-results-and-limitations)
- [Cleanup](#cleanup)
- [Original learning references](#original-learning-references)

## Objective and scope

Study an incident-management conversation with an `IncidentManager` and a `DevOpsAssistant`. The first participant reviews logs and recommends next steps; the second discusses the proposed response. The original guide estimated about 30 minutes for the external lab.

This repository does not include log ingestion, remediation tools, service-restart permissions, or an executable multi-agent application. A conversation about a restart does not restart a service. The following fragments explain the historical architecture without claiming those integrations exist.

## Prepare Azure resources and the external workspace

The 2025 course used a project and model deployment in Azure AI Foundry. Its GPT-4o, Global Standard, DefaultV2, and 60K TPM settings were lab examples; confirm actual service support and capacity before provisioning.

Clone into the explicitly named directory so subsequent paths agree with the checkout name:

```bash
git clone https://github.com/MicrosoftLearning/mslearn-ai-agents ai-agents
```

The original lab path was `ai-agents/Labfiles/05-agent-orchestration/Python`. It is historical and may not exist on the upstream default branch. Use the upstream exercise index or a matching revision rather than assuming the path and package versions are current.

From the selected Linux or Cloud Shell Bash lab directory, create an isolated environment:

```bash
python3 -m venv labenv
source labenv/bin/activate
```

The original dependency set included `python-dotenv`, `azure-identity`, and `semantic-kernel[azure]`. A current install is not guaranteed to expose the archived `AgentGroupChat` API. Use the external lab revision's dependency and project-configuration instructions.

## Create and wrap the agent definitions

These historical fragments belong inside an async function after configuring the asynchronous project client, credential, and deployment. `client`, `credential`, and the actual service deployment are supplied by that external application.

```python
from semantic_kernel.agents import AzureAIAgent

incident_definition = await client.agents.create_agent(
    model="gpt-4o",
    name="IncidentManager",
    instructions=(
        "Analyze the supplied logs and recommend next steps. "
        "Do not claim to execute actions. When the review is complete, "
        "respond with exactly: no action needed"
    ),
)
devops_definition = await client.agents.create_agent(
    model="gpt-4o",
    name="DevOpsAssistant",
    instructions="Discuss the proposed remediation. Do not claim a service was changed without a tool result.",
)
incident_agent = AzureAIAgent(client=client, definition=incident_definition)
devops_agent = AzureAIAgent(client=client, definition=devops_definition)
```

The original guide passed raw service definitions directly to the group chat. The historical Semantic Kernel integration uses agent wrappers. These illustrative definitions provide no service-remediation tools.

## Define historical selection and termination strategies

The archived API expects subclasses of its strategy interfaces. These fragments document that pattern and include an empty-history check:

```python
from semantic_kernel.agents.strategies import SelectionStrategy, TerminationStrategy
from semantic_kernel.contents import AuthorRole


class IncidentSelectionStrategy(SelectionStrategy):
    async def select_agent(self, agents, history):
        if not history or history[-1].role == AuthorRole.USER or history[-1].name == "DevOpsAssistant":
            return next(agent for agent in agents if agent.name == "IncidentManager")
        return next(agent for agent in agents if agent.name == "DevOpsAssistant")


class ApprovalTerminationStrategy(TerminationStrategy):
    async def should_agent_terminate(self, agent, history):
        return bool(
            history
            and history[-1].name == "IncidentManager"
            and (history[-1].content or "").strip().lower() == "no action needed"
        )
```

The exact completion phrase is a conversation convention, not evidence that an incident has been resolved or approval to perform an external action. A maximum iteration count is also needed to bound the interaction.

## Configure the group chat

Historical excerpt, inside the same async context with both wrapped agents:

```python
from semantic_kernel.agents import AgentGroupChat
from semantic_kernel.contents import ChatMessageContent, AuthorRole

chat = AgentGroupChat(
    agents=[incident_agent, devops_agent],
    selection_strategy=IncidentSelectionStrategy(),
    termination_strategy=ApprovalTerminationStrategy(
        agents=[incident_agent],
        maximum_iterations=6,
    ),
)
await chat.add_chat_message(
    message=ChatMessageContent(
        role=AuthorRole.USER,
        content="Review this sample log: ServiceX reported a connection timeout.",
    )
)
async for message in chat.invoke():
    print(f"{message.name}: {message.content}")
```

The surrounding application must manage authentication, resource cleanup, errors, and the async entry point. These excerpts are not a standalone `agent_chat.py` and were not run against Azure.

## Inspect results and limitations

Illustrative discussion, not output captured from a tested integration:

```text
IncidentManager: ServiceX reported a connection timeout. Inspect connectivity and recent changes.
DevOpsAssistant: No service change has been executed. Review the proposed diagnostics first.
IncidentManager: no action needed
```

The final phrase ends this demonstration's discussion. It does not verify service health. Real remediation would require explicit tools, validated inputs, execution permissions, and independent checks of the result.

For a complete external lab, authenticate with `az login` and follow that lab's application entry point. Consult the migration guide before implementing against newer Semantic Kernel orchestration APIs.

## Cleanup

Delete temporary agent definitions and other artifacts created by the external application. Remove dedicated cloud resources after reviewing what the resource group contains. The snippets do not clean up resources automatically.

## Original learning references

- [Ai.azure.com](https://ai.azure.com)
- [05 agent orchestration](https://microsoftlearning.github.io/mslearn-ai-agents/Instructions/05-agent-orchestration.html)

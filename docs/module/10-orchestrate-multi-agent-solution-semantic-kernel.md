# Orchestrate multiple agents with Semantic Kernel

> Study notes from the 2025 challenge. See the [documentation scope and compatibility notes](../README.md#scope-and-compatibility) before following portal instructions or SDK examples.
> `AgentGroupChat` examples document an archived experimental API; see the [orchestration compatibility notes](../README.md#semantic-kernel-orchestration).

## Contents

- [Multi-agent collaboration](#multi-agent-collaboration)
- [Framework concepts](#framework-concepts)
- [Create a historical group chat](#create-a-historical-group-chat)
- [Add messages and invoke agents](#add-messages-and-invoke-agents)
- [Select the next agent](#select-the-next-agent)
- [Terminate the conversation](#terminate-the-conversation)
- [History reduction and conversation state](#history-reduction-and-conversation-state)
- [Summary](#summary)

## Multi-agent collaboration

The course used Semantic Kernel to explore collaboration among agents with different responsibilities. A conceptual DevOps workflow could include monitoring, root-cause analysis, deployment, and reporting agents. That architecture is an example for discussion; this repository does not implement automated operations or deploy agents.

Specialization can clarify responsibilities, but it also introduces coordination, state, cost, and termination concerns. A single agent or deterministic workflow may be sufficient for a simpler task.

## Framework concepts

| Concept | Role in the original material |
| --- | --- |
| Agent | A model-driven participant with instructions and capabilities. |
| Kernel | Application services, model access, and function invocation. |
| Tools and plugins | Capabilities exposed to the agent. |
| History | Messages used as context for subsequent turns. |
| Group chat | Shared collaboration controlled by selection and termination strategies. |

The course discussed `AzureAIAgent`, `ChatCompletionAgent`, and `OpenAIAssistantAgent`. These names record the framework at the time; they are not a guarantee that every class or provider API remains supported in a current installation.

## Create a historical group chat

All Python excerpts below are illustrative fragments for the archived API. They require a matching historical SDK and previously configured agent objects. They are not standalone scripts or tested integrations.

```python
from semantic_kernel.agents import AgentGroupChat

# agent_writer and agent_reviewer must be configured agent instances.
chat = AgentGroupChat(agents=[agent_writer, agent_reviewer])
```

An alternative is to add configured agents after creating the chat:

```python
chat = AgentGroupChat()
chat.add_agent(agent=agent_writer)
chat.add_agent(agent=agent_reviewer)
```

## Add messages and invoke agents

This excerpt belongs inside an async function with the configured `chat` object:

```python
from semantic_kernel.contents import AuthorRole, ChatMessageContent

chat_message = ChatMessageContent(
    role=AuthorRole.USER,
    content="Write a short slogan for a cleaning brush.",
)
await chat.add_chat_message(message=chat_message)
```

A single-turn invocation specifies the participant. A multi-turn invocation uses the chat's configured strategies. These excerpts correct the missing colons and empty loop bodies in the original notes:

```python
# Inside an async function; agent_writer must already be configured.
async for message in chat.invoke(agent_writer):
    print(message.content)
```

```python
# Inside an async function, after configuring selection and termination.
async for message in chat.invoke():
    print(message.content)
```

## Select the next agent

In the writer-reviewer example, `CopywriterAgent` drafts content and `ReviewingDirectorAgent` reviews it. A selection strategy determines the next participant; it does not automatically understand every task correctly.

The original API provided sequential selection, kernel-function selection, and custom strategies based on `SelectionStrategy`. A custom strategy must implement the expected interface and return an agent in the chat.

Example selection prompt, shown as text rather than a complete strategy implementation:

```text
Choose the next participant. Return only its name.
Participants: CopywriterAgent, ReviewingDirectorAgent.
After user input, choose CopywriterAgent.
After CopywriterAgent, choose ReviewingDirectorAgent.
After review feedback, choose CopywriterAgent.
Do not select the same participant for consecutive turns.
History: {{$history}}
```

When the order is fixed, deterministic selection avoids an unnecessary model call. When using a model-based selector, validate its output against the allowed participants.

## Terminate the conversation

A termination strategy decides when the task is complete. The course compared `DefaultTerminationStrategy`, `KernelFunctionTerminationStrategy`, and custom `TerminationStrategy` implementations.

A reviewer approval signal can end the writer-reviewer loop, but every conversation also needs a finite iteration limit. Do not treat an arbitrary substring in untrusted text as approval for an external action.

Illustrative termination prompt:

```text
Determine whether the reviewer approved the latest copy.
Return exactly yes or no.
History: {{$history}}
```

A result parser converts the model output into a boolean. Configure which participant can signal completion and distinguish a completed task from one stopped by an iteration limit.

## History reduction and conversation state

The course used a history reducer when a strategy needed only the latest message:

```python
from semantic_kernel.contents import ChatHistoryTruncationReducer

history_reducer = ChatHistoryTruncationReducer(target_count=1)
```

Reducing context can lower token use, but it can also remove information required for a correct decision. Choose the retained context based on the strategy, not solely on cost.

In the archived group-chat API, completion state affected whether a chat instance could continue. A completed chat could require resetting its completion state; reaching an iteration limit was a separate condition. Confirm behavior against the exact framework version before reusing an instance.

## Summary

Multi-agent orchestration requires explicit selection, shared context, and termination. These notes preserve the archived `AgentGroupChat` learning pattern; use the migration reference when designing against a newer orchestration API.

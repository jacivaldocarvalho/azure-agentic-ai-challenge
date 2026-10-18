# Integrate custom tools into an agent

> Study notes from the 2025 challenge. See the [documentation scope and compatibility notes](../README.md#scope-and-compatibility) before following portal instructions or SDK examples.
> Python SDK excerpts use the historical connection-string API; they are not compatible examples for an arbitrary current SDK installation.

## Contents

- [Why custom tools?](#why-custom-tools)
- [Integration options](#integration-options)
- [Define a function](#define-a-function)
- [Register the function tool](#register-the-function-tool)
- [Connect an Azure Function](#connect-an-azure-function)
- [Describe an OpenAPI operation](#describe-an-openapi-operation)
- [Register the OpenAPI tool](#register-the-openapi-tool)
- [Summary](#summary)

## Why custom tools?

Built-in knowledge and code tools cannot implement every business operation. A custom tool can retrieve order details, prepare support tickets, look up specialist data, or connect a model to an existing API.

Use cases in the course included retail support, personalized marketing, business analysis, and sector-specific workflows. The model selects a declared operation; the application or connected service performs the actual work.

![Agent tool diagram](https://learn.microsoft.com/pt-br/training/wwl-data-ai/build-agent-with-custom-tools/media/agent-tool-diagram.png)

## Integration options

| Option | Suitable learning scenario |
| --- | --- |
| Function calling | Expose application code through a typed function description. |
| Azure Functions | Connect a deployed function through a supported integration. |
| OpenAPI | Describe HTTP operations and their parameters in a standard document. |

The following excerpts retain the historical `azure.ai.projects.models` API. They illustrate separate parts of an integration, not a complete program. They assume a configured `project_client`, a deployment, and the SDK version documented in the compatibility notes. No weather service is deployed here.

## Define a function

This function returns mock data, not live snowfall measurements. Its imports are included so the function definition is self-contained.

```python
import json
from typing import Any, Callable, Set

def recent_snowfall(location: str) -> str:
    """
    Fetches recent snowfall totals for a given location.
    :param location: The city name.
    :return: Snowfall details as a JSON string.
    """
    mock_snow_data = {"Seattle": "0 inches", "Denver": "2 inches"}
    snow = mock_snow_data.get(location, "Data not available.")
    return json.dumps({"location": location, "snowfall": snow})

user_functions: Set[Callable[..., Any]] = {
    recent_snowfall,
}

```

The function's name, parameter types, and docstring describe its purpose to the SDK. Validate inputs and downstream permissions in a real integration.

## Register the function tool

Historical excerpt using `user_functions` from the preceding section and a configured `project_client`:

```python
from azure.ai.projects.models import FunctionTool, ToolSet

# Initialize agent toolset with user functions
functions = FunctionTool(user_functions)
toolset = ToolSet()
toolset.add(functions)
project_client.agents.enable_auto_function_calls(toolset=toolset)

# Create your agent with the toolset
agent = project_client.agents.create_agent(
    model="gpt-4o-mini",
    name="snowfall-agent",
    instructions="You are a weather assistant tracking snowfall. Use the provided functions to answer questions.",
    toolset=toolset
)

```

Passing the constructed `ToolSet` fixes the original example's inconsistent dictionary argument. Automatic local execution must be explicitly supported and enabled by the SDK; otherwise the application must handle requested calls and submit their outputs. The excerpt does not implement the conversation loop.

## Connect an Azure Function

Deploy and configure the function and storage queues before using this excerpt. The historical integration used input and output queues; the placeholder storage endpoint is not a working resource.

```python
import os
from azure.ai.projects.models import AzureFunctionTool, AzureFunctionStorageQueue

storage_service_endpoint = "https://<your-storage>.queue.core.windows.net"

azure_function_tool = AzureFunctionTool(
    name="get_snowfall",
    description="Get snowfall information using Azure Function",
    parameters={
            "type": "object",
            "properties": {
                "location": {"type": "string", "description": "The location to check snowfall."},
            },
            "required": ["location"],
        },
    input_queue=AzureFunctionStorageQueue(
        queue_name="input",
        storage_service_endpoint=storage_service_endpoint,
    ),
    output_queue=AzureFunctionStorageQueue(
        queue_name="output",
        storage_service_endpoint=storage_service_endpoint,
    ),
)

agent = project_client.agents.create_agent(
    model=os.environ["MODEL_DEPLOYMENT_NAME"],
    name="azure-function-agent",
    instructions="You are a snowfall tracking agent. Use the provided Azure Function to fetch snowfall based on location.",
    tools=azure_function_tool.definitions,
)

```

The example assumes a matching function implementation, queue configuration, and authorization. An HTTP-triggered function is not interchangeable with this queue-based tool definition.

## Describe an OpenAPI operation

Save the following illustrative document as `snowfall_openapi.json` in an external lab workspace. Replace the reserved example server URL with a real service. The document describes a simple snowfall response and does not implement an API.

```json
{
  "openapi": "3.0.0",
  "info": {
    "title": "Snowfall API",
    "version": "1.0.0"
  },
  "servers": [{"url": "https://your-snowfall-api.example"}],
  "paths": {
    "/snow": {
      "get": {
        "operationId": "getSnowfall",
        "summary": "Get snowfall information",
        "parameters": [
          {
            "name": "location",
            "in": "query",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful response",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "location": {"type": "string"},
                    "snow": {"type": "string"}
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}

```

## Register the OpenAPI tool

Historical excerpt; anonymous authentication is shown only for an API that intentionally permits it. Use the authentication supported by the actual service.

```python
import json

from azure.ai.projects.models import OpenApiTool, OpenApiAnonymousAuthDetails

with open("snowfall_openapi.json", "r") as f:
    openapi_spec = json.load(f)

auth = OpenApiAnonymousAuthDetails()
openapi_tool = OpenApiTool(
    name="snowfall_api", spec=openapi_spec, auth=auth,
    description="Retrieve snowfall information for a location",
)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini",
    name="openapi-agent",
    instructions="You are a snowfall tracking assistant. Use the API to fetch snowfall data.",
    tools=openapi_tool.definitions
)

```

The original registration passed a tool object directly; this excerpt uses its generated definitions for the historical agent API. It still requires an existing project client and model deployment.

## Summary

Custom tools connect model requests to application capabilities. Clear declarations help tool selection, while execution, error handling, permissions, and state changes remain responsibilities of the surrounding application.

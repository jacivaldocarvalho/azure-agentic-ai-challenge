# Azure Agentic AI Challenge

Learning notes and exercises from Jacivaldo Carvalho's participation in the Microsoft AI Skills Challenge 2025. Topics include Azure AI Foundry, generative AI, retrieval-augmented generation (RAG), AI agents, and Semantic Kernel.

This repository contains study guides and one standalone Python example that sends a history question to Azure OpenAI. The applications described in the guides are learning exercises, rather than complete applications implemented here.

## Repository contents

- [Module notes](docs/module/): concepts and summaries from the challenge.
- [Exercise guides](docs/exercise/): walkthroughs, code excerpts, and screenshots.
- [Python example](exercises/01-history-assistant.py): an interactive history assistant using Azure OpenAI.

The guides and screenshots reflect the 2025 learning material. Most guides and the example's prompts are currently in Portuguese. Portal instructions and SDK excerpts have not been verified against current Azure services.

## Module notes

| Module | Notes |
| --- | --- |
| 01 | [Plan and prepare Azure AI solutions](docs/module/01-planning-azure-ai-solutions.md.md) |
| 02 | [Explore and deploy models in Azure AI Foundry](docs/module/02-explore-and-deploy-models-azure-ai-foundry.md) |
| 03 | [Develop an AI application with Azure AI Foundry](docs/module/03-develop-ai-app-azure-ai-foundry.md) |
| 04 | [Introduction to prompt flow](docs/module/04-intro-prompt-flow-develop-language-model-app-azure-ai-studio.md) |
| 05 | [Build a RAG solution with your own data](docs/module/05-build-rag-data-azure-ai-studio.md) |
| 06 | [AI agent fundamentals](docs/module/06-basic-ai-agents-azure.md) |
| 07 | [AI Agent Service security controls](docs/module/07-intro-ai-agent-service-security-controls.md) |
| 08 | [Develop an agent with Azure AI Agent Service](docs/module/08-develop-ai-agent-azure-service.md) |
| 09 | [Integrate custom tools into an agent](docs/module/09-integrate-custom-tools-into-agent.md) |
| 10 | [Orchestrate multiple agents with Semantic Kernel](docs/module/10-orchestrate-multi-agente-solution-semantic-kernel.md) |

## Run the Python example

### Prerequisites

- Python 3 and the `venv` module. Dependency installation, imports, and offline client initialization were validated with Python 3.12.3.
- An Azure subscription, an Azure OpenAI resource, and its endpoint and API key.
- An existing model deployment named `gpt-4o`, compatible with the API version `2024-12-01-preview` and the request parameters used by the script.

The deployment name and API version are hardcoded in the existing script. No environment variables override them. Their availability in your Azure resource must be checked before running the example. Azure API calls may incur charges.

### Install dependencies

Run these commands from the repository root.

Linux or macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
```

Windows PowerShell:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
```

The runtime dependencies are `openai` and `python-dotenv`. A clean installation, imports, offline Azure client initialization, and dependency consistency checks passed with `openai==3.35.1` and `python-dotenv==1.2.4` on Python 3.12.3. Versions are not locked, so future installations may resolve different releases. Live Azure requests and the Windows setup commands have not been validated.

### Configure credentials

Edit the local `.env` file and replace both placeholders:

| Variable | Value |
| --- | --- |
| `AZURE_OPENAI_ENDPOINT` | Endpoint of your Azure OpenAI resource, such as `https://your-resource-name.openai.azure.com/`. |
| `AZURE_OPENAI_API_KEY` | API key for that resource. |

The script loads `.env` using `python-dotenv`. Keep credentials local: `.env` and its variants are ignored by Git, while `.env.example` contains placeholders only.

### Execute

With the virtual environment active, run:

```bash
python exercises/01-history-assistant.py
```

Enter a history question when prompted. The script sends one request and prints the answer. Its terminal messages and system prompt are currently in Portuguese.

### Troubleshooting

- **Missing module:** activate the virtual environment and install `requirements.txt` with that environment's Python interpreter.
- **Missing credentials or authentication failure:** check both variables and replace the placeholders. Also check existing shell environment variables.
- **Deployment or API error:** verify the resource endpoint, the deployment named `gpt-4o`, and support for the script's hardcoded API version and parameters.
- **Quota or connection error:** check Azure quota and network access. The script currently reports failures through SDK exceptions rather than application-specific messages.

The repository currently has no automated test suite or CI workflow. Running the example is a live integration operation that requires credentials and may incur charges.

## Resource cleanup

The local example does not provision Azure infrastructure. If you create resources while following an exercise, remove resources dedicated to that exercise when finished to avoid ongoing charges. Check for shared resources before deleting anything.

## Author

**Jacivaldo Carvalho**

Telecommunications Engineer | DevOps Engineer | SRE | Networking

[GitHub](https://github.com/jacivaldocarvalho) | [LinkedIn](https://www.linkedin.com/in/jacivaldocarvalho) | [Website](https://www.jacivaldocarvalho.com/)

## License

[MIT](LICENSE), copyright 2025 Jacivaldo Carvalho.

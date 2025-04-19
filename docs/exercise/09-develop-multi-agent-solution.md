# Desenvolvendo uma Solução Multiagente com Azure AI

## Índice
- [Desenvolvendo uma Solução Multiagente com Azure AI](#desenvolvendo-uma-solução-multiagente-com-azure-ai)
  - [Índice](#índice)
  - [Introdução](#introdução)
  - [Criar um Projeto no Azure AI Foundry](#criar-um-projeto-no-azure-ai-foundry)
  - [Implantar um Modelo de IA Generativa](#implantar-um-modelo-de-ia-generativa)
  - [Preparar o Ambiente de Desenvolvimento](#preparar-o-ambiente-de-desenvolvimento)
  - [Criar os Agentes de IA](#criar-os-agentes-de-ia)
    - [Agente Gerenciador de Incidentes](#agente-gerenciador-de-incidentes)
    - [Assistente DevOps](#assistente-devops)
  - [Implementar a Lógica de Chat em Grupo](#implementar-a-lógica-de-chat-em-grupo)
    - [Estratégia de Seleção](#estratégia-de-seleção)
    - [Estratégia de Término](#estratégia-de-término)
    - [Configurar o Chat em Grupo](#configurar-o-chat-em-grupo)
  - [Executar a Solução Multiagente](#executar-a-solução-multiagente)
  - [Limpeza de Recursos](#limpeza-de-recursos)
  - [Conclusão](#conclusão)
  - [Referência](#referência)


## Introdução
Neste artigo, você aprenderá a criar uma solução com múltiplos agentes de IA que trabalham em conjunto usando o Semantic Kernel SDK. Desenvolveremos:

1. **Agente Gerenciador de Incidentes**: Analisa arquivos de log e identifica problemas
2. **Assistente DevOps**: Executa ações corretivas recomendadas

A solução completa será capaz de:
- Analisar automaticamente logs de serviço
- Recomendar ações corretivas
- Executar as correções necessárias
- Verificar se as resoluções foram bem-sucedidas

**Tempo estimado**: 30 minutos


## Criar um Projeto no Azure AI Foundry
1. Acesse o [portal Azure AI Foundry](https://ai.azure.com)
2. Selecione **+ Create project**
3. Configure o projeto com:
   - Nome personalizado
   - Região suportada (eastus, eastus2, etc.)
   - Novo recurso de Azure AI Services
4. Revise e confirme a criação


## Implantar um Modelo de IA Generativa
1. No painel esquerdo, acesse **Models + endpoints**
2. Selecione **Deploy base model** e escolha `gpt-4o`
3. Configure com:
   - Nome personalizado
   - Tipo: Global Standard
   - Limite de tokens: 60K/min
   - Filtro de conteúdo: DefaultV2
4. Aguarde a conclusão da implantação


## Preparar o Ambiente de Desenvolvimento
No Azure Cloud Shell (PowerShell):

```powershell
git clone https://github.com/MicrosoftLearning/mslearn-ai-agents
cd ai-agents/Labfiles/05-agent-orchestration/Python
python -m venv labenv
./labenv/bin/Activate.ps1
pip install python-dotenv azure-identity semantic-kernel[azure]
```

Edite o arquivo `.env` com suas credenciais:
- Connection string do projeto
- Nome da implantação do modelo


## Criar os Agentes de IA
### Agente Gerenciador de Incidentes
```python
incident_agent = await client.agents.create_agent(
    model="gpt-4o",
    name="IncidentManager",
    instructions="Analise logs, identifique problemas e recomende ações..."
)
```

### Assistente DevOps
```python
devops_agent = await client.agents.create_agent(
    model="gpt-4o",
    name="DevOpsAssistant",
    instructions="Execute ações corretivas em serviços..."
)
```


## Implementar a Lógica de Chat em Grupo
### Estratégia de Seleção
Define qual agente deve responder:

```python
class SelectionStrategy:
    async def select_agent(self, agents, history):
        if history[-1].name == "DevOpsAssistant" or history[-1].role == "USER":
            return next(agent for agent in agents if agent.name == "IncidentManager")
        return next(agent for agent in agents if agent.name == "DevOpsAssistant")
```

### Estratégia de Término
Finaliza a conversa quando não há mais ações necessárias:

```python
class ApprovalTerminationStrategy:
    async def should_agent_terminate(self, agent, history):
        return "no action needed" in history[-1].content.lower()
```

### Configurar o Chat em Grupo
```python
chat = AgentGroupChat(
    agents=[incident_agent, devops_agent],
    termination_strategy=ApprovalTerminationStrategy(),
    selection_strategy=SelectionStrategy()
)
```


## Executar a Solução Multiagente
1. Autentique-se no Azure:
   ```powershell
   az login
   ```
2. Execute o aplicativo:
   ```powershell
   python agent_chat.py
   ```

**Exemplo de saída**:
```
INCIDENT_MANAGER > /logs/log1.log | Reinicie o ServiceX
DEVOPS_ASSISTANT > ServiceX reiniciado com sucesso.
INCIDENT_MANAGER > Nenhuma ação necessária.
```


## Limpeza de Recursos
1. No Azure Portal, acesse seu grupo de recursos
2. Selecione **Delete resource group**
3. Confirme a exclusão


## Conclusão
Você criou com sucesso uma solução multiagente que:
1. Detecta automaticamente problemas em logs
2. Recomenda ações corretivas
3. Executa as correções necessárias
4. Verifica os resultados

Esta arquitetura pode ser expandida para diversas automações complexas onde múltiplos agentes especializados colaboram para resolver problemas.

## Referência
[Develop a multi-agent solution](https://microsoftlearning.github.io/mslearn-ai-agents/Instructions/05-agent-orchestration.html)
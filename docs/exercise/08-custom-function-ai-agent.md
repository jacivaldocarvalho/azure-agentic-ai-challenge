# Criando um Agente de IA com Funções Personalizadas no Azure AI

## Índice
- [Criando um Agente de IA com Funções Personalizadas no Azure AI](#criando-um-agente-de-ia-com-funções-personalizadas-no-azure-ai)
  - [Índice](#índice)
  - [Introdução](#introdução)
  - [Criar um Projeto no Azure AI Foundry](#criar-um-projeto-no-azure-ai-foundry)
  - [Implantar um Modelo de IA Generativa](#implantar-um-modelo-de-ia-generativa)
  - [Desenvolver um Agente com Ferramentas de Função](#desenvolver-um-agente-com-ferramentas-de-função)
    - [Configurar o Ambiente](#configurar-o-ambiente)
  - [Definir uma Função Personalizada](#definir-uma-função-personalizada)
  - [Implementar o Agente](#implementar-o-agente)
  - [Executar o Aplicativo](#executar-o-aplicativo)
  - [Limpeza de Recursos](#limpeza-de-recursos)
  - [Conclusão](#conclusão)
  - [Referência](#referência)


## Introdução
Neste artigo, você aprenderá a criar um agente de IA no Azure AI Foundry que utiliza funções personalizadas como ferramentas para realizar tarefas específicas. Vamos desenvolver um agente de suporte técnico capaz de coletar detalhes sobre problemas técnicos e gerar tickets de suporte automaticamente.

O exercício completo leva aproximadamente **30 minutos** e requer:
- Uma conta no Azure
- Acesso ao Azure AI Foundry
- Conhecimento básico de Python


## Criar um Projeto no Azure AI Foundry
1. Acesse o portal do [Azure AI Foundry](https://ai.azure.com) e faça login
2. Selecione **+ Create project**
3. No assistente de criação:
   - Defina um nome para o projeto
   - Crie um novo hub com as configurações:
     - **Regiões suportadas**: eastus, eastus2, swedencentral, westus ou westus3
     - Crie um novo recurso de Azure AI Services
     - Pule a conexão com Azure AI Search
4. Revise e confirme a criação


## Implantar um Modelo de IA Generativa
1. No painel esquerdo, acesse **Models + endpoints**
2. Selecione **Deploy base model** e escolha o modelo `gpt-4o`
3. Configure a implantação com:
   - Nome personalizado
   - Tipo: Global Standard
   - Atualização automática habilitada
   - Limite de tokens: 50K/min (ou o máximo disponível)
   - Filtro de conteúdo: DefaultV2
4. Aguarde a conclusão da implantação


## Desenvolver um Agente com Ferramentas de Função
### Configurar o Ambiente
1. No Azure Portal, abra o Cloud Shell (PowerShell)
2. Clone o repositório do projeto:
   ```powershell
   rm -r ai-agents -f
   git clone https://github.com/MicrosoftLearning/mslearn-ai-agents ai-agents
   cd ai-agents/Labfiles/03-ai-agent-functions/Python
   ```
3. Instale as dependências:
   ```powershell
   python -m venv labenv
   ./labenv/bin/Activate.ps1
   pip install python-dotenv azure-identity azure-ai-projects
   ```


## Definir uma Função Personalizada
Edite o arquivo `user_functions.py` e adicione:

```python
def submit_support_ticket(email_address: str, description: str) -> str:
    script_dir = Path(__file__).parent
    ticket_number = str(uuid.uuid4()).replace('-', '')[:6]
    file_name = f"ticket-{ticket_number}.txt"
    file_path = script_dir / file_name
    text = f"Support ticket: {ticket_number}\nSubmitted by: {email_address}\nDescription:\n{description}"
    file_path.write_text(text)
    
    message_json = json.dumps({"message": f"Support ticket {ticket_number} submitted."})
    return message_json

user_functions: Set[Callable[..., Any]] = {submit_support_ticket}
```

Esta função gera tickets de suporte com:
- Número único
- Email do solicitante
- Descrição do problema
- Salvamento em arquivo .txt


## Implementar o Agente
No arquivo `agent.py`, adicione:

```python
# Conexão com o projeto
project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(...),
    conn_str=PROJECT_CONNECTION_STRING
)

# Criação do agente
with project_client:
    functions = FunctionTool(user_functions)
    toolset = ToolSet()
    toolset.add(functions)
            
    agent = project_client.agents.create_agent(
        model=MODEL_DEPLOYMENT,
        name="support-agent",
        instructions="Você é um agente de suporte técnico...",
        toolset=toolset
    )

    thread = project_client.agents.create_thread()
```

O agente é configurado para:
- Usar o modelo GPT-4
- Ter instruções específicas para suporte técnico
- Acessar a função personalizada
- Manter o contexto da conversa


## Executar o Aplicativo
1. Autentique-se no Azure:
   ```powershell
   az login
   ```
2. Execute o aplicativo:
   ```powershell
   python agent.py
   ```
3. Interaja com o agente:
   ```
   I have a technical problem
   ```
   O agente irá:
   - Solicitar email e descrição do problema
   - Chamar a função para gerar o ticket
   - Retornar o número do ticket criado

4. Verifique os tickets gerados:
   ```powershell
   cat ticket-<número>.txt
   ```


## Limpeza de Recursos
Para evitar custos desnecessários:
1. No Azure Portal, acesse o grupo de recursos
2. Selecione **Delete resource group**
3. Confirme a exclusão


## Conclusão
Você criou com sucesso um agente de IA com funções personalizadas no Azure AI, capaz de:
- Entender solicitações de suporte
- Coletar informações necessárias
- Gerar tickets automaticamente
- Salvar registros em arquivos

Este padrão pode ser estendido para diversas automações com funções personalizadas.

## Referência

[se a custom function in an AI agent](https://microsoftlearning.github.io/mslearn-ai-agents/Instructions/03-agent-custom-functions.html)

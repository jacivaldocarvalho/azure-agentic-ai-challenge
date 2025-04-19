# Criando um Agente de IA com Azure AI Agent Service  

## Índice  
- [Criando um Agente de IA com Azure AI Agent Service](#criando-um-agente-de-ia-com-azure-ai-agent-service)
  - [Índice](#índice)
  - [Introdução](#introdução)
  - [Criar um Projeto no Azure AI Foundry](#criar-um-projeto-no-azure-ai-foundry)
  - [Implantar um Modelo de IA Generativa](#implantar-um-modelo-de-ia-generativa)
  - [Criar um Aplicativo Cliente para o Agente](#criar-um-aplicativo-cliente-para-o-agente)
    - [Clonar o Repositório do GitHub](#clonar-o-repositório-do-github)
    - [Configurar as Definições do Aplicativo](#configurar-as-definições-do-aplicativo)
  - [Escrever o Código para o Agente](#escrever-o-código-para-o-agente)
  - [Executar o Aplicativo](#executar-o-aplicativo)
  - [Resumo](#resumo)
  - [Limpeza de Recursos](#limpeza-de-recursos)
  - [Referência](#referência)
 

## Introdução  
Neste artigo, você aprenderá a criar um agente de IA utilizando o **Azure AI Agent Service**. O agente será capaz de analisar dados e gerar gráficos dinamicamente usando a ferramenta **Code Interpreter**, que executa código em tempo real para produzir imagens. O exercício completo leva aproximadamente **30 minutos** e requer uma conta no **Azure**.  
 

## Criar um Projeto no Azure AI Foundry  

1. Acesse o portal do **Azure AI Foundry** em [https://ai.azure.com](https://ai.azure.com) e faça login com suas credenciais.  
2. Selecione **+ Criar projeto**.  
3. No assistente de criação:  
   - Defina um **nome válido** para o projeto.  
   - Escolha a opção de criar um novo **hub**.  
   - Personalize as configurações do hub:  
     - **Nome do hub**: Um nome válido.  
     - **Assinatura**: Sua assinatura do Azure.  
     - **Grupo de recursos**: Crie ou selecione um existente.  
     - **Região**: Escolha entre `eastus`, `eastus2`, `swedencentral`, `westus` ou `westus3` (regiões que suportam o modelo `gpt-4o`).  
     - **Recursos do Azure AI Services**: Crie um novo.  
     - **Azure AI Search**: Pule esta etapa.  
4. Revise as configurações e selecione **Criar**.  
5. Após a criação, feche os pop-ups de dicas e verifique a página do projeto.  
  

## Implantar um Modelo de IA Generativa  

1. No painel esquerdo, vá para **Modelos + endpoints**.  
2. Na guia **Model deployments**, selecione **+ Deploy model** → **Deploy base model**.  
3. Procure por `gpt-4o`, selecione-o e personalize a implantação:  
   - **Nome da implantação**: Um nome válido.  
   - **Tipo de implantação**: Global Standard.  
   - **Atualização automática de versão**: Habilitada.  
   - **Versão do modelo**: A mais recente disponível.  
   - **Recurso de IA conectado**: Selecione sua conexão do Azure OpenAI.  
   - **Limite de tokens por minuto (TPM)**: 50K (ou o máximo permitido).  
   - **Filtro de conteúdo**: DefaultV2.  
4. Aguarde a conclusão da implantação.  
  

## Criar um Aplicativo Cliente para o Agente  

### Clonar o Repositório do GitHub  

1. Abra o **Azure Portal** em [https://portal.azure.com](https://portal.azure.com).  
2. Abra o **Cloud Shell** (PowerShell).  
3. Execute:  
   ```powershell
   rm -r ai-agents -f
   git clone https://github.com/MicrosoftLearning/mslearn-ai-agents ai-agents
   cd ai-agents/Labfiles/02-build-ai-agent/Python
   ```  

### Configurar as Definições do Aplicativo  

1. Instale as bibliotecas necessárias:  
   ```powershell
   python -m venv labenv
   ./labenv/bin/Activate.ps1
   pip install python-dotenv azure-identity azure-ai-projects
   ```  
2. Edite o arquivo `.env`:  
   ```powershell
   code .env
   ```  
   - Substitua `your_project_connection_string` pela string de conexão do projeto.  
   - Substitua `your_model_deployment` pelo nome da implantação do modelo.  
   - Salve (CTRL+S) e feche (CTRL+Q).  
 

## Escrever o Código para o Agente  

1. Edite o arquivo `agent.py`:  
   ```powershell
   code agent.py
   ```  
2. Adicione as referências necessárias:  
   ```python
   from azure.identity import DefaultAzureCredential
   from azure.ai.projects import AIProjectClient
   from azure.ai.projects.models import FilePurpose, CodeInterpreterTool
   ```  
3. Conecte-se ao projeto:  
   ```python
   project_client = AIProjectClient.from_connection_string(
       credential=DefaultAzureCredential(
           exclude_environment_credential=True,
           exclude_managed_identity_credential=True),
       conn_str=PROJECT_CONNECTION_STRING
   )
   ```  
4. Faça upload do arquivo de dados e crie a ferramenta **CodeInterpreterTool**:  
   ```python
   file = project_client.agents.upload_file_and_poll(
       file_path=file_path, purpose=FilePurpose.AGENTS
   )
   code_interpreter = CodeInterpreterTool(file_ids=[file.id])
   ```  
5. Defina o agente:  
   ```python
   agent = project_client.agents.create_agent(
       model=MODEL_DEPLOYMENT,
       name="data-agent",
       instructions="Analise os dados do arquivo. Se o usuário pedir um gráfico, crie e salve como .png.",
       tools=code_interpreter.definitions,
       tool_resources=code_interpreter.resources,
   )
   ```  
6. Crie uma thread para a conversa:  
   ```python
   thread = project_client.agents.create_thread()
   ```  
7. Envie prompts ao agente e exiba respostas:  
   ```python
   message = project_client.agents.create_message(
       thread_id=thread.id,
       role="user",
       content=user_prompt,
   )
   run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
   ```  
8. Verifique erros e exiba mensagens:  
   ```python
   if run.status == "failed":
       print(f"Erro: {run.last_error}")
   messages = project_client.agents.list_messages(thread_id=thread.id)
   last_msg = messages.get_last_text_message_by_role("assistant")
   ```  
9. Salve arquivos gerados e limpe recursos:  
   ```python
   for file_path_annotation in messages.file_path_annotations:
       project_client.agents.save_file(file_id=file_path_annotation.file_path.file_id, file_name=Path(file_path_annotation.text).name)
   project_client.agents.delete_agent(agent.id)
   project_client.agents.delete_thread(thread.id)
   ```  
  

## Executar o Aplicativo  

1. Autentique-se no Azure:  
   ```powershell
   az login
   ```  
2. Execute o aplicativo:  
   ```powershell
   python agent.py
   ```  
3. Teste o agente com prompts como:  
   - *"Qual é a categoria com o maior custo?"*  
   - *"Crie um gráfico de pizza mostrando custo por categoria."*  
4. Para sair, digite **quit**.  


## Resumo  
Neste artigo, você criou um **agente de IA** no **Azure AI Agent Service** capaz de analisar dados e gerar gráficos usando o **Code Interpreter**.  
 

## Limpeza de Recursos  
Para evitar custos desnecessários:  
1. No **Azure Portal**, vá ao **grupo de recursos** usado.  
2. Selecione **Excluir grupo de recursos** e confirme.  

Pronto! Seu agente de IA está funcionando e pode ser expandido para tarefas mais complexas. 🚀

## Referência

[Develop an AI agent](https://microsoftlearning.github.io/mslearn-ai-agents/Instructions/02-build-ai-agent.html)
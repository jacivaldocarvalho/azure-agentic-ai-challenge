# **Como Criar um Chat App Personalizado com Azure AI Foundry e Prompt Flow**

## Índice
- [**Como Criar um Chat App Personalizado com Azure AI Foundry e Prompt Flow**](#como-criar-um-chat-app-personalizado-com-azure-ai-foundry-e-prompt-flow)
  - [Índice](#índice)
  - [**Introdução**](#introdução)
  - [**Passo 1: Criar um Projeto no Azure AI Foundry**](#passo-1-criar-um-projeto-no-azure-ai-foundry)
  - [**Passo 2: Implantar um Modelo GPT-4**](#passo-2-implantar-um-modelo-gpt-4)
    - [**Personalizando o Assistente de Viagens**](#personalizando-o-assistente-de-viagens)
  - [**Passo 3: Criar e Executar um Prompt Flow**](#passo-3-criar-e-executar-um-prompt-flow)
    - [**Configurando o Fluxo**](#configurando-o-fluxo)
    - [**Testando o Fluxo**](#testando-o-fluxo)
  - [**Passo 4: Implantar o Fluxo como um Endpoint**](#passo-4-implantar-o-fluxo-como-um-endpoint)
  - [**Conclusão**](#conclusão)
    - [**Limpeza de Recursos**](#limpeza-de-recursos)
  - [Referência](#referência)

## **Introdução**  
Neste artigo, você aprenderá a criar um aplicativo de chat personalizado usando o **Azure AI Foundry** e o **Prompt Flow**. O objetivo é desenvolver um assistente virtual baseado em um modelo GPT do **Azure OpenAI**, capaz de responder a perguntas relacionadas a viagens de forma inteligente e contextualizada.  

O processo inclui:  
1. Criar um projeto no **Azure AI Foundry**.  
2. Implantar um modelo **GPT-4**.  
3. Configurar um **Prompt Flow** para gerenciar conversas.  
4. Testar e implantar o fluxo como um endpoint.  

Vamos começar!  
 

## **Passo 1: Criar um Projeto no Azure AI Foundry**  

1. Acesse o portal do **Azure AI Foundry** em [https://ai.azure.com](https://ai.azure.com) e faça login com suas credenciais da Azure.  
2. Na página inicial, selecione **+ Create project**.  
3. No assistente de criação:  
   - Defina um nome para o projeto (ex: `my-ai-project`).  
   - Personalize as configurações do **hub**:  
     - **Hub name**: Um nome único (ex: `my-ai-hub`).  
     - **Subscription**: Sua assinatura Azure.  
     - **Resource group**: Crie um novo (ex: `my-ai-resources`).  
     - **Location**: Selecione a região recomendada para **GPT-4**.  
     - **Azure AI Services**: Crie um novo recurso (ex: `my-ai-services`).  
     - **Azure AI Search**: Pule esta etapa.  
4. Revise as configurações e selecione **Create**.  

Após a conclusão, você será direcionado para a página do projeto.  
 

## **Passo 2: Implantar um Modelo GPT-4**  

Para usar o modelo em um fluxo de conversa, é necessário implantá-lo primeiro:  

1. Na barra lateral, vá para **Models + endpoints** e selecione **+ Deploy model** > **Deploy base model**.  
2. Configure o modelo **GPT-4**:  
   - **Deployment name**: Um nome único.  
   - **Deployment type**: Standard.  
   - **Model version**: Mantenha a padrão.  
   - **AI resource**: Selecione o recurso criado anteriormente.  
   - **Tokens per Minute Rate Limit**: 5K.  
   - **Content filter**: DefaultV2.  
   - **Enable dynamic quota**: Desativado.  
3. Aguarde a implantação e selecione **Open in playground**.  

### **Personalizando o Assistente de Viagens**  
No playground, altere a mensagem do sistema para:  

```markdown
**Objective**: Assist users with travel-related inquiries, offering tips, advice, and recommendations as a knowledgeable travel agent.

**Capabilities**:  
- Provide up-to-date travel information, including destinations, accommodations, transportation, and local attractions.  
- Offer personalized travel suggestions based on user preferences, budget, and travel dates.  
- Share tips on packing, safety, and navigating travel disruptions.  
- Help with itinerary planning, including optimal routes and must-see landmarks.  
- Answer common travel questions and provide solutions to potential travel issues.  

**Instructions**:  
1. Engage with the user in a friendly and professional manner, as a travel agent would.  
2. Use available resources to provide accurate and relevant travel information.  
3. Tailor responses to the user's specific travel needs and interests.  
4. Ensure recommendations are practical and consider the user's safety and comfort.  
5. Encourage the user to ask follow-up questions for further assistance.  
```  

Teste perguntando: *"What can you do?"* e observe a resposta personalizada.  
 

## **Passo 3: Criar e Executar um Prompt Flow**  

Agora, transformaremos essa configuração em um fluxo de chat automatizado:  

1. No **Chat playground**, selecione **Prompt flow** na barra superior.  
2. Defina o nome da pasta como **Travel-Chat**.  
3. Um fluxo básico será criado com:  
   - **Entradas**: Histórico do chat e pergunta do usuário.  
   - **Nó LLM**: Conectado ao modelo implantado.  
   - **Saída**: Resposta gerada.  

### **Configurando o Fluxo**  
1. Inicie uma sessão de computação (**Start compute session**).  
2. No nó **LLM (chat)**:  
   - **Connection**: Selecione a conexão criada.  
   - **Api**: `chat`.  
   - **deployment_name**: Selecione o modelo **GPT-4** implantado.  
   - **response_format**: `{"type":"text"}`.  
3. Verifique se o **prompt** contém as instruções personalizadas.  

### **Testando o Fluxo**  
1. Salve o fluxo (**Save**).  
2. Selecione **Chat** e teste com:  
   - *"I have one day in London, what should I do?"*  
 

## **Passo 4: Implantar o Fluxo como um Endpoint**  

Quando estiver satisfeito com os resultados, implante o fluxo:  

1. Selecione **Deploy** e configure:  
   - **Endpoint**: Novo.  
   - **Endpoint name**: Um nome único.  
   - **Deployment name**: Um nome único.  
   - **Virtual machine**: `Standard_DS3_v2`.  
   - **Instance count**: `3`.  
   - **Inferencing data collection**: Ativado.  

2. Após a implantação, vá para **Models + endpoints** e teste o endpoint com:  
   - *"What is there to do in San Francisco?"*  
   - *"Where else could I go?"*  

3. Na página **Consume**, você encontrará informações de conexão e exemplos de código para integrar o endpoint em um aplicativo.  


## **Conclusão**  

Neste tutorial, você aprendeu a:  
✅ Criar um projeto no **Azure AI Foundry**.  
✅ Implantar um modelo **GPT-4** personalizado.  
✅ Configurar um **Prompt Flow** para um assistente de viagens.  
✅ Testar e implantar o fluxo como um endpoint.  

Agora, você pode integrar esse chat em aplicativos como um **copilot personalizado**!  

### **Limpeza de Recursos**  
Para evitar custos desnecessários:  
1. Acesse o [Portal Azure](https://portal.azure.com).  
2. Vá para **Resource groups**.  
3. Selecione o grupo criado e clique em **Delete resource group**.  

## Referência
[Use a prompt flow to manage conversation in a chat app](https://microsoftlearning.github.io/mslearn-ai-studio/Instructions/03-Use-prompt-flow-chat.html)
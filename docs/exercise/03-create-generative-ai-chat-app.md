# **Criando um Aplicativo de Chat com IA Generativa usando Azure AI Foundry**  
Neste artigo, vamos explorar como criar um aplicativo de chat que utiliza IA generativa para responder perguntas. Usaremos o **Azure AI Foundry SDK** para conectar um projeto a um modelo de linguagem avançado, como o **GPT-4o**, e implementar uma interface de conversação interativa.

Este exercício leva aproximadamente **40 minutos** e é ideal para desenvolvedores que desejam integrar IA generativa em suas aplicações. 

## **Índice**  

- [**Criando um Aplicativo de Chat com IA Generativa usando Azure AI Foundry**](#criando-um-aplicativo-de-chat-com-ia-generativa-usando-azure-ai-foundry)
  - [**Índice**](#índice)
  - [**Pré-requisitos**](#pré-requisitos)
  - [**Passo 1: Criando um Projeto no Azure AI Foundry**](#passo-1-criando-um-projeto-no-azure-ai-foundry)
  - [**Passo 2: Implantando um Modelo de IA Generativa**](#passo-2-implantando-um-modelo-de-ia-generativa)
  - [**Passo 3: Criando um Aplicativo de Chat**](#passo-3-criando-um-aplicativo-de-chat)
    - [**Preparando o Ambiente**](#preparando-o-ambiente)
    - [**Escrevendo o Código do Chat**](#escrevendo-o-código-do-chat)
      - [**Python**](#python)
      - [**C#**](#c)
    - [**Executando o Aplicativo**](#executando-o-aplicativo)
  - [**Usando o SDK da OpenAI (Opcional)**](#usando-o-sdk-da-openai-opcional)
  - [**Conclusão**](#conclusão)
  - [Referência](#referência)



## **Pré-requisitos**  
- Uma conta **Azure** ativa.  
- Acesso ao portal **Azure AI Foundry** ([https://ai.azure.com](https://ai.azure.com)).  
- Conhecimento básico de **Python** ou **C#** (o tutorial oferece opções para ambas as linguagens).  


## **Passo 1: Criando um Projeto no Azure AI Foundry**  

1. **Acesse o Portal Azure AI Foundry**  
   - Abra o navegador e acesse [https://ai.azure.com](https://ai.azure.com).  
   - Faça login com suas credenciais Azure.  

2. **Crie um Novo Projeto**  
   - Na página inicial, clique em **+ Create project**.  
   - Defina um nome para o projeto (ex: `meu-projeto-ia`).  
   - Selecione a opção para criar um novo **hub** (ex: `meu-hub-ia`).  

3. **Configure os Recursos do Azure**  
   - **Assinatura**: Selecione sua assinatura Azure.  
   - **Grupo de recursos**: Crie um novo (ex: `meus-recursos-ia`) ou use um existente.  
   - **Localização**: Selecione a região recomendada para o modelo **GPT-4o**.  
   - **Azure AI Services**: Crie um novo recurso (ex: `meus-servicos-ia`).  
   - **Azure AI Search**: Pule esta configuração.  

4. **Revise e Crie**  
   - Confirme as configurações e clique em **Create**.  
   - Aguarde a implantação ser concluída.  
 

## **Passo 2: Implantando um Modelo de IA Generativa**  

Agora, vamos implantar um modelo de linguagem para uso no chat.  

1. **Acesse a Página de Modelos**  
   - No menu à esquerda, vá para **Models + endpoints**.  
   - Clique em **+ Deploy model** e selecione **Deploy base model**.  

2. **Selecione o Modelo GPT-4o**  
   - Busque por **gpt-4o** e confirme a seleção.  

3. **Configure a Implantação**  
   - **Nome da implantação**: `gpt-4o`  
   - **Tipo de implantação**: **Global Standard**  
   - **Versão do modelo**: Use a mais recente disponível.  
   - **Recurso de IA conectado**: Selecione o recurso criado anteriormente.  
   - **Limite de tokens por minuto (TPM)**: Defina para **50K** (ou o máximo permitido).  
   - **Filtro de conteúdo**: **DefaultV2**  

4. **Aguarde a Implantação**  
   - O processo pode levar alguns minutos.  
 

## **Passo 3: Criando um Aplicativo de Chat**  

Vamos desenvolver um cliente em **Python** ou **C#** para interagir com o modelo.  

### **Preparando o Ambiente**  

1. **Obtenha a String de Conexão**  
   - No portal Azure AI Foundry, vá para **Overview** e copie a **Project connection string**.  

2. **Configure o Cloud Shell no Azure**  
   - Abra o **Azure Portal** ([https://portal.azure.com](https://portal.azure.com)).  
   - Ative o **Cloud Shell** (PowerShell).  

3. **Clone o Repositório do GitHub**  
   ```bash
   rm -r mslearn-ai-foundry -f
   git clone https://github.com/microsoftlearning/mslearn-ai-studio mslearn-ai-foundry
   ```
   - Navegue até a pasta do projeto:  
     - **Python**:  
       ```bash
       cd mslearn-ai-foundry/labfiles/chat-app/python
       ```
     - **C#**:  
       ```bash
       cd mslearn-ai-foundry/labfiles/chat-app/c-sharp
       ```

4. **Instale as Dependências**  
   - **Python**:  
     ```bash
     pip install python-dotenv azure-identity azure-ai-projects azure-ai-inference
     ```
   - **C#**:  
     ```bash
     dotnet add package Azure.Identity
     dotnet add package Azure.AI.Projects --version 1.0.0-beta.3
     dotnet add package Azure.AI.Inference --version 1.0.0-beta.3
     ```

5. **Configure o Arquivo de Ambiente**  
   - Edite `.env` (Python) ou `appsettings.json` (C#) e insira:  
     - A **string de conexão do projeto**.  
     - O **nome da implantação do modelo** (ex: `gpt-4o`).  


### **Escrevendo o Código do Chat**  

#### **Python**  
```python
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.inference.models import SystemMessage, UserMessage, AssistantMessage

# Carrega configurações
load_dotenv()
project_connection = os.getenv("PROJECT_CONNECTION_STRING")
model_deployment = os.getenv("MODEL_DEPLOYMENT")

# Conecta ao projeto
projectClient = AIProjectClient.from_connection_string(
    conn_str=project_connection,
    credential=DefaultAzureCredential())

# Cria cliente de chat
chat = projectClient.inference.get_chat_completions_client()

# Inicia a conversa
prompt = [SystemMessage("Você é um assistente de IA útil.")]

while True:
    input_text = input("Você: ")
    if input_text.lower() == "quit":
        break
    prompt.append(UserMessage(input_text))
    response = chat.complete(model=model_deployment, messages=prompt)
    completion = response.choices[0].message.content
    print(f"IA: {completion}")
    prompt.append(AssistantMessage(completion))
```

#### **C#**  
```csharp
using Azure.Identity;
using Azure.AI.Projects;
using Azure.AI.Inference;

var project_connection = config["ProjectConnectionString"];
var model_deployment = config["ModelDeployment"];

// Conecta ao projeto
var projectClient = new AIProjectClient(project_connection, new DefaultAzureCredential());

// Cria cliente de chat
var chat = projectClient.GetChatCompletionsClient();

// Inicia a conversa
var prompt = new List<ChatRequestMessage>() {
    new ChatRequestSystemMessage("Você é um assistente de IA útil.")
};

while (true)
{
    Console.Write("Você: ");
    string input_text = Console.ReadLine();
    if (input_text.ToLower() == "quit") break;

    prompt.Add(new ChatRequestUserMessage(input_text));
    var response = chat.Complete(new ChatCompletionsOptions() {
        Model = model_deployment,
        Messages = prompt
    });
    Console.WriteLine($"IA: {response.Value.Content}");
    prompt.Add(new ChatRequestAssistantMessage(response.Value.Content));
}
```


### **Executando o Aplicativo**  
- **Python**:  
  ```bash
  python chat-app.py
  ```
- **C#**:  
  ```bash
  dotnet run
  ```

Teste perguntando:  
- *"Qual é o animal mais rápido do mundo?"*  
- *"Onde posso ver um?"*  

Digite **quit** para sair.  

---

## **Usando o SDK da OpenAI (Opcional)**  
Se preferir, você pode adaptar o código para usar o **OpenAI SDK** diretamente.  

1. **Instale o SDK**:  
   - **Python**:  
     ```bash
     pip install openai
     ```
   - **C#**:  
     ```bash
     dotnet add package Azure.AI.OpenAI --prerelease
     ```

2. **Modifique o Código**:  
   Substitua o cliente de chat por:  
   ```python
   openai_client = projectClient.inference.get_azure_openai_client()
   response = openai_client.chat.completions.create(
       model=model_deployment,
       messages=prompt
   )
   ```


## **Conclusão**  
Neste tutorial, você:  
✅ Criou um projeto no **Azure AI Foundry**.  
✅ Implantou o modelo **GPT-4o**.  
✅ Desenvolveu um **aplicativo de chat** em Python ou C#.  

Agora você pode expandir esse projeto integrando-o a um **frontend web** ou adicionando mais funcionalidades!  

Para evitar custos desnecessários, **exclua o grupo de recursos** no Azure Portal após o uso.  

🚀 **Pronto para inovar com IA generativa?** Experimente e compartilhe seus resultados!

## Referência
[Create a generative AI chat app](https://microsoftlearning.github.io/mslearn-ai-studio/Instructions/02a-AI-foundry-sdk.html)

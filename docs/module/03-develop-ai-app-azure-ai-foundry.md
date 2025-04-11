# Desenvolver um aplicativo de IA com o SDK do Azure AI Foundry
Use o SDK do Azure AI Foundry para desenvolver aplicativos de IA com projetos do Azure AI Foundry.

## Índice

- [Desenvolver um aplicativo de IA com o SDK do Azure AI Foundry](#desenvolver-um-aplicativo-de-ia-com-o-sdk-do-azure-ai-foundry)
  - [Índice](#índice)
  - [Introdução](#introdução)
  - [O que é o SDK do Azure AI Foundry?](#o-que-é-o-sdk-do-azure-ai-foundry)
    - [Instalando pacotes do SDK](#instalando-pacotes-do-sdk)
    - [Usando o SDK para se conectar a um projeto](#usando-o-sdk-para-se-conectar-a-um-projeto)
  - [Trabalhar com conexões de projeto](#trabalhar-com-conexões-de-projeto)
  - [Criar um cliente de chat](#criar-um-cliente-de-chat)
    - [Criando um aplicativo cliente para implantações de inferência de modelo de IA do Azure](#criando-um-aplicativo-cliente-para-implantações-de-inferência-de-modelo-de-ia-do-azure)
    - [Criando um aplicativo cliente para implantações de serviço do Azure OpenAI](#criando-um-aplicativo-cliente-para-implantações-de-serviço-do-azure-openai)
  - [Resumo](#resumo)


## Introdução
Os desenvolvedores que criam soluções de IA com o Azure AI Foundry precisam trabalhar com uma combinação de serviços e estruturas de software. O SDK do Azure AI Foundry foi projetado para reunir serviços comuns e bibliotecas de código em um projeto de IA por meio de um ponto de acesso programático central, facilitando que os desenvolvedores escrevam o código necessário para criar aplicativos de IA eficazes no Azure.

Neste módulo, você aprenderá a usar o SDK do Azure AI Foundry para trabalhar com recursos em um projeto de IA.

## O que é o SDK do Azure AI Foundry?
O SDK do Azure AI Foundry é um conjunto de pacotes e serviços projetados para trabalhar em conjunto para permitir que os desenvolvedores escrevam código que usa recursos em um projeto do Azure AI Foundry. Com o SDK do Azure AI Foundry, os desenvolvedores podem criar aplicativos que se conectam a um projeto, acessar as conexões de recursos e modelos nesse projeto e usá-los para executar operações de IA, como enviar prompts para um modelo de IA gerativo e processar as respostas

O SDK fornece bibliotecas .NET do Python e do Microsoft C# que você pode usar para criar aplicativos de IA com base em projetos do Azure AI Foundry.

### Instalando pacotes do SDK
O pacote principal para trabalhar com projetos no SDK do Azure AI Foundry é a biblioteca de projetos de IA do Azure, que permite que você se conecte a um projeto do Azure AI Foundry e acesse os recursos definidos nele.

Para usar a biblioteca projetos de IA do Azure no Python, você pode usar o utilitário de instalação de pacotes do pip para instalar o pacote de azure-ai-projects do PyPi:

´´´python
pip install azure-ai-projects
´´´

### Usando o SDK para se conectar a um projeto
A primeira tarefa na maioria dos códigos do SDK do Azure AI Foundry é conectar-se a um projeto do Azure AI Foundry. Cada projeto tem uma cadeia de conexão exclusiva, que você pode encontrar na página Visão Geral do projeto no portal do Azure AI Foundry.

![](https://learn.microsoft.com/pt-br/training/wwl-data-ai/ai-foundry-sdk/media/ai-project-overview.png)

Você pode usar essa cadeia de conexão em seu código para criar um objeto AIProjectClient, que fornece um proxy programático para o projeto.

O snippet de código a seguir mostra como criar o objeto am AIProjectClient no Python.

```python
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import ConnectionType
from azure.identity import DefaultAzureCredential
...

project_connection_string = "<region>.api.azureml.ms;<project_id>;<hub_name>;<project_name>"
project_client = AIProjectClient.from_connection_string(
      credential=DefaultAzureCredential(),
      conn_str=project_connection_string,
    )
```
>Observação
O código usa as credenciais padrão do Azure para autenticar ao acessar o projeto. Para habilitar essa autenticação, além do pacote azure-ai-projects, você precisa instalar o pacote de identidade do azure:
pip install azure-identity

>Dica
Para acessar o projeto com êxito, o código Python deve ser executado no contexto de uma sessão autenticada do Azure. Por exemplo, você pode usar o comando CLI (interface de linha de comando) do Azure az-login para entrar antes de executar o código.

## Trabalhar com conexões de projeto
Cada projeto do Azure AI Foundry inclui recursos conectados, que são definidos no do hub e nível de projeto. Cada recurso é uma conexão a um serviço externo, como serviços de IA do Azure, armazenamento do Azure, pesquisa de IA do Azure e outros.

![](https://learn.microsoft.com/pt-br/training/wwl-data-ai/ai-foundry-sdk/media/ai-project-connections.png)

Com o SDK do Azure AI Foundry, você pode se conectar a um projeto e recuperar conexões; que você pode usar para consumir os serviços conectados.

O objeto A**IProjectClient** no Python tem uma propriedade de conexões, que você pode usar para acessar as conexões de recurso no projeto. Os métodos das conexões objeto incluem:

- ```connections.list()```: retorna uma coleção de objetos de conexão, cada um representando uma conexão no projeto. Você pode filtrar os resultados especificando um parâmetro de connection_type opcional com uma enumeração válida, como ```ConnectionType.AZURE_AI_SERVICE```.
- ```connections.get(connection_name, include_credentials)```: retorna um objeto de conexão para a conexão com o nome especificado. Se o parâmetro include_credentials for True (o valor padrão), as credenciais necessárias para se conectar à conexão serão retornadas , por exemplo, na forma de uma chave de API para um recurso de serviços de IA do Azure.
- ```connections.get_default(connection_type, include_credentials)```: retorna a conexão padrão do tipo especificado – por exemplo, a conexão padrão dos serviços de IA do Azure definida no projeto.

Os objetos de conexão retornados por esses métodos incluem propriedades específicas de conexão, que você pode usar para se conectar ao recurso associado. Por exemplo, o snippet de código a seguir recupera a conexão padrão dos serviços de IA do Azure e a usa para instanciar um objeto TextAnalyticsClient para usar a funcionalidade de análise de sentimento do serviço de Linguagem de IA do Azure (que está incluído em um recurso dos serviços de IA do Azure).

```python
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import ConnectionType
from azure.identity import DefaultAzureCredential
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

try:
    # Get project client
    project_connection_string = "<region>.api.azureml.ms;<project_id>;<hub_name>;<project_name>"
    project_client = AIProjectClient.from_connection_string(
      credential=DefaultAzureCredential(),
      conn_str=project_connection_string,
    )

    # Get the properties of the default Azure AI Services connection with credentials
    connection = project_client.connections.get_default(
      connection_type=ConnectionType.AZURE_AI_SERVICES,
      include_credentials=True, 
    )

    # Use the connection information to create a text analytics client
    ai_svc_credential = AzureKeyCredential(connection.key)
    text_analytics_client = TextAnalyticsClient(endpoint=connection.endpoint_url, credential=ai_svc_credential)

    # Use the Language service to analyze some text (to infer sentiment) 
    text = "I hated the movie. It was so slow!"
    sentimentAnalysis = text_analytics_client.analyze_sentiment(documents=[text])[0]
    print("Text: {}\nSentiment: {}".format(text,sentimentAnalysis.sentiment))

except Exception as ex:
    print(ex)
```

>Observação
Além dos pacotes de azure-ai-projects e de identidade do azure discutidos anteriormente, o código de exemplo mostrado aqui pressupõe que o pacote azure-ai-textanalytics foi instalado:
pip install azure-ai-textanalytics

## Criar um cliente de chat
 Um cenário comum em um aplicativo de IA é conectar-se a um modelo de IA generativo e usar prompts para se envolver em uma caixa de diálogo baseada em chat com ele. Você pode usar o SDK do Azure AI Foundry para conversar com modelos implantados em seu projeto do Azure AI Foundry.

As bibliotecas e o código específicos usados para criar um cliente de chat dependem de como o modelo de destino foi implantado no projeto do Azure AI Foundry. Você pode implantar modelos nas seguintes soluções de hospedagem de modelo:

- **inferência de modelo de IA do Azure**: um único ponto de extremidade para vários modelos de diferentes tipos, incluindo modelos OpenAI e outros do catálogo de modelos do Azure AI Foundry. Os modelos são consumidos por meio de um serviços de IA do Azure conexão de recurso no projeto.
- **serviço do Azure OpenAI**: um único ponto de extremidade para modelos OpenAI hospedados no Azure. Os modelos são consumidos por meio de um serviço Azure OpenAI conexão de recurso no projeto.
- **API sem servidor**: uma solução de modelo como serviço na qual cada modelo implantado é acessado por meio de um ponto de extremidade exclusivo e hospedado no projeto Azure AI Foundry.
- **de computação gerenciada**: uma solução de modelo como serviço na qual cada modelo implantado é acessado por meio de um ponto de extremidade exclusivo hospedado na computação personalizada.

>Observação
Para implantar modelos em um ponto de extremidade de inferência de modelo de IA do Azure, você deve habilitar a opção Implantar modelos no serviço de inferência de modelo de IA do Azure opção no Azure AI Foundry.

Neste módulo, nos concentraremos em modelos implantados no serviço de de inferência do modelo de IA do Azure e modelos implantados no serviço de Azure OpenAI.

### Criando um aplicativo cliente para implantações de inferência de modelo de IA do Azure
Quando você implantou modelos no serviço de inferência de modelo de IA do Azure, pode usar o SDK do Azure AI Foundry para escrever código que cria um objeto ChatCompletionsClient, que você pode usar para conversar com um modelo implantado. Um dos benefícios de usar esse tipo de implantação de modelo é que você pode alternar facilmente entre modelos implantados alterando um parâmetro em seu código (o nome da implantação do modelo), tornando-se uma ótima maneira de testar em vários modelos durante o desenvolvimento de um aplicativo.

O exemplo de código python a seguir usa um objeto ChatCompletionsClient para conversar com uma implantação de modelo chamada de modelo phi-4.

````python
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.inference.models import SystemMessage, UserMessage

try:

    # Initialize the project client
    project_connection_string = "<region>.api.azureml.ms;<project_id>;<hub_name>;<project_name>"
    project_client = AIProjectClient.from_connection_string(
        credential=DefaultAzureCredential(),
        conn_str=project_connection_string,
    )

    ## Get a chat client
    chat = project_client.inference.get_chat_completions_client()

    # Get a chat completion based on a user-provided prompt
    user_prompt = input("Enter a question:")

    response = chat.complete(
        model="phi-4-model",
        messages=[
                   SystemMessage("You are a helpful AI assistant that answers questions."),
                   UserMessage(user_prompt)
        ],
    )
    print(response.choices[0].message.content)

except Exception as ex:
    print(ex)
````

> Observação
A classe ChatCompletionsClient usa biblioteca de de Inferência de IA do Azure. Além dos pacotes azure-ai-projects e de identidade do azure discutidos anteriormente, o código de exemplo mostrado aqui pressupõe que o pacote de azure-ai-inference foi instalado:
pip install azure-ai-inference

### Criando um aplicativo cliente para implantações de serviço do Azure OpenAI
Ao implantar modelos no serviço Azure OpenAI, você pode usar o **AIProjectConnection** para se conectar ao recurso de serviço do Azure OpenAI em seu projeto e, em seguida, usar o SDK do Azure OpenAI para conversar com seus modelos.

No SDK do Azure AI Foundry para Python, a classe **AIProjectClient** fornece um método **get_azure_openai_client()** que você pode usar para criar um objeto cliente do Azure OpenAI. Em seguida, você pode usar as classes e os métodos definidos no SDK do Azure OpenAI para consumir um modelo implantado no serviço Azure OpenAI.

O exemplo de código python a seguir usa os SDKs do Azure AI Foundry e do Azure OpenAI para conversar com uma implantação de modelo chamada de modelo gpt-4.

```python
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
import openai


try:
    # Initialize the project client
    project_connection_string = "<region>.api.azureml.ms;<project_id>;<hub_name>;<project_name>"
    project_client = AIProjectClient.from_connection_string(
        credential=DefaultAzureCredential(),
        conn_str=project_connection_string,
    )

    ## Get an Azure OpenAI chat client
    openai_client = project_client.inference.get_azure_openai_client(api_version="2024-06-01")

    # Get a chat completion based on a user-provided prompt
    user_prompt = input("Enter a question:")
    response = openai_client.chat.completions.create(
        model="gpt-4-model",
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant that answers questions."},
            {"role": "user", "content": user_prompt},
        ]
    )
    print(response.choices[0].message.content)

except Exception as ex:
    print(ex)
```

>Observação
Além do azure-ai-projects e pacotes de de identidade do azure discutidos anteriormente, o código de exemplo mostrado aqui pressupõe que o pacote de openai foi instalado:
pip install openai

## Resumo
Usando o SDK do Azure AI Foundry, você pode desenvolver aplicativos avançados de IA que usam recursos em seus projetos do Azure AI Foundry. O SDK do Azure AI Foundry classe AIProjectClient fornece um proxy programático para um projeto, permitindo que você acesse recursos conectados e use bibliotecas específicas do serviço para consumi-los.

>Observação
Para obter mais informações sobre o SDK do Azure AI Foundry, consulte O [SDK do Azure AI Foundry](https://learn.microsoft.com/pt-br/azure/ai-foundry/how-to/develop/sdk-overview?tabs=sync&pivots=programming-language-python).



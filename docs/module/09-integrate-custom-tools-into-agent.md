# Integrar ferramentas personalizadas ao seu agente

> As ferramentas internas são úteis, mas podem não atender a todas as suas necessidades. Neste módulo, saiba como estender os recursos do seu agente integrando ferramentas personalizadas para seu agente usar.


## Índice

- [Integrar ferramentas personalizadas ao seu agente](#integrar-ferramentas-personalizadas-ao-seu-agente)
  - [Índice](#índice)
  - [Introdução](#introdução)
  - [Por que usar ferramentas personalizadas](#por-que-usar-ferramentas-personalizadas)
    - [Por que usar ferramentas personalizadas?](#por-que-usar-ferramentas-personalizadas-1)
    - [Cenários comuns para ferramentas personalizadas em agentes](#cenários-comuns-para-ferramentas-personalizadas-em-agentes)
      - [Automação de suporte ao cliente](#automação-de-suporte-ao-cliente)
      - [Gerenciamento de inventário](#gerenciamento-de-inventário)
      - [Agendamento de consultas de saúde](#agendamento-de-consultas-de-saúde)
      - [Suporte ao Helpdesk de TI](#suporte-ao-helpdesk-de-ti)
      - [E-learning e treinamento](#e-learning-e-treinamento)
  - [Opções para implementar ferramentas personalizadas](#opções-para-implementar-ferramentas-personalizadas)
  - [Como integrar ferramentas personalizadas](#como-integrar-ferramentas-personalizadas)
    - [Chamada de função](#chamada-de-função)
    - [Exemplo: Definir e usar uma função](#exemplo-definir-e-usar-uma-função)
    - [Funções do Azure](#funções-do-azure)
      - [Exemplo: usando o Azure Functions com um gatilho de fila](#exemplo-usando-o-azure-functions-com-um-gatilho-de-fila)
    - [Especificação do OpenAPI](#especificação-do-openapi)
      - [Exemplo: usando uma especificação OpenAPI](#exemplo-usando-uma-especificação-openapi)
  - [Resumo](#resumo)

## Introdução
O Serviço de Agente de IA do Azure oferece uma maneira perfeita de criar um agente sem precisar de uma ampla experiência em IA ou machine learning. Usando ferramentas, você pode fornecer ao seu agente funcionalidade para executar ações em seu nome.

O Serviço de Agente de IA fornece ferramentas internas para coletar conhecimento e gerar código, que fornecem ao agente alguma funcionalidade poderosa. No entanto, às vezes, seu agente precisa ser capaz de concluir tarefas ou ações específicas que um modelo de IA teria dificuldades para lidar por conta própria. Para realizar essas ações, você pode fornecer ao agente uma ferramenta personalizada com base em seu próprio código ou em um serviço ou API de terceiros.

Imagine que você está trabalhando no setor de varejo, e sua empresa está lutando para gerenciar consultas de clientes com eficiência. A equipe de suporte ao cliente está sobrecarregada de perguntas repetitivas, levando a atrasos nos tempos de resposta e à diminuição da satisfação do cliente. Usando o Serviço de Agente de IA do Azure com ferramentas personalizadas, você pode criar um agente de perguntas frequentes personalizado que lida com consultas comuns. Esse agente pode ser fornecido com um conjunto de ferramentas personalizadas para pesquisar pedidos de clientes, liberando sua equipe de suporte para se concentrar em problemas mais complexos.

Neste módulo, você aprenderá a utilizar ferramentas personalizadas no Serviço do Agente de IA do Azure para aumentar a produtividade, melhorar a precisão e criar soluções personalizadas para necessidades específicas.

## Por que usar ferramentas personalizadas
O Serviço de Agente de IA do Azure oferece uma plataforma avançada para integrar ferramentas personalizadas para aumentar a produtividade e fornecer soluções personalizadas para necessidades de negócios específicas. Usando essas ferramentas personalizadas, as empresas podem obter maior eficiência e eficácia em suas operações.

### Por que usar ferramentas personalizadas?
As ferramentas personalizadas nos serviços de IA do Azure podem aumentar significativamente a produtividade automatizando tarefas repetitivas e simplificando fluxos de trabalho específicos para seu caso de uso. Essas ferramentas melhoram a precisão fornecendo saídas precisas e consistentes, reduzindo a probabilidade de erro humano. Além disso, as ferramentas personalizadas oferecem soluções personalizadas que abordam necessidades comerciais específicas, permitindo que as organizações otimizem seus processos e obtenham melhores resultados.

- Produtividade aprimorada: automatizar tarefas repetitivas e simplificar fluxos de trabalho.
- Precisão aprimorada: forneça saídas precisas e consistentes, reduzindo o erro humano.
- Soluções personalizadas: atender às necessidades de negócios específicas e otimizar processos.

A adição de ferramentas disponibiliza funcionalidades personalizadas para o agente usar, dependendo de como ele decide responder ao prompt do usuário. Por exemplo, considere como uma ferramenta personalizada para recuperar dados meteorológicos de um serviço meteorológico externo pode ser usada por um agente.

![](https://learn.microsoft.com/pt-br/training/wwl-data-ai/build-agent-with-custom-tools/media/agent-tool-diagram.png)

O diagrama mostra o processo de um agente optando por usar a ferramenta personalizada:
1. Um usuário pergunta a um agente sobre as condições climáticas em uma estação de esqui.
2. O agente determina que ele tem acesso a uma ferramenta que pode usar uma API para obter informações meteorológicas e as chama.
3. A ferramenta retorna o relatório meteorológico e o agente informa o usuário.

### Cenários comuns para ferramentas personalizadas em agentes
As ferramentas personalizadas no Serviço do Agente de IA do Azure permitem que os usuários estendam os recursos dos agentes de IA, adaptando-os para atender às necessidades comerciais específicas. Alguns exemplos de casos de uso que ilustram a versatilidade e o impacto das ferramentas personalizadas incluem:

#### Automação de suporte ao cliente
- Cenário: uma empresa de varejo integra uma ferramenta personalizada que conecta o Agente de IA do Azure ao sistema crm (gerenciamento de relacionamento com o cliente).
- Funcionalidade: o agente de IA pode recuperar históricos de pedidos do cliente, processar reembolsos e fornecer atualizações em tempo real sobre status de envio.
- Resultado: resolução mais rápida de consultas de clientes, carga de trabalho reduzida para equipes de suporte e melhor satisfação do cliente.

#### Gerenciamento de inventário
- Cenário: uma empresa de fabricação desenvolve uma ferramenta personalizada para vincular o agente de IA ao sistema de gerenciamento de inventário.
- Funcionalidade: o agente de IA pode verificar os níveis de estoque, prever as necessidades de reabastecimento usando dados históricos e fazer pedidos com fornecedores automaticamente.
- Resultado: processos de inventário simplificados e operações otimizadas da cadeia de suprimentos.

#### Agendamento de consultas de saúde
- Cenário: um provedor de serviços de saúde integra uma ferramenta de agendamento personalizada com o agente de IA.
- Funcionalidade: o agente de IA pode acessar registros de pacientes, sugerir slots de compromisso disponíveis e enviar lembretes aos pacientes.
- Resultado: Redução da carga administrativa, melhor experiência do paciente e melhor utilização de recursos.

#### Suporte ao Helpdesk de TI
- Cenário: um departamento de TI desenvolve uma ferramenta personalizada para integrar o agente de IA com seus sistemas de base de dados de conhecimento e tíquetes.
- Funcionalidade: o agente de IA pode solucionar problemas técnicos comuns, escalonar problemas complexos e acompanhar os status dos tíquetes.
- Resultado: resolução de problemas mais rápida, tempo de inatividade reduzido e melhor produtividade dos funcionários.

#### E-learning e treinamento
- Cenário: uma instituição educacional cria uma ferramenta personalizada para conectar o agente de IA ao LMS (sistema de gerenciamento de aprendizagem).
- Funcionalidade: o agente de IA pode recomendar cursos, acompanhar o progresso dos alunos e responder a perguntas sobre o conteúdo do curso.
- Resultado: experiências de aprendizagem aprimoradas, maior engajamento dos alunos e tarefas administrativas simplificadas.

Esses exemplos demonstram como as ferramentas personalizadas dentro do Serviço de Agente de IA do Azure podem ser usadas entre setores para enfrentar desafios exclusivos, gerar eficiência e fornecer valor.

## Opções para implementar ferramentas personalizadas
Os serviços de IA do Azure fornecem várias opções de ferramentas personalizadas, incluindo ferramentas especificadas para OpenAPI, Azure Functions e chamada de função. Essas ferramentas permitem a integração perfeita com APIs externas, aplicativos controlados por eventos e funções personalizadas.

- Chamada de função: a chamada de função permite que você descreva a estrutura de funções personalizadas para um agente e retorne as funções que precisam ser chamadas junto com seus argumentos. O agente pode identificar dinamicamente as funções apropriadas com base em suas definições. Esse recurso é útil para integrar lógica personalizada e fluxos de trabalho, em uma seleção de linguagens de programação, em seus agentes de IA.
- Azure Functions: o Azure Functions permite criar aplicativos inteligentes controlados por eventos com sobrecarga mínima. Eles dão suporte a gatilhos e associações, que simplificam a interação dos Agentes de IA com sistemas e serviços externos. Os gatilhos determinam quando uma função é executada, enquanto as associações facilitam conexões simplificadas com fontes de dados de entrada ou saída.
- Ferramentas de especificação openAPI: essas ferramentas permitem que você conecte seu Agente de IA do Azure a uma API externa usando uma especificação do OpenAPI 3.0. Isso fornece integrações de API padronizadas, automatizadas e escalonáveis que aprimoram os recursos do seu agente. As especificações do OpenAPI descrevem APIs HTTP, permitindo que as pessoas entendam como uma API funciona, gerem código do cliente, criem testes e apliquem padrões de design.

Essa flexibilidade para integrar a funcionalidade personalizada de várias maneiras permite uma ampla gama de possibilidades de extensibilidade para seus agentes do Serviço do Agente de IA do Azure.

## Como integrar ferramentas personalizadas
Ferramentas personalizadas em um agente podem ser definidas de várias maneiras, dependendo do que funciona melhor para seu cenário. Você pode descobrir que sua empresa já tem o Azure Functions implementado para seu agente usar ou uma especificação pública do OpenAPI fornece ao agente a funcionalidade que você está procurando.

### Chamada de função
A chamada de função permite que os agentes executem funções predefinidas dinamicamente com base na entrada do usuário. Esse recurso é ideal para cenários em que os agentes precisam executar tarefas específicas, como recuperar dados ou processar consultas de usuário, e pode ser feito em código de dentro do agente. Sua função pode chamar outras APIs para obter informações adicionais ou iniciar um programa.

### Exemplo: Definir e usar uma função
Comece definindo uma função que o agente pode chamar. Por exemplo, aqui está uma função falsa de rastreamento de queda de neve:

```python
import json

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

Registre a função com seu agente usando o SDK de IA do Azure:

```python
# Initialize agent toolset with user functions
functions = FunctionTool(user_functions)
toolset = ToolSet()
toolset.add(functions)

# Create your agent with the toolset
agent = project_client.agents.create_agent(
    model="gpt-4o-mini",
    name="snowfall-agent",
    instructions="You are a weather assistant tracking snowfall. Use the provided functions to answer questions.",
    toolset={"functions": [recent_snowfall]}
)
```

O agente agora pode chamar recent_snowfall dinamicamente quando determina que o prompt requer informações que podem ser recuperadas pela função.

### Funções do Azure
O Azure Functions fornece recursos de computação sem servidor para processamento em tempo real. Essa integração é ideal para fluxos de trabalho controlados por eventos, permitindo que os agentes respondam a gatilhos como solicitações HTTP ou mensagens de fila.

#### Exemplo: usando o Azure Functions com um gatilho de fila
Primeiro, desenvolva e implante sua Função do Azure. Neste exemplo, imagine que temos uma função em nossa assinatura do Azure para buscar a queda de neve para um determinado local.

Quando a função do Azure estiver em vigor, integre-a à definição do agente como uma ferramenta de função do Azure:

```python
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
O agente agora pode enviar solicitações para a Função do Azure por meio de uma fila de armazenamento e processar os resultados.

### Especificação do OpenAPI
As ferramentas definidas pelo OpenAPI permitem que os agentes interajam com APIs externas usando especificações padronizadas. Essa abordagem simplifica a integração de API e garante a compatibilidade com vários serviços. O Serviço do Agente de IA do Azure usa ferramentas especificadas do OpenAPI 3.0.

#### Exemplo: usando uma especificação OpenAPI
Primeiro, crie um arquivo JSON ( neste exemplo, chamado snowfall_openapi.json) descrevendo a API.

```json
{
  "openapi": "3.0.0",
  "info": {
    "title": "Snowfall API",
    "version": "1.0.0"
  },
  "paths": {
    "/snow": {
      "get": {
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

Em seguida, registre a ferramenta OpenAPI na definição do agente:

```python
from azure.ai.projects.models import OpenApiTool, OpenApiAnonymousAuthDetails

with open("snowfall_openapi.json", "r") as f:
    openapi_spec = json.load(f)

auth = OpenApiAnonymousAuthDetails()
openapi_tool = OpenApiTool(name="snowfall_api", spec=openapi_spec, auth=auth)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini",
    name="openapi-agent",
    instructions="You are a snowfall tracking assistant. Use the API to fetch snowfall data.",
    tools=[openapi_tool]
)
```

O agente agora pode usar a ferramenta OpenAPI para buscar dados de queda de neve dinamicamente.

>Observação: Um dos conceitos relacionados a agentes e ferramentas personalizadas com as quais os desenvolvedores geralmente têm dificuldade é a natureza declarativa da solução. Você não precisa escrever um código que chame explicitamente suas funções de ferramenta personalizadas – o próprio agente decide chamar funções de ferramenta com base em mensagens em prompts. Ao fornecer ao agente funções que têm nomes significativos e parâmetros bem documentados, o agente pode "descobrir" quando e como chamar a função por si só!

Usando uma das opções de ferramenta personalizada disponíveis (ou qualquer combinação delas), você pode criar agentes avançados, flexíveis e inteligentes com o Serviço do Agente de IA do Azure. Essas integrações permitem a interação perfeita com sistemas externos, processamento em tempo real e fluxos de trabalho escalonáveis, facilitando a criação de soluções personalizadas adaptadas às suas necessidades.

## Resumo
Neste módulo, abordamos os benefícios de integrar ferramentas personalizadas ao Serviço do Agente de IA do Azure para aumentar a produtividade e fornecer soluções de negócios personalizadas. Ao fornecer ferramentas personalizadas ao nosso agente, podemos otimizar os processos para atender às necessidades específicas, resultando em melhores respostas do seu agente.

As técnicas aprendidas neste módulo permitem que as empresas gerem materiais de marketing, melhorem a comunicação e analisem tendências de mercado de forma mais eficaz, tudo por meio de ferramentas personalizadas. A integração de várias opções de ferramenta no Serviço do Agente de IA, do Azure Functions às especificações do OpenAPI, permite a criação de aplicativos inteligentes orientados a eventos que usam padrões bem estabelecidos já usados em muitas empresas.

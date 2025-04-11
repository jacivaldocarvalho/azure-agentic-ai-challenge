# Planejar e preparar-se para desenvolver soluções de IA no Azure

## Índice

- [Planejar e preparar-se para desenvolver soluções de IA no Azure](#planejar-e-preparar-se-para-desenvolver-soluções-de-ia-no-azure)
  - [Índice](#índice)
  - [Introdução](#introdução)
  - [O que é IA?](#o-que-é-ia)
  - [Serviços de IA do Azure](#serviços-de-ia-do-azure)
    - [Considerações sobre os recursos dos serviços de IA do Azure](#considerações-sobre-os-recursos-dos-serviços-de-ia-do-azure)
    - [Serviço único ou recurso de vários serviços?](#serviço-único-ou-recurso-de-vários-serviços)
    - [Disponibilidade regional](#disponibilidade-regional)
    - [Custo](#custo)
  - [Azure AI Foundry](#azure-ai-foundry)
    - [Hubs e projetos](#hubs-e-projetos)
    - [Centros](#centros)
    - [Projetos](#projetos)
    - [Considerações sobre o Azure AI Foundry](#considerações-sobre-o-azure-ai-foundry)
      - [Hub e organização do projeto](#hub-e-organização-do-projeto)
      - [Recursos conectados](#recursos-conectados)
      - [Segurança e autorização](#segurança-e-autorização)
      - [Disponibilidade regional](#disponibilidade-regional-1)
      - [Custos e cotas](#custos-e-cotas)
  - [Ferramentas de desenvolvedor e SDKs](#ferramentas-de-desenvolvedor-e-sdks)
    - [Ferramentas e ambientes de desenvolvimento](#ferramentas-e-ambientes-de-desenvolvimento)
    - [A imagem de contêiner do VS Code do Azure AI Foundry](#a-imagem-de-contêiner-do-vs-code-do-azure-ai-foundry)
    - [GitHub e GitHub Copilot](#github-e-github-copilot)
    - [Linguagens de programação, APIs e SDKs](#linguagens-de-programação-apis-e-sdks)
  - [IA responsável](#ia-responsável)
    - [Imparcialidade](#imparcialidade)
    - [Confiabilidade e segurança](#confiabilidade-e-segurança)
    - [Privacidade e segurança](#privacidade-e-segurança)
    - [Inclusão](#inclusão)
    - [Transparência](#transparência)
    - [Responsabilidade](#responsabilidade)
  - [Resumo](#resumo)
  
## Introdução
O crescimento do uso de IA (inteligência artificial) em geral e gerativo IA, em particular, significa que os desenvolvedores são cada vez mais obrigados a criar soluções abrangentes de IA. Essas soluções precisam combinar modelos de machine learning, serviços de IA, soluções de engenharia de prompt e código personalizado.

O Microsoft Azure fornece vários serviços que você pode usar para criar soluções de IA. No entanto, antes de embarcar em um projeto de desenvolvimento de aplicativos de IA, é útil considerar as opções disponíveis para serviços, ferramentas e estruturas, bem como alguns princípios e práticas que podem ajudá-lo a ter sucesso.

Este módulo explora algumas das principais considerações para planejar um projeto de desenvolvimento de IA e apresenta do Azure AI Foundry; uma plataforma abrangente para desenvolvimento de IA no Microsoft Azure.

## O que é IA?
O termo "IA" (Inteligência Artificial) abrange uma ampla gama de recursos de software que permitem que os aplicativos exponham comportamentos semelhantes a humanos. A IA existe há muitos anos, e sua definição variou à medida que os casos de tecnologia e uso associados a ela evoluíram. No cenário tecnológico atual, as soluções de IA são baseadas no aprendizado de máquina modelos que encapsulam relações semânticas encontradas em grandes quantidades de dados; permitindo que os aplicativos apareçam para interpretar a entrada em vários formatos, raciocinar sobre os dados de entrada e gerar as respostas e previsões apropriadas.

Os recursos comuns de IA que os desenvolvedores podem integrar em um aplicativo de software incluem:

| Capacidade                         | Descrição |
|------------------------------------|-----------|
| **IA Generativa**                    | A capacidade de gerar respostas originais para o idioma natural solicitado. Por exemplo, o software para uma empresa imobiliária pode ser usado para gerar automaticamente descrições de propriedade e cópia de publicidade para uma listagem de propriedades. |
| **Agentes**                        | Aplicativos de IA generativos que podem responder à entrada do usuário ou avaliar situações de forma autônoma e tomar as medidas apropriadas. Por exemplo, um agente "assistente executivo" pode fornecer detalhes sobre o local de uma reunião em seu calendário ou até mesmo anexar um mapa ou automatizar a reserva de um serviço de táxi ou rideshare para ajudá-lo a chegar lá. |
| **Visão Computacional** | A capacidade de aceitar, interpretar e processar a entrada visual de imagens, vídeos e fluxos de câmera ao vivo. Por exemplo, um check-out automatizado em um supermercado pode usar a pesquisa visual computacional para identificar quais produtos um cliente tem em sua cesta de compras, eliminando a necessidade de verificar um código de barras ou inserir manualmente o produto e a quantidade. |
| **Fala**                           | A capacidade de reconhecer e sintetizar fala. Por exemplo, um assistente digital pode permitir que os usuários façam perguntas ou forneçam instruções audíveis falando em um microfone e gerem saída falada para fornecer respostas ou confirmações. |
| **Processamento de Linguagem Natural** | A capacidade de processar a linguagem natural em forma escrita ou falada, analisá-la, identificar pontos-chave e gerar resumos ou categorizações. Por exemplo, um aplicativo de marketing pode analisar mensagens de mídia social que mencionam uma determinada empresa, convertê-las em um idioma específico e categorizá-las como positivas ou negativas com base na análise de sentimento. |
| **Extração de Informações**       | A capacidade de usar a visão computacional, a fala e o processamento de linguagem natural para extrair informações importantes de documentos, formulários, imagens, gravações e outros tipos de conteúdo. Por exemplo, um aplicativo automatizado de processamento de declarações de despesas pode extrair datas de compra, detalhes de item de linha individuais e custos totais de um recibo verificado. |
| **Suporte à Decisão**             | A capacidade de usar dados históricos e correlações aprendidas para fazer previsões que dão suporte à tomada de decisões de negócios. Por exemplo, analisando fatores demográficos e econômicos em uma cidade para prever tendências do mercado imobiliário que informam as decisões de preços de propriedades. |

Determinar os recursos específicos de IA que você deseja incluir em seu aplicativo pode ajudá-lo a identificar os serviços de IA mais apropriados que você precisará provisionar, configurar e usar em sua solução.

## Serviços de IA do Azure
O Microsoft Azure fornece uma ampla gama de serviços de nuvem que você pode usar para desenvolver, implantar e gerenciar uma solução de IA. O ponto de partida mais óbvio para considerar o desenvolvimento de IA no Azure são os serviços de IA do Azure; um conjunto de APIs e modelos predefinidos prontos para uso que você pode integrar aos seus aplicativos. A tabela a seguir lista alguns serviços de IA do Azure comumente usados (para obter uma lista completa de todos os serviços de IA do Azure disponíveis, [consulte serviços de IA do Azure disponíveis](https://learn.microsoft.com/pt-br/azure/ai-services/what-are-ai-services#available-azure-ai-services?azure-portal=true)).

| Serviço | Descrição |
|---------|-----------|
| **Azure OpenAI** | O serviço Azure OpenAI fornece acesso a modelos de IA generativos OpenAI, incluindo a família GPT de modelos de linguagem grandes e pequenos e modelos DALL-E de geração de imagem, em um serviço de nuvem escalonável e seguro no Azure. |
| **Visão de IA do Azure** | O serviço Azure AI Vision fornece um conjunto de modelos e APIs que você pode usar para implementar funcionalidades de pesquisa visual computacional em um aplicativo. Ele permite detectar objetos em imagens, gerar legendas e descrições e ler texto em imagens. |
| **Fala de IA do Azure** | O serviço de Fala de IA do Azure fornece APIs para conversão de texto em fala, fala em texto, além de recursos como reconhecimento de alto-falante e tradução de voz. |
| **Linguagem de IA do Azure** | O serviço de Linguagem de IA do Azure oferece modelos e APIs para analisar texto em linguagem natural, executar tarefas como extração de entidades, análise de sentimento e resumo, além de criar modelos de linguagem de conversação e respostas a perguntas. |
| **Segurança de Conteúdo da IA do Azure** | Esse serviço fornece algoritmos avançados para processar imagens e textos e identificar conteúdo potencialmente ofensivo, arriscado ou indesejado. |
| **Tradutor de IA do Azure** | Usa modelos de linguagem avançados para traduzir texto entre uma ampla variedade de idiomas. |
| **Detecção Facial da IA do Azure** | Serviço especializado em pesquisa visual computacional para detectar, analisar e reconhecer rostos humanos. Devido aos riscos de identificação pessoal, alguns recursos são restritos a clientes aprovados. |
| **Visão Personalizada de IA do Azure** | Permite treinar e usar modelos personalizados de visão computacional para classificação de imagens e detecção de objetos. |
| **IA do Azure para Informação de Documentos** | Com o Azure AI Document Intelligence, é possível usar modelos prontos ou personalizados para extrair campos de documentos complexos, como faturas, recibos e formulários. |
| **Compreensão de Conteúdo de IA do Azure** | Fornece recursos de análise de conteúdo multimodal para extrair dados de formulários, documentos, imagens, vídeos e fluxos de áudio. |
| **Azure AI Search** | Usa um pipeline de habilidades de IA e código personalizado para extrair informações de conteúdo e criar um índice pesquisável. Pode ser utilizado para criar índices vetoriais usados em prompts para modelos de linguagem generativos, como os do Azure OpenAI. |

### Considerações sobre os recursos dos serviços de IA do Azure
Para usar os serviços de IA do Azure, crie um ou mais recursos de IA do Azure em uma assinatura do Azure e implemente código em aplicativos cliente para consumi-los. Em alguns casos, os serviços de IA incluem interfaces visuais baseadas na Web que você pode usar para configurar e testar seus recursos , por exemplo, para treinar um modelo de classificação de imagem personalizado usando o serviço da Visão Personalizada, você pode usar a interface visual para carregar imagens de treinamento, gerenciar trabalhos de treinamento e implantar o modelo resultante.


>**Observação**
Você pode provisionar recursos dos serviços de IA do Azure no portal do Azure (ou usando modelos BICEP ou ARM ou a interface de linha de comando do Azure) e criar aplicativos que os usam diretamente por meio de várias APIs e SDKs específicas do serviço. No entanto, como discutiremos mais adiante neste módulo, na maioria dos cenários de desenvolvimento de médio a grande escala, é melhor provisionar recursos de serviços de IA do Azure como parte de um hub do Azure Foundry - permitindo que você centralize o controle de acesso e o gerenciamento de custos e facilitando o gerenciamento do uso de recursos compartilhados com base no desenvolvimento de IA projetos.

### Serviço único ou recurso de vários serviços?
A maioria dos serviços de IA do Azure, como Azure AI Vision, de Linguagem de IA do Azure e assim por diante, pode ser provisionada como recursos autônomos, permitindo que você crie apenas os recursos do Azure de que você precisa especificamente. Além disso, os serviços autônomos de IA do Azure geralmente incluem um SKU de camada livre com funcionalidade limitada, permitindo que você avalie e desenvolva com o serviço sem custo. Cada recurso autônomo de IA do Azure fornece um ponto de extremidade e chaves de autorização que você pode usar para acessá-lo com segurança de um aplicativo cliente.

Como alternativa, você pode provisionar um recurso serviços de IA do Azure de vários serviços que encapsula os seguintes serviços em um único recurso do Azure:

- Azure OpenAI
- Fala IA do Azure
- Visão de IA do Azure
- Idioma de IA do Azure
- Segurança de conteúdo de IA do Azure
- Tradutor de IA do Azure
- Inteligência Artificial de Documentos do Azure
- Compreensão de conteúdo de IA do Azure

O uso de um recurso de vários serviços pode facilitar o gerenciamento de aplicativos que usam vários recursos de IA.

### Disponibilidade regional
Alguns serviços e modelos estão disponíveis apenas em um subconjunto de regiões do Azure. Considere a disponibilidade do serviço e quaisquer restrições de cota regional para sua assinatura ao provisionar serviços de IA do Azure. Use a tabela de disponibilidade do produto para verificar a disponibilidade regional dos serviços do Azure. Use a [tabela de disponibilidade](https://azure.microsoft.com/pt-br/explore/global-infrastructure/products-by-region/table) do modelo na documentação do serviço Azure OpenAI para determinar a disponibilidade regional para modelos do Azure OpenAI.

### Custo
Os serviços de IA do Azure são cobrados com base no uso, com diferentes esquemas de preços disponíveis dependendo dos serviços específicos que estão sendo usados. Ao planejar uma solução de IA no Azure, use a documentação preços dos serviços de IA do Azure para entender os [preços dos serviços de IA](https://azure.microsoft.com/pt-br/pricing/details/cognitive-services/) que você pretende incorporar ao seu aplicativo. Você pode usar a [calculadora de preços do Azure](https://azure.microsoft.com/pt-br/pricing/calculator/) para estimar os custos que seu uso esperado incorrerá.

## Azure AI Foundry
O Azure AI Foundry é uma plataforma para desenvolvimento de IA no Microsoft Azure. Embora você possa provisionar recursos individuais dos serviços de IA do Azure e criar aplicativos que os consomem sem ele, a organização do projeto, o gerenciamento de recursos e os recursos de desenvolvimento de IA do Azure AI Foundry torna a maneira recomendada de criar todas as soluções menos simples.

O Azure AI Foundry fornece o portal do Azure AI Foundry, uma interface visual baseada na Web para trabalhar com projetos de IA. Ele também fornece o SDK do Azure AI Foundry, que você pode usar para criar soluções de IA programaticamente.

### Hubs e projetos
No Azure AI Foundry, você gerencia os recursos, os ativos, o código e outros elementos da solução de IA em hubs e projetos. Hubs fornecem um contêiner de nível superior para gerenciar recursos compartilhados, dados, conexões e configuração de segurança para o desenvolvimento de aplicativos de IA. Um hub pode dar suporte a vários projetos , nos quais os desenvolvedores colaboram na criação de uma solução específica.

### Centros
Um hub fornece uma coleção gerenciada centralmente de recursos compartilhados e configuração de gerenciamento para desenvolvimento de solução de IA. Você precisa de pelo menos um hub para usar todos os recursos e funcionalidades de desenvolvimento de solução do AI Foundry.

![Gerenciado central de um hub](https://learn.microsoft.com/pt-br/training/wwl-data-ai/prepare-azure-ai-development/media/ai-foundry-hub.png)

Em um hub, você pode definir recursos compartilhados a serem usados em vários projetos. Quando você cria um hub usando o portal do Azure AI Foundry, um recurso Hub de IA do Azure do Azure é criado em um grupo de recursos associado ao hub. Além disso, os seguintes recursos são criados para o hub:

- Um serviço de IA do Azure recurso para fornecer acesso ao Azure OpenAI e a outros serviços de IA do Azure.
- Um cofre de chaves em que dados confidenciais, como conexões e credenciais, podem ser armazenados com segurança.
- Uma conta de Armazenamento para dados usados no hub e em seus projetos.
- Opcionalmente, um recurso do Azure AI Search que pode ser usado para indexar dados e dar suporte ao aterramento para prompts de IA generativos.

Você pode criar mais recursos conforme necessário (por exemplo, um recurso face de IA do Azure) e adicioná-lo ao hub (ou a um projeto individual) definindo um recurso conectado . À medida que você cria mais itens em seu hub, como instâncias de computação ou pontos de extremidade, mais recursos serão criados para eles no grupo de recursos do Azure.

O acesso aos recursos em um hub é regido pela criação usuários e atribuição a funções. Um administrador de TI pode gerenciar o acesso aos recursos centralmente no nível do hub e os projetos associados ao hub herdam os recursos e as atribuições de função; permitindo que as equipes de desenvolvimento usem os recursos necessários sem a necessidade de solicitar acesso em uma base projeto por projeto.

### Projetos
Um hub pode dar suporte a um ou mais projetos, cada um deles usado para organizar os recursos e ativos necessários para um determinado esforço de desenvolvimento de IA.

![Página de um projeto no Azure AI Foundry](https://learn.microsoft.com/pt-br/training/wwl-data-ai/prepare-azure-ai-development/media/ai-foundry-project.png)

Os usuários podem colaborar em um projeto, compartilhando dados em contêineres de armazenamento específicos do projeto e recursos conectados e usando os recursos compartilhados definidos no hub associado ao projeto. O Azure AI Foundry fornece ferramentas e funcionalidades em um projeto que os desenvolvedores podem usar para criar soluções de IA com eficiência, incluindo:

- Um catálogo de modelos em que você pode encontrar e implantar modelos de machine learning de várias fontes, incluindo o Azure OpenAI e a biblioteca de modelos de Detecção Facial.
- Playgrounds em que você pode testar prompts com modelos de IA generativos.
- Acesso a serviços de IA do Azure, incluindo interfaces visuais para experimentar e configurar serviços, bem como pontos de extremidade e chaves que você pode usar para se conectar a eles a partir de aplicativos cliente.
- o Visual Studio Code contêineres que definem um ambiente de desenvolvimento hospedado no qual você pode escrever, testar e implantar código.
- funcionalidade de ajuste fino para modelos de IA generativos que você precisa personalizar com base em prompts e respostas de treinamento personalizados.
- de Fluxo de Prompt, uma ferramenta de orquestração de prompt que você pode usar para definir a lógica para a interação de um aplicativo de IA gerador com um modelo.
- Ferramentas para avaliar, avaliar e melhorar seus aplicativos de IA, incluindo de rastreamento, avaliações e gerenciamento de de segurança e segurança de conteúdo.
- O gerenciamento de ativos do projeto, incluindo modelos e pontos de extremidade, dados e índices e aplicativos Web implantados.

### Considerações sobre o Azure AI Foundry
Ao planejar uma solução de IA baseada no Azure AI Foundry, há algumas considerações adicionais para aquelas discutidas anteriormente em relação aos serviços de IA do Azure.

#### Hub e organização do projeto
Planeje o hub e a organização do projeto para o gerenciamento mais eficaz de recursos e a eficiência da administração. Use hubs para centralizar o gerenciamento de usuários e recursos compartilhados envolvidos em projetos relacionados e, em seguida, adicionar recursos específicos do projeto conforme necessário. Por exemplo, uma organização pode ter equipes de desenvolvimento de software separadas para cada área do negócio, portanto, pode fazer sentido criar hubs separados para cada área de negócios (como Marketing, RH e assim por diante) em que projetos de desenvolvimento de aplicativos de IA para cada área de negócios podem ser criados. Os recursos compartilhados em cada hub estarão automaticamente disponíveis em projetos criados nesses hubs.

>Dica
Para obter mais informações sobre hubs e projetos, consulte [Gerenciar, colaborar e organizar com hubs.](https://learn.microsoft.com/pt-br/azure/ai-foundry/concepts/ai-resources)

#### Recursos conectados
No nível do hub, um administrador de TI pode criar conexões de recursos compartilhados em um hub que será usado em projetos downstream. Os projetos acessam os recursos conectados por proxy em nome dos usuários do projeto, para que os usuários nesses projetos não precisem de acesso direto a esses recursos para usá-los no contexto do projeto. As conexões em um hub estão automaticamente disponíveis em novos projetos no hub sem solicitações adicionais para o administrador de TI. Se um projeto individual precisar de acesso a um recurso específico que outros projetos no mesmo hub não usam, você poderá criar mais recursos conectados no nível do projeto.

Ao planejar seus projetos e hubs do Azure AI Foundry, identifique os recursos conectados compartilhados que você deve adicionar a cada hub para que eles sejam herdados por projetos nesse hub, permitindo exceções no nível do projeto.

>Dica
Para obter mais informações sobre recursos conectados, consulte [Conexões no portal do Azure AI Foundry](https://learn.microsoft.com/pt-br/azure/ai-foundry/concepts/connections).

#### Segurança e autorização
Para cada hub e projeto, identifique os usuários que precisarão de acesso e as funções às quais eles devem ser atribuídos.

As funções no nível do hub podem executar tarefas de gerenciamento de infraestrutura, como a criação de recursos conectados no nível do hub ou novos projetos. As funções padrão em um hub são:

- Proprietário: acesso total ao hub, incluindo a capacidade de gerenciar e criar novos hubs e atribuir permissões. Essa função é atribuída automaticamente ao criador do hub.
- Colaborador: acesso total ao hub, incluindo a capacidade de criar novos hubs, mas não é capaz de gerenciar permissões de hub no recurso existente.
- do Desenvolvedor de IA do Azure: todas as permissões, exceto criar novos hubs e gerenciar as permissões do hub.
- operador de implantação de inferência de IA do Azure: todas as permissões necessárias para criar uma implantação de recurso em um grupo de recursos.
- Leitor: acesso somente leitura ao hub. Essa função é atribuída automaticamente a todos os membros do projeto dentro do recurso de IA do Azure.

As funções no nível do projeto determinam as tarefas que um usuário pode executar em um projeto individual. As funções padrão em um projeto são:

- Proprietário: acesso total ao projeto, incluindo a capacidade de atribuir permissões aos usuários do projeto.
- Colaborador: acesso total ao projeto, mas não pode atribuir permissões aos usuários do projeto.
- desenvolvedor de IA do Azure: permissões para executar a maioria das ações, incluindo a criação de implantações, mas não pode atribuir permissões aos usuários do projeto.
- operador de implantação de inferência de IA do Azure: permissões para executar todas as ações necessárias para criar uma implantação de recurso em um grupo de recursos.
- Leitor: acesso somente leitura ao projeto.

>Dica
Para obter mais informações sobre como gerenciar funções em hubs e projetos do Azure AI Foundry, consulte [controle de acesso baseado em função no portal do Azure AI Foundry](https://learn.microsoft.com/pt-br/azure/ai-foundry/concepts/rbac-azure-ai-foundry).

#### Disponibilidade regional
ara obter mais informações sobre a disponibilidade regional do Azure AI Foundry, consulte [disponibilidade de recursos do Azure AI Foundry entre regiões de nuvens](https://learn.microsoft.com/pt-br/azure/ai-foundry/reference/region-support).

#### Custos e cotas
Além do custo dos serviços de IA do Azure que sua solução usa, há custos associados ao Azure AI Foundry relacionados aos recursos que dão suporte a hubs e projetos, bem como armazenamento e computação para ativos, desenvolvimento e soluções implantadas. Você deve considerar esses custos ao planejar o uso do Azure AI Foundry para desenvolvimento de solução de IA.

Além dos custos de consumo do serviço, você deve considerar as cotas de recursos necessárias para dar suporte aos aplicativos de IA que pretende criar. As cotas são usadas para limitar a utilização e desempenham um papel fundamental no gerenciamento de custos e no gerenciamento da capacidade do Azure. Em alguns casos, talvez seja necessário solicitar cota adicional para aumentar os limites de taxa para operações de modelo de IA ou computação disponível para desenvolvimento e implantação de solução.

>Dica
Para obter mais informações sobre como planejar e gerenciar custos para o Azure AI Foundry, consulte [Planejar e gerenciar custos para o Azure AI Foundry](https://learn.microsoft.com/pt-br/azure/ai-foundry/how-to/costs-plan-manage). Para obter mais informações sobre como gerenciar a cota do Azure AI Foundry, consulte [Gerenciar e aumentar as cotas para recursos com o Azure AI Foundry](https://learn.microsoft.com/pt-br/azure/ai-foundry/how-to/quota).

## Ferramentas de desenvolvedor e SDKs
Embora você possa executar muitas das tarefas necessárias para desenvolver uma solução de IA diretamente no portal do Azure AI Foundry, os desenvolvedores também precisam escrever, testar e implantar código.

### Ferramentas e ambientes de desenvolvimento
Há muitas ferramentas de desenvolvimento e ambientes disponíveis, e os desenvolvedores devem escolher um que dê suporte aos idiomas, SDKs e APIs com os quais precisam trabalhar e com os quais estão mais confortáveis. Por exemplo, um desenvolvedor que se concentra fortemente na criação de aplicativos para Windows usando o .NET Framework pode preferir trabalhar em um IDE (ambiente de desenvolvimento integrado) como o Microsoft Visual Studio. Por outro lado, um desenvolvedor de aplicativos Web que trabalha com uma ampla variedade de linguagens e bibliotecas de software livre pode preferir usar um editor de código como o VS Code (Visual Studio Code). Ambos os produtos são adequados para o desenvolvimento de aplicativos de IA no Azure.

### A imagem de contêiner do VS Code do Azure AI Foundry
Como alternativa para instalar e configurar seu próprio ambiente de desenvolvimento, no portal do Azure AI Foundry, você pode criar computação e usá-lo para hospedar uma imagem de contêiner para o VS Code (instalado localmente ou como um aplicativo Web hospedado em um navegador). O benefício de usar a imagem de contêiner é que ela inclui as versões mais recentes dos pacotes do SDK com as quais você provavelmente trabalhará ao criar aplicativos de IA com o Azure AI Foundry.

![Vscode versão web](https://learn.microsoft.com/pt-br/training/wwl-data-ai/prepare-azure-ai-development/media/vs-code.png)

>Dica
Para obter mais informações sobre como usar a imagem de contêiner do VS Code no portal do Azure AI Foundry, consulte [Introdução aos projetos do Azure AI Foundry no VS Code](https://learn.microsoft.com/pt-br/azure/ai-foundry/how-to/develop/vscode).

### GitHub e GitHub Copilot
O GitHub é a plataforma mais popular do mundo para controle do código-fonte e gerenciamento de DevOps e pode ser um elemento crítico de qualquer esforço de desenvolvimento de equipe. O Visual Studio e o VS Code (incluindo a imagem de contêiner do VS Code do Azure AI Foundry) fornecem integração nativa com o GitHub e acesso ao GitHub Copilot; um assistente de IA que pode melhorar significativamente a produtividade e a eficácia do desenvolvedor.

### Linguagens de programação, APIs e SDKs
Você pode desenvolver aplicativos de IA usando muitas linguagens e estruturas de programação comuns, incluindo Microsoft C#, Python, Node, TypeScript, Java e outros. Ao criar soluções de IA no Azure, alguns SDKs comuns que você deve planejar para instalar e usar incluem:

- [O SDK do Azure AI Foundry](https://learn.microsoft.com/pt-br/azure/ai-foundry/how-to/develop/sdk-overview?tabs=sync&pivots=programming-language-python), que permite que você escreva código para se conectar a projetos do Azure AI Foundry e acessar conexões de recursos, com as quais você pode trabalhar usando SDKs específicos do serviço.
- [SDKs dos Serviços de IA do Azure](https://learn.microsoft.com/pt-br/azure/ai-services/reference/sdk-package-resources?pivots=programming-language-csharp) – bibliotecas específicas do serviço de IA para várias linguagens de programação e estruturas que permitem consumir recursos dos Serviços de IA do Azure em sua assinatura. Você também pode usar os Serviços de IA do Azure por meio de suas APIs REST.

- O do Serviço do Agente de IA do Azure, que é acessado por meio do SDK do Azure AI Foundry e pode ser integrado a estruturas como [AutoGen](https://microsoft.github.io/autogen/0.2/docs/Getting-Started/) e [kernel semântico](https://learn.microsoft.com/pt-br/semantic-kernel/overview/) para criar soluções abrangentes de agente de IA.
- O O [Fluxo de Prompt SDK](https://microsoft.github.io/promptflow/index.html), que você pode usar para implementar a lógica de orquestração para gerenciar interações de prompt com modelos de IA generativos.

## IA responsável
É importante que os engenheiros de software considerem o impacto de seus softwares nos usuários e na sociedade em geral; incluindo considerações sobre seu uso responsável. Quando o aplicativo é imbuido com inteligência artificial, essas considerações são particularmente importantes devido à natureza de como os sistemas de IA funcionam e informam decisões; geralmente com base em modelos probabilísticos, que, por sua vez, dependem dos dados com os quais foram treinados.

A natureza humana das soluções de IA é um benefício significativo em tornar os aplicativos amigáveis, mas também pode levar os usuários a confiar muito na capacidade do aplicativo de tomar decisões corretas. O potencial de danos a indivíduos ou grupos por meio de previsões incorretas ou uso indevido de recursos de IA é uma grande preocupação, e os engenheiros de software que criam soluções habilitadas para IA devem aplicar a devida consideração para mitigar os riscos e garantir a imparcialidade, a confiabilidade e a proteção adequada contra danos ou discriminação.

Vamos discutir alguns princípios fundamentais para a IA responsável que foram adotados na Microsoft.

### Imparcialidade
Os sistemas de IA devem tratar todas as pessoas de forma justa. Por exemplo, suponha que você crie um modelo de machine learning para dar suporte a um aplicativo de aprovação de empréstimo para um banco. O modelo deve fazer previsões de se o empréstimo deve ou não ser aprovado sem incorporar qualquer viés baseado em gênero, etnia ou outros fatores que possam resultar em uma vantagem ou desvantagem injusta para grupos específicos de candidatos.

A imparcialidade dos sistemas de aprendizado de máquina é uma área altamente ativa de pesquisa em andamento, e existem algumas soluções de software para avaliar, quantificar e atenuar a injustiça em modelos aprendidos por máquina. No entanto, as ferramentas por si só não são suficientes para garantir a imparcialidade. Considere a imparcialidade desde o início do processo de desenvolvimento de aplicativos; examinar cuidadosamente os dados de treinamento para garantir que eles sejam representativos de todos os assuntos potencialmente afetados e avaliar o desempenho preditivo para subseções da população de usuários durante todo o ciclo de vida de desenvolvimento.

### Confiabilidade e segurança
Os sistemas de IA devem ser executados de forma confiável e segura. Por exemplo, considere um sistema de software baseado em IA para um veículo autônomo; ou um modelo de machine learning que diagnostica sintomas do paciente e recomenda prescrições. A não confiabilidade nesses tipos de sistema pode resultar em um risco substancial para a vida humana.

Assim como acontece com qualquer software, o desenvolvimento de aplicativos de software baseado em IA deve ser submetido a testes rigorosos e processos de gerenciamento de implantação para garantir que eles funcionem conforme o esperado antes do lançamento. Além disso, os engenheiros de software precisam levar em conta a natureza probabilística dos modelos de machine learning e aplicar limites apropriados ao avaliar as pontuações de confiança para previsões.

### Privacidade e segurança
Os sistemas de IA devem ser seguros e respeitar a privacidade. Os modelos de machine learning nos quais os sistemas de IA são baseados dependem de grandes volumes de dados, que podem conter detalhes pessoais que devem ser mantidos privados. Mesmo depois que os modelos são treinados e o sistema está em produção, eles usam novos dados para fazer previsões ou tomar medidas que podem estar sujeitas a questões de privacidade ou segurança; portanto, as proteções apropriadas para proteger os dados e o conteúdo do cliente devem ser implementadas.

### Inclusão
Os sistemas de IA devem capacitar todos e envolver as pessoas. A IA deve trazer benefícios para todas as partes da sociedade, independentemente da capacidade física, gênero, orientação sexual, etnia ou outros fatores.

Uma maneira de otimizar a inclusão é garantir que o design, o desenvolvimento e o teste do aplicativo incluam a entrada de um grupo de pessoas o mais diversificado possível.

### Transparência
Os sistemas de IA devem ser compreensíveis. Os usuários devem estar totalmente cientes da finalidade do sistema, como ele funciona e quais limitações podem ser esperadas.

Por exemplo, quando um sistema de IA é baseado em um modelo de machine learning, você geralmente deve conscientizar os usuários sobre fatores que podem afetar a precisão de suas previsões, como o número de casos usados para treinar o modelo ou os recursos específicos que têm mais influência sobre suas previsões. Você também deve compartilhar informações sobre a pontuação de confiança para previsões.

Quando um aplicativo de IA depende de dados pessoais, como um sistema de reconhecimento facial que usa imagens de pessoas para reconhecê-los; você deve deixar claro para o usuário como seus dados são usados e retidos e quem tem acesso a eles.

### Responsabilidade
As pessoas devem ser responsáveis por sistemas de IA. Embora muitos sistemas de IA pareçam operar de forma autônoma, em última análise, é responsabilidade dos desenvolvedores que treinaram e validaram os modelos usados e definiram a lógica que baseia as decisões em previsões de modelo para garantir que o sistema geral atenda aos requisitos de responsabilidade. Para ajudar a cumprir essa meta, os designers e desenvolvedores da solução baseada em IA devem trabalhar dentro de uma estrutura de governança e princípios organizacionais que garantam que a solução atenda aos padrões responsáveis e legais claramente definidos.

## Resumo
Neste módulo, você explorou algumas das principais considerações ao planejar e se preparar para o desenvolvimento de aplicativos de IA. Você também teve a oportunidade de se familiarizar com o Azure AI Foundry, a plataforma recomendada para desenvolver soluções de IA no Azure.

>Dica
Para obter as últimas notícias e informações sobre o desenvolvimento de aplicativos de IA no Azure, consulte [IA do Azure](https://azure.microsoft.com/pt-br/solutions/ai).
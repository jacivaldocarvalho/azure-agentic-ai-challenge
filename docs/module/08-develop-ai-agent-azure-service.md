# Desenvolver um agente de IA com o Serviço do Agente de IA do Azure
> Este módulo fornece aos engenheiros as habilidades para começar a criar agentes com o Serviço de Agente de IA do Azure.


## Índice

- [Desenvolver um agente de IA com o Serviço do Agente de IA do Azure](#desenvolver-um-agente-de-ia-com-o-serviço-do-agente-de-ia-do-azure)
  - [Índice](#índice)
  - [Introdução](#introdução)
  - [O que é um agente de IA](#o-que-é-um-agente-de-ia)
    - [Por que os agentes de IA são úteis?](#por-que-os-agentes-de-ia-são-úteis)
    - [Exemplos de casos de uso do agente de IA](#exemplos-de-casos-de-uso-do-agente-de-ia)
      - [Agentes de produtividade pessoal](#agentes-de-produtividade-pessoal)
      - [Agentes de pesquisa](#agentes-de-pesquisa)
      - [Agentes de vendas](#agentes-de-vendas)
      - [Agentes de atendimento ao cliente](#agentes-de-atendimento-ao-cliente)
      - [Agentes do desenvolvedor](#agentes-do-desenvolvedor)
  - [Como usar o Serviço do Agente de IA do Azure](#como-usar-o-serviço-do-agente-de-ia-do-azure)
    - [Finalidade do Serviço do Agente de IA do Azure](#finalidade-do-serviço-do-agente-de-ia-do-azure)
    - [Principais recursos do Serviço do Agente de IA do Azure](#principais-recursos-do-serviço-do-agente-de-ia-do-azure)
    - [Recursos do Serviço do Agente de IA do Azure](#recursos-do-serviço-do-agente-de-ia-do-azure)
  - [Desenvolver agentes com o Serviço do Agente de IA do Azure](#desenvolver-agentes-com-o-serviço-do-agente-de-ia-do-azure)
    - [Desenvolvendo aplicativos que usam agentes](#desenvolvendo-aplicativos-que-usam-agentes)
    - [Ferramentas disponíveis para seu agente](#ferramentas-disponíveis-para-seu-agente)
  - [Ferramentas de conhecimento](#ferramentas-de-conhecimento)
  - [Ferramentas de ação](#ferramentas-de-ação)
  - [Resumo](#resumo)

## Introdução
O Serviço de Agente de IA do Azure é um serviço totalmente gerenciado projetado para capacitar os desenvolvedores a criar, implantar e dimensionar com segurança agentes de IA extensíveis e de alta qualidade sem a necessidade de gerenciar os recursos de computação e armazenamento subjacentes.

Imagine que você está trabalhando no setor de saúde, onde há a necessidade de automatizar as interações dos pacientes e simplificar as tarefas administrativas. Sua organização deseja desenvolver um agente de IA que possa lidar com consultas de pacientes, agendar consultas e fornecer informações médicas com base em dados em tempo real. No entanto, gerenciar a infraestrutura e garantir a segurança de dados são desafios significativos. O Serviço de Agente de IA do Azure oferece uma solução, permitindo que você crie agentes de IA adaptados às suas necessidades por meio de instruções personalizadas e ferramentas avançadas. Esse serviço simplifica o processo de desenvolvimento, reduz a quantidade de código necessária e gerencia a infraestrutura subjacente, permitindo que você se concentre na criação de soluções de IA de alta qualidade.

Neste módulo, você aprenderá a usar o Serviço do Agente de IA do Azure para desenvolver agentes.

## O que é um agente de IA

Um agente de IA é um serviço de software que usa IA generativa para entender e executar tarefas em nome de um usuário ou de outro programa. Esses agentes usam modelos avançados de IA para entender o contexto, tomar decisões, utilizar dados de aterramento e tomar ações para alcançar metas específicas. Ao contrário dos aplicativos tradicionais, os agentes de IA podem operar de forma independente, executando fluxos de trabalho complexos e automatizando processos sem a necessidade de intervenção humana constante. A evolução da IA generativa permite que os agentes se comportem de forma inteligente em nosso nome, transformando como podemos usar e integrar esses agentes.

Entender o que é um agente de IA e como utilizá-los é crucial para usar efetivamente a IA para automatizar tarefas, tomar decisões informadas e aprimorar as experiências do usuário. Esse conhecimento permite que as organizações implantem agentes de IA estrategicamente, maximizando seu potencial para impulsionar a inovação, melhorar a eficiência e alcançar objetivos de negócios.

### Por que os agentes de IA são úteis?

Os agentes de IA são incrivelmente úteis por vários motivos:

- Automação de tarefas de rotina: os agentes de IA podem lidar com tarefas repetitivas e mundanas, liberando trabalhadores humanos para se concentrarem em atividades mais estratégicas e criativas. Isso leva ao aumento da produtividade e da eficiência.
- Tomada de decisão aprimorada: ao processar grandes quantidades de dados e fornecer insights, os agentes de IA dão suporte a uma melhor tomada de decisão. Eles podem analisar tendências, prever resultados e oferecer recomendações com base em dados em tempo real. Os Agentes de IA podem até mesmo usar algoritmos de tomada de decisão avançados e modelos de machine learning para analisar dados e tomar decisões informadas de forma autônoma. Isso permite que eles lidem com cenários complexos e forneçam insights acionáveis, enquanto os modelos de chat de IA gerativos se concentram principalmente na geração de respostas baseadas em texto.
- Escalabilidade: os agentes de IA podem dimensionar as operações sem a necessidade de aumentos proporcionais nos recursos humanos. Isso é benéfico para as empresas que buscam crescer sem aumentar significativamente os custos operacionais.
- Disponibilidade 24 horas por dia, 7 dias por semana: assim como todos os softwares, os agentes de IA podem operar continuamente sem interrupções, garantindo que as tarefas sejam concluídas prontamente e que o atendimento ao cliente esteja disponível 24 horas por dia.

Os agentes são criados para simular a inteligência humana e podem ser aplicados em vários domínios, como atendimento ao cliente, análise de dados, automação e muito mais.

### Exemplos de casos de uso do agente de IA

Os agentes de IA têm uma ampla gama de aplicativos em vários setores. Aqui estão alguns exemplos notáveis:

#### Agentes de produtividade pessoal
Agentes de produtividade pessoal auxiliam indivíduos com tarefas diárias, como agendar reuniões, enviar emails e gerenciar listas de to-do. Por exemplo, o Microsoft 365 Copilot pode ajudar os usuários a elaborar documentos, criar apresentações e analisar dados no pacote do Microsoft Office.

#### Agentes de pesquisa
Os agentes de pesquisa monitoram continuamente as tendências do mercado, coletam dados e geram relatórios. Esses agentes podem ser usados em serviços financeiros para acompanhar o desempenho das ações, na área de saúde para se manterem atualizados com as pesquisas médicas mais recentes ou no marketing para analisar o comportamento do consumidor.

#### Agentes de vendas
Os agentes de vendas automatizam os processos de geração e qualificação de clientes potenciais. Eles podem pesquisar potenciais clientes potenciais, enviar mensagens de acompanhamento personalizadas e até agendar chamadas de vendas. Essa automação ajuda as equipes de vendas a se concentrarem em fechar negócios em vez de tarefas administrativas.

#### Agentes de atendimento ao cliente
Os agentes de atendimento ao cliente lidam com consultas de rotina, fornecem informações e resolvem problemas comuns. Eles podem ser integrados a chatbots em sites ou plataformas de mensagens, oferecendo suporte instantâneo aos clientes. Por exemplo, o Cineplex usa um agente de IA para processar solicitações de reembolso, reduzindo significativamente o tempo de tratamento e melhorando a satisfação do cliente.

#### Agentes do desenvolvedor
Os agentes de desenvolvedor ajudam em tarefas de desenvolvimento de software, como revisão de código, correção de bugs e gerenciamento de repositório. Eles podem atualizar automaticamente as bases de código, sugerir melhorias e garantir que os padrões de codificação sejam mantidos. O GitHub Copilot é um ótimo exemplo de um agente de desenvolvedor.

## Como usar o Serviço do Agente de IA do Azure

O Serviço de Agente de IA do Azure é um serviço totalmente gerenciado projetado para capacitar os desenvolvedores a criar, implantar e dimensionar com segurança agentes de IA extensíveis e de alta qualidade sem a necessidade de gerenciar os recursos de computação e armazenamento subjacentes. Esta unidade aborda a finalidade, os benefícios, os principais recursos e os recursos de integração do Serviço do Agente de IA do Azure.

### Finalidade do Serviço do Agente de IA do Azure

O Serviço do Agente de IA do Azure permite que os desenvolvedores criem agentes de IA adaptados às suas necessidades por meio de instruções personalizadas e ferramentas avançadas, como interpretadores de código e funções personalizadas. Esses agentes podem responder perguntas, executar ações ou automatizar fluxos de trabalho combinando modelos de IA generativos com ferramentas que interagem com fontes de dados do mundo real. O serviço simplifica o processo de desenvolvimento reduzindo a quantidade de código necessária e gerenciando a infraestrutura subjacente.

Anteriormente, os desenvolvedores podiam criar uma experiência semelhante a um agente usando APIs padrão no Azure AI Foundry e conectar-se a funções personalizadas ou outras ferramentas, mas fazer isso exigiria um esforço de codificação significativo. O Serviço do Agente de IA do Azure manipula tudo isso por meio da AI Foundry para criar agentes por meio do portal ou em seu próprio aplicativo em menos de 50 linhas de código. O exercício no módulo explora os dois métodos de criação de um agente.e

O Serviço do Agente de IA do Azure é ideal para cenários que exigem modelos de linguagem avançados para automação de fluxo de trabalho. Pode ser usado para:

- Responda a perguntas usando fontes de dados proprietárias ou em tempo real.
- Tome decisões e execute ações com base nas entradas do usuário.
- Automatize fluxos de trabalho complexos combinando modelos de IA generativos com ferramentas que interagem com dados do mundo real.

Por exemplo, um agente de IA pode ser criado para gerar relatórios, analisar dados ou até mesmo interagir com usuários por meio de aplicativos ou chatbots, tornando-o adequado para suporte ao cliente, análise de dados e relatórios automatizados.

### Principais recursos do Serviço do Agente de IA do Azure

O Serviço do Agente de IA do Azure oferece vários recursos importantes:

- Chamada automática de ferramenta: o serviço manipula todo o ciclo de vida de chamada de ferramentas, incluindo a execução do modelo, a invocação de ferramentas e o retorno de resultados.
- Dados gerenciados com segurança: os estados de conversa são gerenciados com segurança usando threads, eliminando a necessidade de os desenvolvedores lidarem com isso manualmente.
- Ferramentas prontas para uso: o serviço inclui ferramentas de recuperação de arquivo, interpretação de código e interação com fontes de dados como Bing, Azure AI Search e Azure Functions.
- Seleção de modelo flexível: os desenvolvedores podem escolher entre vários modelos, incluindo modelos do Azure OpenAI e outros, como Llama 3, Mistral e Cohere.
- Segurança de nível empresarial: o serviço garante a privacidade e a conformidade dos dados com o tratamento seguro de dados e a autenticação sem chave.
- Soluções de armazenamento personalizáveis: os desenvolvedores podem usar o armazenamento gerenciado pela plataforma ou trazer seu próprio Armazenamento de Blobs do Azure para visibilidade e controle completos.
O Serviço de Agente de IA do Azure fornece uma maneira mais simplificada e segura de criar e implantar agentes de IA em comparação com o desenvolvimento diretamente com a API de Inferência.

### Recursos do Serviço do Agente de IA do Azure
O Serviço de Agente de IA do Azure é totalmente gerenciado e projetado para ajudar os desenvolvedores a criar agentes sem precisar se preocupar com recursos subjacentes. Por meio do Azure, a AI Foundry e o Serviço de Agente provisionarão os recursos de nuvem necessários. Se desejar, você pode optar por conectar seus próprios recursos ao criar seu agente, dando a você a flexibilidade de utilizar o Azure, no entanto, funciona melhor para você.

No mínimo, você precisa criar um hub de IA do Azure com um projeto de IA do Azure para seu agente. Você pode adicionar mais serviços do Azure conforme necessário. Você pode criar os recursos usando o portal do Azure AI Foundry ou usar [modelos bicep predefinidos](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.azure-ai-agent-service) para implantar os recursos em sua assinatura. Duas arquiteturas comuns para soluções do Serviço do Agente de IA do Azure são:

- Configuração básica do agente: uma configuração mínima que inclui o hub de IA do Azure, o projeto de IA do Azure e os recursos dos Serviços de IA do Azure.

![](https://learn.microsoft.com/pt-br/training/wwl-data-ai/develop-ai-agent-azure/media/basic-agent-setup-resources.png)

- Configuração do agente padrão: uma configuração mais abrangente que inclui a configuração básica do agente, além do Azure Key Vault, do Azure AI Search e do Armazenamento do Azure.

![](https://learn.microsoft.com/pt-br/training/wwl-data-ai/develop-ai-agent-azure/media/standard-agent-setup-resources.png)

## Desenvolver agentes com o Serviço do Agente de IA do Azure
Soluções anteriores para obter uma experiência semelhante a um agente levaram centenas de linhas de código para fazer coisas como referenciar dados de aterramento ou conectar-se a uma função personalizada. O Serviço de Agente agora simplifica tudo isso, dando suporte à chamada de função do lado do cliente com apenas algumas linhas de código e conexões com o Azure Functions ou uma ferramenta definida por OpenAPI.

### Desenvolvendo aplicativos que usam agentes
O Serviço do Agente de IA do Azure fornece vários SDKs e uma API REST para você integrar agentes ao seu aplicativo usando sua linguagem de programação preferida. O exercício mais adiante neste módulo se concentra no Python, mas o padrão geral é o mesmo para REST ou outros SDKs de idioma.

![](https://learn.microsoft.com/pt-br/training/wwl-data-ai/develop-ai-agent-azure/media/ai-agent-code-pattern.png)

O diagrama mostra as seguintes etapas de alto nível que você deve implementar em seu código:

1. Conecte-se ao projeto do AI Foundry para seu agente, usando a cadeia de conexão do projeto e a autenticação de ID do Entra.
2. Obtenha uma referência a um agente existente que você criou no portal do Azure AI Foundry ou crie um novo especificando:

- A implantação do modelo no projeto que o agente deve usar para interpretar e responder a prompts.
- nstruções que determinam a funcionalidade e o comportamento do agente.
- Ferramentas e recursos que o agente pode usar para executar tarefas.

3. Crie um thread para uma sessão de chat com o agente. Todas as conversas com um agente são realizadas em um thread com estado que retém o histórico de mensagens e os artefatos de dados gerados durante o chat.
4. Adicione mensagens ao thread e invoque-o com o agente.
5. Verifique o status do thread e, quando estiver pronto, recupere as mensagens e os artefatos de dados.
6. Repita as duas etapas anteriores como um loop de chat até que a conversa possa ser concluída.
7. Quando terminar, exclua o agente e o thread para limpar os recursos e excluir dados que não são mais necessários.

### Ferramentas disponíveis para seu agente
Grande parte da funcionalidade aprimorada de um agente vem da capacidade do agente de determinar quando e como usar ferramentas. As ferramentas disponibilizam funcionalidades adicionais para o agente e, se a conversa ou tarefa garantir o uso de uma ou mais ferramentas, o agente chamará essa ferramenta e manipulará a resposta.

Você pode atribuir ferramentas ao criar um agente no portal do Azure AI Foundry ou ao definir um agente no código usando o SDK.

![](https://learn.microsoft.com/pt-br/training/wwl-data-ai/develop-ai-agent-azure/media/portal-tools.png)

Por exemplo, uma das ferramentas disponíveis é o interpretador de código. Essa ferramenta permite que seu agente execute o código personalizado que grava para conseguir algo, como o código MATLAB, para criar um grafo ou resolver um problema de análise de dados.

As ferramentas disponíveis são divididas em duas categorias:

## Ferramentas de conhecimento
As ferramentas de conhecimento aprimoram o contexto ou o conhecimento do agente. As ferramentas disponíveis incluem:

- Pesquisa do Bing: usa os resultados da pesquisa do Bing para aterrar prompts com dados ao vivo em tempo real da Web.
- Pesquisa de arquivo: solicitações de motivos com dados de arquivos em um repositório de vetores.
- Pesquisa de IA do Azure: solicitações de base com dados dos resultados da consulta do Azure AI Search.
- Microsoft Fabric: usa o Agente de Dados do Fabric para aterrar prompts com dados de seus armazenamentos de dados do Fabric.

## Ferramentas de ação
As ferramentas de ação executam uma ação ou executam uma função. As ferramentas disponíveis incluem:

- Interpretador de Código: uma área restrita para código Python gerado por modelo que pode acessar e processar arquivos carregados.
- Função: chame seu código de função personalizado – você deve fornecer definições e implementações de função.
- Função do Azure: chamar código no Azure Functions sem servidor.
- Especificação OpenAPI: chamar APIs externas com base na especificação OpenAPI 3.0.

Ao conectar ferramentas internas e personalizadas, você pode permitir que seu agente execute inúmeras tarefas em seu nome.

## Resumo

Os agentes de IA representam um avanço significativo no campo da inteligência artificial, oferecendo inúmeros benefícios para empresas e indivíduos. Ao automatizar tarefas rotineiras, aprimorar a tomada de decisões e fornecer soluções escalonáveis, os agentes de IA estão transformando como trabalhamos e interagimos com a tecnologia. À medida que esses agentes continuarem a evoluir, seus potenciais aplicativos só se expandirão, gerando mais inovação e eficiência em vários setores.

Neste módulo, você aprendeu sobre a finalidade do Serviço de Agente de IA do Azure, seus principais recursos, o processo de instalação e seus recursos de integração com outros serviços de IA do Azure. Também abordamos o desafio de criar, implantar e dimensionar agentes de IA. O Serviço de Agente de IA do Azure resolve vários desses desafios, fornecendo um ambiente totalmente gerenciado para criar agentes de IA extensíveis e de alta qualidade com gerenciamento mínimo de codificação e infraestrutura.

As técnicas abordadas neste módulo demonstram várias vantagens, incluindo chamada automática de ferramenta, gerenciamento seguro de dados e seleção de modelo flexível. Esses recursos permitem que os desenvolvedores se concentrem na criação de soluções inteligentes, garantindo a segurança e a conformidade de nível empresarial. O impacto nos negócios inclui processos de desenvolvimento simplificados, sobrecarga operacional reduzida e funcionalidades aprimoradas de IA.




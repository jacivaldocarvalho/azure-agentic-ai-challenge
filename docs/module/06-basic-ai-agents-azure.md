# Conceitos básicos dos agentes de IA no Azure

> Os agentes de IA representam a próxima geração de aplicativos inteligentes. Saiba como eles podem ser desenvolvidos e usados no Microsoft Azure.

## Índice

- [Conceitos básicos dos agentes de IA no Azure](#conceitos-básicos-dos-agentes-de-ia-no-azure)
  - [Índice](#índice)
  - [Introdução](#introdução)
  - [O que são agentes de IA?](#o-que-são-agentes-de-ia)
  - [Opções para desenvolvimento de agente](#opções-para-desenvolvimento-de-agente)
    - [Serviço do Agente de IA do Azure](#serviço-do-agente-de-ia-do-azure)
    - [API de Assistentes do OpenAI](#api-de-assistentes-do-openai)
    - [Kernel Semântico](#kernel-semântico)
    - [AutoGen](#autogen)
    - [SDK de Agentes do Microsoft 365](#sdk-de-agentes-do-microsoft-365)
    - [Microsoft Copilot Studio](#microsoft-copilot-studio)
    - [Construtor de agentes do Copilot Studio no Microsoft 365 Copilot](#construtor-de-agentes-do-copilot-studio-no-microsoft-365-copilot)
    - [Escolhendo uma solução de desenvolvimento de agente](#escolhendo-uma-solução-de-desenvolvimento-de-agente)
  - [Serviço do Agente de IA do Azure](#serviço-do-agente-de-ia-do-azure-1)
    - [Componentes de um agente](#componentes-de-um-agente)
  - [Resumo](#resumo)

## Introdução
À medida que os modelos de IA generativos se tornam mais poderosos e onipresentes, seu uso cresceu além de aplicativos simples de "chat" para alimentar agentes inteligentes que podem operar de forma autônoma para automatizar tarefas. Cada vez mais, as organizações estão usando modelos de IA generativos para criar agentes que orquestram processos de negócios e coordenam cargas de trabalho de maneiras que antes eram inimagináveis.

Este módulo discute alguns dos principais conceitos relacionados aos agentes de IA e apresenta algumas das tecnologias que os desenvolvedores podem usar para criar soluções de agente no Microsoft Azure.

## O que são agentes de IA?
Os agentes de IA são serviços de software inteligentes que combinam modelos de IA generativos com dados contextuais e a capacidade de automatizar tarefas com base na entrada do usuário e em fatores ambientais que eles percebem.

Por exemplo, uma organização pode criar um agente de IA para ajudar os funcionários a gerenciar declarações de despesas. O agente pode usar um modelo gerador combinado com a documentação da política de despesas corporativas para responder a perguntas dos funcionários sobre quais despesas podem ser reivindicadas e quais limites se aplicam. Além disso, o agente poderia usar uma função programática para enviar automaticamente declarações de despesas para despesas repetidas regularmente (como uma fatura mensal de celular) ou rotear de forma inteligente as despesas para o aprovador apropriado com base nos valores de declaração.

Um exemplo do cenário do agente de despesas é mostrado no diagrama a seguir.

O diagrama mostra o seguinte processo:

1. Um usuário faz uma pergunta ao agente de despesas sobre despesas que podem ser reivindicadas.
2. O agente de despesas aceita a pergunta como um prompt.
3. agente usa um repositório de conhecimento que contém informações de política de despesas para aterrar o prompt.
4. O prompt aterrado é enviado ao modelo de linguagem do agente para gerar uma resposta.
5. O agente gera uma declaração de despesa em nome do usuário e envia-a para ser processada e gerar um pagamento de verificação.

Em cenários mais complexos, as organizações podem desenvolver soluções de vários agentes em que vários agentes coordenam o trabalho entre elas. Por exemplo, um agente de reserva de viagens poderia reservar voos e hotéis para funcionários e enviar automaticamente declarações de despesas com recibos apropriados para o agente de despesas, conforme mostrado neste diagrama:


O diagrama mostra o seguinte processo:

1. Um usuário fornece detalhes de uma próxima viagem a um agente de reserva de viagens.
2. O agente de reserva de viagens automatiza a reserva de passagens de voo e reservas de hotel.
3. O agente de reserva de viagens inicia uma reivindicação de despesas para os custos de viagem, embora o agente de despesas.
4. O agente de despesas envia a declaração de despesas para processamento.

## Opções para desenvolvimento de agente
Há muitas maneiras de os desenvolvedores criarem agentes de IA, incluindo várias estruturas e SDKs.

### Serviço do Agente de IA do Azure
O Serviço do Agente de IA do Azure é um serviço gerenciado no Azure que foi projetado para fornecer uma estrutura para criar, gerenciar e usar agentes de IA no Azure AI Foundry. O serviço é baseado na API de Assistentes do OpenAI, mas com maior opção de modelos, integração de dados e segurança corporativa; permitindo que você use o SDK do OpenAI e o SDK do Azure Foundry para desenvolver soluções agente.

### API de Assistentes do OpenAI
A API de Assistentes do OpenAI fornece um subconjunto dos recursos no Serviço do Agente de IA do Azure e só pode ser usada com modelos OpenAI. No Azure, você pode usar a API de Assistentes com o serviço Azure OpenAI, embora, na prática, o Serviço do Agente de IA do Azure forneça maior flexibilidade e funcionalidade para o desenvolvimento de agente no Azure.

### Kernel Semântico
O Kernel Semântico é um kit de desenvolvimento leve e de software livre que você pode usar para criar agentes de IA e orquestrar soluções de vários agentes. O SDK de Kernel Semântico principal foi projetado para todos os tipos de desenvolvimento de IA generativo, enquanto o Kernel Agent Semântico é uma plataforma especificamente otimizada para criar agentes e implementar padrões de solução agente.

### AutoGen
O AutoGen é uma estrutura de software livre para desenvolver agentes rapidamente. É útil como uma ferramenta de pesquisa e ideação ao experimentar agentes.

### SDK de Agentes do Microsoft 365
Os desenvolvedores podem criar agentes auto-hospedados para entrega por meio de uma ampla gama de canais usando o SDK do Microsoft 365 Agents. Apesar do nome, os agentes criados usando esse SDK não estão limitados ao Microsoft 365, mas podem ser entregues por meio de canais como Slack ou Messenger

### Microsoft Copilot Studio
O Microsoft Copilot Studio fornece um ambiente de desenvolvimento de baixo código que os "desenvolvedores cidadãos" podem usar para criar e implantar rapidamente agentes que se integram a um ecossistema do Microsoft 365 ou canais comumente usados como Slack e Messenger. A interface de design visual do Copilot Studio torna-a uma boa opção para criar agentes quando você tem pouca ou nenhuma experiência de desenvolvimento de software profissional.

### Construtor de agentes do Copilot Studio no Microsoft 365 Copilot
Os usuários empresariais podem usar o #B0 ferramenta declarativa #C1 construtor de agentes do Copilot Studio no Microsoft 365 Copilot para criar agentes básicos para tarefas comuns. A natureza declarativa da ferramenta permite que os usuários criem um agente descrevendo a funcionalidade necessária ou podem usar uma interface visual intuitiva para especificar opções para seu agente.

### Escolhendo uma solução de desenvolvimento de agente
Com uma ampla gama de ferramentas e estruturas disponíveis, pode ser desafiador decidir quais delas usar. Use as seguintes considerações para ajudá-lo a identificar as opções certas para seu cenário:

- Para usuários de negócios com pouca ou nenhuma experiência de desenvolvimento de software, o construtor de agentes do Copilot Studio no Microsoft 365 Copilot Chat fornece uma maneira de criar agentes declarativos simples que automatizam tarefas cotidianas. Essa abordagem pode capacitar os usuários de uma organização a se beneficiarem de agentes de IA com impacto mínimo na TI.
- Se os usuários empresariais tiverem habilidades técnicas suficientes para criar soluções de baixo código usando tecnologias do Microsoft Power Platform, o Copilot Studio permitirá que eles combinem essas habilidades com seus conhecimentos de domínio de negócios e criem soluções de agente que estendam os recursos do Microsoft 365 Copilot ou adicionem funcionalidades agente a canais comuns como Microsoft Teams, Slack ou Messenger.
- Quando uma organização precisa de extensões mais complexas para recursos do Microsoft 365 Copilot, os desenvolvedores profissionais podem usar o SDK do Microsoft 365 Agents para criar agentes direcionados aos mesmos canais do Copilot Studio.
- Para desenvolver soluções agente que usam serviços de back-end do Azure com uma ampla opção de modelos, serviços de armazenamento e pesquisa personalizados e integração com os serviços de IA do Azure, os desenvolvedores profissionais devem usar o Serviço de Agente de IA do Azure no Azure AI Foundry.
- Comece com o Serviço de Agente de IA do Azure para desenvolver agentes individuais e autônomos. Quando precisar criar soluções de vários agentes, use o Kernel Semântico para orquestrar os agentes em sua solução.

## Serviço do Agente de IA do Azure
O Serviço do Agente de IA do Azure é um serviço no Azure AI Foundry que você pode usar para criar, testar e gerenciar agentes de IA. Ele fornece uma experiência de desenvolvimento de agente visual no portal do Azure AI Foundry e uma experiência de desenvolvimento de primeiro código usando o SDK do Azure AI Foundry.

### Componentes de um agente
Os agentes desenvolvidos usando o Serviço de Agente de IA do Azure têm os seguintes elementos:

- Um modelo de IA gerador implantado que permite ao agente raciocinar e gerar respostas de linguagem natural para prompts. Você pode usar modelos openai comuns e uma seleção de modelos do catálogo de modelos do Azure AI Foundry.
- Fontes de dados que permitem ao agente aterrar prompts com dados contextuais. As fontes de conhecimento potenciais incluem resultados de pesquisa na Internet do Microsoft Bing, um índice do Azure AI Search ou seus próprios dados e documentos.
- Funções programáticas que permitem ao agente automatizar ações #B2 #A3 . Ferramentas internas para acessar o conhecimento no Azure AI Search e no Bing são fornecidas, bem como uma ferramenta de interpretador de código que você pode usar para gerar e executar código Python. Você também pode criar ferramentas personalizadas usando seu próprio código ou o Azure Functions.

As conversas entre usuários e agentes ocorrem em um thread, que retém um histórico das mensagens trocadas na conversa, bem como quaisquer ativos de dados, como arquivos, que são gerados.

## Resumo
Neste módulo, você aprendeu sobre agentes de IA e algumas das opções disponíveis para desenvolvê-los. Você também aprendeu a criar um agente simples usando as ferramentas visuais para o Serviço do Agente de IA do Azure no portal do Azure AI Foundry.
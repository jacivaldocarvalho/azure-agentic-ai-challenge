# Introdução aos controles de segurança do serviço do agente de IA

>Uma visão geral introdutória dos controles de segurança do Serviço de Agente de IA do Azure.

## Índice

- [Introdução aos controles de segurança do serviço do agente de IA](#introdução-aos-controles-de-segurança-do-serviço-do-agente-de-ia)
  - [Índice](#índice)
  - [Introdução: Entenda o Serviço de Agente de IA do Azure](#introdução-entenda-o-serviço-de-agente-de-ia-do-azure)
  - [Protegendo o Serviço do Agente Azure AI](#protegendo-o-serviço-do-agente-azure-ai)
  - [Controle de acesso baseado em função do serviço do agente de IA do Azure](#controle-de-acesso-baseado-em-função-do-serviço-do-agente-de-ia-do-azure)
  - [Serviço de Agente e Acesso à Rede](#serviço-de-agente-e-acesso-à-rede)
  - [Resumo](#resumo)

## Introdução: Entenda o Serviço de Agente de IA do Azure
O Serviço de Agente de IA do Azure é um serviço totalmente gerenciado, projetado para capacitar desenvolvedores a criar, implantar e escalar com segurança agentes de IA extensíveis e de alta qualidade, sem a necessidade de gerenciar os recursos de computação e armazenamento subjacentes. Tarefas que podem levar centenas de linhas de código para suportar chamadas de funções do lado do cliente agora podem ser realizadas com apenas algumas linhas de código com o Serviço de Agente de IA do Azure.

Um Agente de IA atua como um microsserviço "inteligente" que pode ser usado para responder a perguntas (Recuperação de Geração Aumentada), executar ações ou automatizar completamente fluxos de trabalho. Os agentes de IA conseguem isso combinando o poder dos modelos generativos de IA para entender recursos de informação com ferramentas que permitem que esse modelo acesse e interaja com fontes de dados do mundo real.

Como o Azure AI Agent Service é um serviço totalmente gerenciado pela Microsoft, você pode se concentrar na criação de fluxos de trabalho e nos agentes que os alimentam sem precisar se preocupar com dimensionamento, segurança ou gerenciamento da infraestrutura subjacente para agentes individuais.

Como o Serviço de Agente de IA do Azure é um serviço gerenciado pela Microsoft e você não precisa se preocupar com a segurança subjacente de suas partes móveis, você ainda deve aplicar os princípios de segurança padrão ao usar o serviço de agente de IA. Esses princípios incluem:

- Restrinja o acesso ao serviço usando o controle de acesso baseado em funções. Garanta que apenas as entidades de segurança apropriadas possam interagir com o serviço do agente de IA e institua o princípio do menor privilégio.
- Restrinja o acesso ao serviço do Agente de IA. O serviço do Agente de IA está interagindo com recursos confidenciais, como dados organizacionais. Certifique-se de que o escopo desse acesso seja limitado e que o serviço do Agente de IA e suas ferramentas tenham apenas a visibilidade necessária de recursos, como repositórios de dados.
- Restrinja o acesso à rede do serviço do Agente de IA e o acesso à rede do serviço do Agente de IA. Limite quais hosts de rede podem interagir com o serviço do Agente de IA e controle quais hosts de rede o serviço do Agente de IA e suas ferramentas associadas podem alcançar.

## Protegendo o Serviço do Agente Azure AI
No Azure AI Foundry, os Agentes são associados a projetos, e os projetos estão localizados em hubs. Os hubs são o principal recurso de nível superior do Azure para o Azure AI Foundry e fornecem uma maneira central para uma equipe governar a segurança, a conectividade e os recursos de computação em playgrounds e projetos. Normalmente, um administrador de TI ou líder técnico gerencia um hub. Esses administradores de TI ou líderes técnicos podem usar hubs para governar a infraestrutura, incluindo configuração de rede virtual, chaves gerenciadas pelo cliente, identidades gerenciadas e políticas, além de configurar serviços relevantes do Azure AI. Depois que um hub é criado, os desenvolvedores podem criar projetos a partir dele e acessar recursos compartilhados da empresa sem precisar da ajuda constante de um administrador de TI.

Os projetos funcionam como espaços de desenvolvimento isolados, permitindo que desenvolvedores e cientistas de dados criem, testem e implantem sistemas de IA. Cada vez que um novo projeto é criado em um hub, ele herda automaticamente as configurações de segurança desse hub. Os agentes, por fazerem parte dos projetos, podem aproveitar os recursos e as configurações definidos tanto no nível do hub quanto do projeto.

Você pode aplicar controles de segurança por meio da interface do Azure AI Foundry ou aplicando controles de segurança por meio do portal do Azure. Ao implantar um hub e um projeto, esses recursos são armazenados em um grupo de recursos na sua assinatura do Azure. O Azure AI Foundry oferece uma maneira abstrata de interagir com esses controles de segurança sem exigir conhecimento dos princípios de administração do Azure. O Azure AI Foundry permite configurar funções de controle de acesso baseadas em funções. No portal do Azure, você pode definir as seguintes configurações de segurança no nível do Hub de IA do Azure:

- Controle de acesso baseado em função
- Acesso à rede
- Monitoramento de alertas, métricas e logs

No nível do projeto do Azure AI, você pode configurar o controle de acesso baseado em função, alertas de monitoramento, métricas e logs, mas não pode configurar restrições de acesso à rede. Na maioria dos cenários, você configura os controles de segurança relacionados aos agentes do Serviço de Agentes do Azure AI no nível do hub. Quando você precisa ter diferentes conjuntos de controles de segurança, hospede os agentes do Serviço de Agentes do Azure AI em diferentes hubs do Azure AI.

## Controle de acesso baseado em função do serviço do agente de IA do Azure
O controle de acesso baseado em função do Azure (Azure RBAC) é usado para gerenciar o acesso aos recursos do Azure, como a capacidade de criar novos recursos ou usar os existentes. Os usuários com o seu ID Microsoft Entra recebem funções específicas, que concedem acesso aos recursos. O RBAC do Azure permite que você configure o acesso aos hubs e projetos do Azure AI Foundry e, por extensão, aos agentes existentes nesses projetos.

O hub do Azure AI Foundry tem funções integradas que estão disponíveis por padrão.

| Papel                                           | Descrição                                                                                                                                                                                                                                                                                      |
|------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Proprietário                                   | Acesso total ao hub, incluindo a capacidade de gerenciar e criar novos hubs e atribuir permissões. Esta função é atribuída automaticamente ao criador do hub.                                                                                            |
| Contribuinte                                   | O usuário tem acesso total ao hub, incluindo a capacidade de criar novos hubs, mas não consegue gerenciar as permissões do hub no recurso existente.                                                                                                     |
| Administrador de IA do Azure                   | Esta função é atribuída automaticamente à identidade gerenciada atribuída pelo sistema para o hub. A função de Administrador de IA do Azure tem as permissões mínimas necessárias para que a identidade gerenciada execute suas tarefas.                  |
| Desenvolvedor de IA do Azure                   | Execute todas as ações, exceto criar novos hubs e gerenciar as permissões do hub. Por exemplo, os usuários podem criar projetos, cálculos e conexões. Os usuários podem atribuir permissões dentro de seus projetos. Os usuários podem interagir com recursos de IA do Azure existentes. |
| Operador de implantação de inferência de IA do Azure | Execute todas as ações necessárias para criar uma implantação de recurso dentro de um grupo de recursos.                                                                                                                                                    |
| Leitor                                         | Acesso somente leitura ao hub. Essa função é atribuída automaticamente a todos os membros do projeto no hub.                                                                                                                                              |

Os hubs têm a identidade gerenciada atribuída pelo sistema à função de Administrador de IA do Azure. Essa função tem um escopo mais restrito, limitando-se às permissões mínimas necessárias para que a identidade gerenciada execute suas tarefas. Essa identidade gerenciada atribuída pelo sistema é herdada no nível do projeto. Dependendo da configuração de um Agente de IA do Azure, o processo usará a identidade gerenciada atribuída pelo sistema ao acessar fontes de dados ou executar ações como executar código, executar uma função personalizada ou uma função do Azure com a identidade do usuário.

Quando um usuário recebe acesso a um projeto (por exemplo, por meio do gerenciamento de permissões do portal do Azure AI Foundry), mais duas funções são atribuídas automaticamente a ele. A primeira função é Leitor no hub. A segunda função é Operador de Implantação de Inferência, que permite ao usuário criar implantações no grupo de recursos em que o projeto está.

A tabela a seguir é um exemplo de como configurar o controle de acesso baseado em função para o Azure AI Foundry para uma empresa.

| Persona                           | Papel                                              | Propósito                                                                                                                                                                                                                                                                                                     |
|-----------------------------------|----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Administrador de TI               | Proprietário do hub                                | O administrador de TI pode garantir que o hub esteja configurado de acordo com os padrões da empresa. Ele pode atribuir aos gerentes a função de Colaborador no recurso, caso deseje permitir que eles criem novos hubs. Ou pode atribuir aos gerentes a função de Desenvolvedor de IA do Azure no recurso para não permitir a criação de novos hubs. |
| Gerentes                          | Colaborador ou desenvolvedor de IA do Azure no hub | Os gerentes podem gerenciar o hub, auditar recursos de computação, auditar conexões e criar conexões compartilhadas.                                                                                                                                                                                         |
| Líder de equipe/Desenvolvedor líder | Desenvolvedor de IA do Azure no hub                 | Os desenvolvedores líderes podem criar projetos para suas equipes e criar recursos compartilhados (como computação e conexões) no nível do hub. Após a criação do projeto, os proprietários podem convidar outros membros.                                                                                   |
| Membros da equipe/desenvolvedores | Colaborador ou desenvolvedor de IA do Azure no projeto | Os desenvolvedores podem criar e implantar modelos de IA em um projeto e criar ativos que permitam o desenvolvimento, como computações e conexões.                                                                                                                     |

Você pode adicionar usuários e atribuir funções diretamente do Azure AI Foundry, tanto no nível do hub quanto do projeto. No centro de gerenciamento, selecione Usuários na seção do hub ou do projeto e, em seguida, selecione Novo usuário para adicionar um usuário.

![](https://learn.microsoft.com/pt-br/training/advocates/intro-ai-agent-service-security-controls/media/hub-user-role.png)

Ao criar um hub, as permissões de controle de acesso baseadas em funções integradas concedem acesso para usar o recurso. No entanto, se desejar usar recursos além dos que foram criados em seu nome, você precisa garantir que:

- O recurso que você está tentando usar tem permissões configuradas para permitir que você o acesse.
- Seu hub tem permissão para acessá-lo.

Por exemplo, se você estiver tentando consumir um novo armazenamento de Blobs que não esteja hospedado no hub de IA do Azure associado, certifique-se de que a identidade gerenciada do hub seja adicionada à função de Leitor de Armazenamento de Blobs do Blob. Você também precisará configurar o acesso de saída gerenciado do local de trabalho para permitir a comunicação de rede com o endpoint associado ao armazenamento de Blobs. A configuração do acesso à rede será abordada com mais detalhes na próxima unidade.

## Serviço de Agente e Acesso à Rede
Você configura o acesso à rede para um Agente de IA do Azure associado a um projeto do Azure Foundry no nível do Hub. Você só pode definir as configurações de rede para um Hub no portal do Azure e não pode definir as configurações de rede no Azure Foundry.

Você tem as seguintes opções ao configurar o acesso à rede:

- Acesso público. Permita o acesso público de todas as redes, incluindo a internet, ou desative o acesso público. Se você desativar o acesso público, precisará acessar o hub, o projeto e o serviço do Agente de IA por meio de um endpoint privado.
- Conexões de endpoint privadas. Permite adicionar endpoints privados para acessar o hub, os projetos e os Agentes de IA do Azure. Ao configurar o acesso a endpoints privados, você pode permitir o acesso de redes virtuais e sub-redes específicas. Os endpoints privados exigem um endereço DNS que possa ser hospedado em uma zona DNS privada.
- Acesso de saída gerenciado pelo Workspace. Ao configurar o acesso de saída para o Hub de IA do Azure associado ao projeto que hospeda o Agente de IA do Azure, você pode escolher:
  - Desativado: o Compute pode acessar recursos públicos e a movimentação de dados de saída é irrestrita.
  - Permitir saída da Internet: o computador pode acessar recursos privados e a movimentação de dados de saída é irrestrita.
  - Permitir apenas saídas aprovadas. O Compute pode acessar recursos que estão na lista de permissões específicas e a movimentação de dados de saída é restrita a endereços aprovados.

![](https://learn.microsoft.com/pt-br/training/advocates/intro-ai-agent-service-security-controls/media/networking-configuration.png)

Para acessar seus recursos não pertencentes ao Azure, localizados em uma rede virtual diferente ou totalmente on-premises a partir da rede virtual gerenciada do Azure AI Foundry, você precisa configurar e implantar um Gateway de Aplicativo. Por meio desse Gateway de Aplicativo, você pode configurar o acesso completo de ponta a ponta aos seus recursos. Após configurar o Gateway de Aplicativo, você pode criar um ponto de extremidade privado da rede virtual gerenciada do hub do Azure AI Foundry para o Gateway de Aplicativo. Um Ponto de Extremidade Privado do Azure permite acesso privado a recursos específicos, como os Hubs do Azure Foundry e seus projetos, sem expô-los à Internet pública, garantindo que os dados permaneçam isolados e seguros.

![](https://learn.microsoft.com/pt-br/training/advocates/intro-ai-agent-service-security-controls/media/ai-foundry-app-gateway.png)

## Resumo
Neste módulo, você aprendeu a gerenciar as configurações de segurança dos agentes do serviço AI Agent, configurando a segurança dos hubs e projetos do AI Foundry. Você aprendeu sobre as diferentes funções do RBAC associadas ao AI Foundry, como a identidade gerenciada se relaciona aos agentes do AI e como configurar o acesso e as restrições à rede.
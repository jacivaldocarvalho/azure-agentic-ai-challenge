# Orquestre uma solução multiagente usando o Semantic Kernel

> Aprenda a usar o Semantic Kernel SDK para desenvolver seus próprios agentes de IA que podem colaborar para uma solução multiagente.

## Índice

- [Orquestre uma solução multiagente usando o Semantic Kernel](#orquestre-uma-solução-multiagente-usando-o-semantic-kernel)
  - [Índice](#índice)
  - [Introdução](#introdução)
  - [Entenda a estrutura do agente do kernel semântico](#entenda-a-estrutura-do-agente-do-kernel-semântico)
    - [O que é o Semantic Kernel Agent Framework?](#o-que-é-o-semantic-kernel-agent-framework)
    - [Conceitos básicos](#conceitos-básicos)
    - [Tipos de agentes](#tipos-de-agentes)
    - [Por que você deve usar o Semantic Kernel Agent Framework](#por-que-você-deve-usar-o-semantic-kernel-agent-framework)
  - [Criar um chat em grupo de agentes](#criar-um-chat-em-grupo-de-agentes)
    - [Adicionar mensagens ao chat](#adicionar-mensagens-ao-chat)
    - [Modos de conversação no AgentGroupChat](#modos-de-conversação-no-agentgroupchat)
  - [Crie uma estratégia de seleção de agentes](#crie-uma-estratégia-de-seleção-de-agentes)
    - [Seleção de agentes](#seleção-de-agentes)
      - [Por que a seleção de agentes é importante?](#por-que-a-seleção-de-agentes-é-importante)
    - [Como a estrutura seleciona os agentes?](#como-a-estrutura-seleciona-os-agentes)
      - [Conversas de turno único](#conversas-de-turno-único)
      - [Conversas multi-turno](#conversas-multi-turno)
    - [Estratégia de seleção de agentes](#estratégia-de-seleção-de-agentes)
      - [Estratégia de Seleção Sequencial](#estratégia-de-seleção-sequencial)
      - [Estratégia de Seleção de Função do Kernel](#estratégia-de-seleção-de-função-do-kernel)
      - [Classe base SelectionStrategy](#classe-base-selectionstrategy)
    - [Truncando o histórico do bate-papo](#truncando-o-histórico-do-bate-papo)
  - [Defina uma estratégia de encerramento de chat](#defina-uma-estratégia-de-encerramento-de-chat)
    - [Estratégia de rescisão](#estratégia-de-rescisão)
    - [Por que usar uma estratégia de rescisão?](#por-que-usar-uma-estratégia-de-rescisão)
    - [Como a estrutura implementa estratégias de término?](#como-a-estrutura-implementa-estratégias-de-término)
      - [Estratégia de Término Padrão](#estratégia-de-término-padrão)
      - [Estratégia de término da função do kernel](#estratégia-de-término-da-função-do-kernel)
      - [Classe base TerminationStrategy](#classe-base-terminationstrategy)
    - [Truncando o histórico do bate-papo](#truncando-o-histórico-do-bate-papo-1)
    - [Estado de conversação](#estado-de-conversação)
  - [Resumo](#resumo)

## Introdução

Agentes de IA oferecem uma combinação poderosa de tecnologias, capazes de concluir tarefas com o uso de IA generativa. No entanto, em algumas situações, a tarefa necessária pode ser maior do que o realista para um único agente. Para esses cenários, considere uma solução multiagente . Uma solução multiagente permite que os agentes colaborem na mesma conversa.

Imagine que você esteja tentando lidar com desafios comuns de DevOps, como monitorar o desempenho de aplicativos, identificar problemas e implementar correções. Um sistema multiagente pode consistir em quatro agentes especializados trabalhando em colaboração:

- O Agente de Monitoramento ingere continuamente logs e métricas, detecta anomalias usando processamento de linguagem natural (PNL) e dispara alertas quando surgem problemas.
- O Agente de Análise de Causa Raiz então correlaciona essas anomalias com alterações recentes do sistema, usando modelos de aprendizado de máquina ou regras predefinidas para identificar a causa raiz do problema.
- Depois que a causa raiz é identificada, o Agente de Implantação Automatizada assume o controle para implementar correções ou reverter alterações problemáticas interagindo com pipelines de CI/CD e executando scripts de implantação.
- Por fim, o Agente de Relatórios gera relatórios detalhados resumindo as anomalias, causas raiz e soluções, e notifica as partes interessadas por e-mail ou outros canais de comunicação.

Este sistema multiagente modular, escalável e inteligente otimiza o processo de DevOps. Os agentes colaboram para reduzir a intervenção manual e aumentar a eficiência, garantindo comunicação e resolução de problemas em tempo hábil.

Neste módulo, você explorará como usar os poderosos recursos do Semantic Kernel para projetar e orquestrar agentes inteligentes que trabalham em colaboração para resolver problemas complexos. Você também aprenderá a usar o Semantic Kernel Agents Framework para desenvolver seus próprios agentes de IA que podem colaborar em uma solução multiagente.

## Entenda a estrutura do agente do kernel semântico

O Semantic Kernel é um SDK de código aberto que permite aos desenvolvedores integrar modelos de IA em seus aplicativos. Parte desse SDK é o Semantic Kernel Agents Framework , que permite a criação de agentes usando os mesmos recursos existentes no framework Semantic Kernel principal.

### O que é o Semantic Kernel Agent Framework?
O Semantic Kernel Agent Framework é um framework projetado para ajudar desenvolvedores a criar agentes com tecnologia de IA. Esses agentes podem processar entradas do usuário, tomar decisões e executar tarefas de forma autônoma, utilizando modelos de linguagem de programação de grande porte e lógica de programação tradicional. O framework fornece componentes estruturados para definir fluxos de trabalho baseados em IA, permitindo que os agentes interajam com usuários, APIs e serviços externos.

### Conceitos básicos
O Agent Framework no Semantic Kernel fornece arquitetura sobre os recursos existentes do Semantic Kernel, incluindo:

- Agentes
Agentes são entidades inteligentes, orientadas por IA, capazes de raciocinar e executar tarefas. Eles utilizam modelos de linguagem, funções e memória para tomar decisões dinamicamente.

- Colaboração de agentes
Os agentes podem colaborar por meio de um chat em grupo , que permite que vários agentes participem do mesmo chat, mesmo que sejam de tipos diferentes. Os chats em grupo determinam qual agente deve responder e como determinar se a conversa foi encerrada.

Os recursos que impulsionam o Semantic Kernel também ainda estão disponíveis no Agent Framework, incluindo:

- Núcleo
O kernel é o componente central do Kernel Semântico. Ele atua como o mecanismo de execução, gerenciando interações de IA, orquestração de funções e memória.

- Ferramentas e plugins
Os plugins se alinham aos recursos existentes do Kernel Semântico, permitindo que os agentes interajam dinamicamente com serviços externos ou executem tarefas complexas por meio de chamadas de função. Dentro do Agent Framework, ferramentas estão disponíveis para fornecer funcionalidades extras aos seus agentes, como pesquisa de arquivos ou interpretador de código, semelhante ao uso de ferramentas no serviço Azure AI Agent. Os agentes usam ferramentas e plugins para executar tarefas específicas.

- História
Os agentes podem manter o histórico de conversas de múltiplas interações, permitindo que acompanhem interações anteriores e adaptem as respostas conforme necessário. O histórico de conversas está sempre acessível aos agentes, seja como um todo ou para o histórico de conversas de um agente específico.

### Tipos de agentes
O Semantic Kernel Agent Framework oferece suporte a vários tipos diferentes de agentes, incluindo:

- Agente de IA do Azure - um agente especializado dentro do Framework de Agente de Kernel Semântico. O AzureAIAgenttipo foi projetado para fornecer recursos avançados de conversação com integração perfeita entre ferramentas. Ele automatiza a chamada de ferramentas e gerencia o histórico de conversas com segurança usando threads, reduzindo a sobrecarga de manutenção de estado. O agente AzureAIAgenttambém oferece suporte a uma variedade de ferramentas integradas, incluindo recuperação de arquivos, execução de código e interação de dados via Bing, Azure AI Search, Azure Functions e OpenAPI.
- Agente de Conclusão de Chat : projetado para interfaces de conclusão de chat e conversação. O ChatCompletionAgenttipo espelha os recursos e padrões do Serviço de IA subjacente para oferecer suporte ao processamento de linguagem natural, compreensão contextual e gerenciamento de diálogos.
- Agente Assistente OpenAI : projetado para recursos mais avançados e tarefas multietapas. O OpenAIAssistantAgenttipo suporta interações orientadas a objetivos com recursos adicionais, como interpretação de código e pesquisa de arquivos.

### Por que você deve usar o Semantic Kernel Agent Framework
O Semantic Kernel Agent Framework oferece uma plataforma robusta para a construção de agentes de IA inteligentes, autônomos e colaborativos. O framework pode integrar agentes de diversas fontes, incluindo o Serviço de Agente de IA do Azure, e oferece suporte tanto à colaboração multiagente quanto à interação entre humanos. Os agentes podem trabalhar juntos para orquestrar fluxos de trabalho sofisticados, onde cada agente se especializa em uma tarefa específica, como coleta de dados, análise ou tomada de decisão. O framework também facilita processos com envolvimento humano, permitindo que os agentes aprimorem a tomada de decisão humana, fornecendo insights ou automatizando tarefas repetitivas. Essa combinação de autonomia, colaboração e interatividade torna o Semantic Kernel Agent Framework a escolha ideal para aplicações que exigem comportamento dinâmico e orientado a objetivos.

## Criar um chat em grupo de agentes
Um recurso fundamental do Semantic Kernel Agent Framework é sua capacidade de facilitar interações entre múltiplos agentes. Usando o Semantic Kernel Agent Framework AgentGroupChat, os desenvolvedores podem criar conversas dinâmicas e multiagentes, nas quais diferentes tipos de agentes colaboram para gerar respostas.

A AgentGroupChatclasse estende a estrutura do AgentChat, fornecendo uma maneira estruturada de gerenciar a colaboração entre vários agentes. Ela oferece mecanismos integrados para controlar o fluxo de conversas, definir estratégias de colaboração e oferecer suporte a interações de turno único e múltiplos turnos.

Para criar o AgentGroupChat, você pode inicializar o objeto de bate-papo com um conjunto predefinido de agentes. Por exemplo:

```python
# Define agents
agent_writer = AzureAIAgent(...)
agent_reviewer = AzureAIAgent(...)

# Create chat with participating agents
chat = AgentGroupChat(agents=[agent_writer, agent_reviewer])
```

Ou você pode começar com um chat vazio e adicionar agentes dinamicamente. Por exemplo:

```python
# Create an empty chat
chat = AgentGroupChat()

# Add agents to an existing chat
chat.add_agent(agent=agent_writer)
chat.add_agent(agent=agent_reviewer)
```

### Adicionar mensagens ao chat
Após a criação do seu chat, você pode criar um ChatMessageContentobjeto e adicioná-lo à conversa. O ChatMessageContentobjeto recebe um parâmetro de função, além do conteúdo. Por exemplo:

```python
chat_message = ChatMessageContent(role=AuthorRole.USER, content="This is the message content.")
await chat.add_chat_message(message=chat_message)
```

### Modos de conversação no AgentGroupChat
Os chats em grupo de agentes podem operar em dois modos distintos, dependendo dos requisitos da conversa:

Em conversas de turno único , um agente designado fornece uma resposta com base na entrada do usuário.

- Você pode invocar uma resposta de um chat de turno único usando AgentGroupChat.invokee especificando o agente que deve responder. Por exemplo:

```python
  async for message in chat.invoke(agent)
      # process message response(s)
```

Em conversas multi-turn , vários agentes se revezam respondendo, continuando a conversa até que uma condição de término seja atendida.

- As respostas dos agentes são retornadas de forma assíncrona à medida que são geradas, permitindo que a conversa se desenrole em tempo real.

- Você pode invocar uma resposta de um bate-papo multi-turno usando AgentGroupChat.invoke. Por exemplo:

```python
  async for message in chat.invoke()
      # process message response(s)
```
Ambos os modos permitem que os agentes colaborem com base nas respostas uns dos outros, resultando em interações dinâmicas e inteligentes.

## Crie uma estratégia de seleção de agentes
Um recurso fundamental do Semantic Kernel Agent Framework é o suporte a interações inteligentes e multiagentes. A colaboração entre agentes pode ser alcançada usando o AgentGroupChat, que possui alguns componentes críticos a serem considerados e que não são necessários com agentes únicos ou aplicações Semantic Kernel sem agentes.

As unidades a seguir discutem um exemplo de solução multiagente, em que temos dois agentes em um cenário de redator-revisor:

- Um agente redator que escreve conteúdo online, chamado CopywriterAgent.
- Um diretor de criação apenas revisando as propostas, chamado ReviewingDirectorAgent.

### Seleção de agentes
É importante escolher o agente mais adequado para responder à consulta de um usuário, especialmente em sistemas multiagentes, onde os agentes são especializados em domínios diferentes.

Por exemplo, se você conversar com os agentes solicitando um slogan para uma nova escova de limpeza, o ReviewingDirectorAgent não deve ser invocado para responder, pois eles não sabem escrever slogans. Em vez disso, pedir ao CopywriterAgent para responder forneceria ao usuário uma resposta precisa.

#### Por que a seleção de agentes é importante?
- Precisão: encaminhar consultas para o agente mais relevante garante respostas precisas.
- Eficiência: Reduz o tempo de processamento ao utilizar a expertise de agentes especializados.
- Escalabilidade: a seleção adequada permite que a estrutura lide com diversas consultas sem sobrecarregar os agentes individuais e fornece a melhor resposta ao usuário à medida que o número de agentes no chat aumenta.

### Como a estrutura seleciona os agentes?
#### Conversas de turno único

- Reconhecimento de intenção: a estrutura analisa a consulta do usuário para identificar a intenção e combiná-la com o agente mais relevante.
- Regras predefinidas: os desenvolvedores podem configurar regras de roteamento para direcionar consultas específicas a agentes designados em seu aplicativo.

#### Conversas multi-turno

- Rastreamento de contexto: a estrutura mantém um registro do histórico da conversa para entender a intenção do usuário e selecionar o agente apropriado.
- Alternância dinâmica: se o tópico mudar, a estrutura muda dinamicamente para um agente especializado no novo domínio no meio da conversa.

### Estratégia de seleção de agentes
Para agentes multi-turno, a seleção do agente é determinada por uma estratégia de seleção . A estratégia de seleção é definida dentro da estrutura, seja usando uma estratégia de seleção predefinida ou estendendo uma SelectionStrategyclasse para definir um comportamento de seleção personalizado. Você pode definir a estratégia de seleção ao criar o AgentGroupChatobjeto.

#### Estratégia de Seleção Sequencial
- A SequentialSelectionStrategyclasse oferece uma estratégia de seleção predefinida, em que a ordem de turno dos agentes é baseada na ordem em que os agentes foram adicionados ao chat. A opção de especificar um agente inicial também está disponível.

#### Estratégia de Seleção de Função do Kernel
- A KernelFunctionSelectionStrategyclasse permite que você defina sua estratégia de seleção criando uma função kernel a partir de um prompt. No nosso exemplo de escritor e revisor, o prompt da sua estratégia de seleção poderia ser:

```python
prompt=f"""
    Determine which participant takes the next turn in a conversation based on the most recent participant.
    State only the name of the participant to take the next turn.
    No participant should take more than one turn in a row.

    Choose only from these participants:
    - ReviewingDirectorAgent
    - CopywriterAgent

    Always follow these rules when selecting the next participant:
    - After user input, it is CopywriterAgent's turn.
    - After CopywriterAgent replies, it is ReviewingDirectorAgent's turn.
    - After ReviewingDirectorAgent provides feedback, it is CopywriterAgent's turn.

    History:
    {{$history}}
"""
```

Se sua interação preferida sempre deve ter um determinado agente respondendo primeiro, isso pode ser especificado em sua estratégia de seleção, conforme visto no prompt acima.

#### Classe base SelectionStrategy
- A SelectionStrategyclasse base contém um select_agentmétodo substituível onde você pode definir uma lógica personalizada para selecionar o próximo agente. O valor de retorno deve ser um agente presente no chat em grupo.

Depois de decidir sua estratégia de seleção, você pode atribuí-la ao selection_strategyparâmetro do AgentGroupChatobjeto.

### Truncando o histórico do bate-papo
Como a estratégia de seleção normalmente depende da última mensagem do chat para determinar o próximo agente, você pode truncar o histórico do chat para reduzir o uso de tokens e ajudar a melhorar o desempenho. O KernelFunctionSelectionStrategyaceita um history_reducerparâmetro que você pode especificar como:

```python
history_reducer = ChatHistoryTruncationReducer(target_count=1)
```
## Defina uma estratégia de encerramento de chat
Conversas multi-turn têm respostas retornadas de forma assíncrona, para que a conversa possa se desenvolver naturalmente. No entanto, os agentes precisam saber quando interromper uma conversa, o que é determinado pela estratégia de encerramento .

### Estratégia de rescisão
Uma estratégia de encerramento garante que conversas ou tarefas sejam concluídas adequadamente. Essa estratégia evita mensagens desnecessárias para o usuário, limita o uso de recursos e melhora a experiência geral do usuário.

Por exemplo, no cenário do agente redator-revisor, assim que o Agente DiretorRevisor analisa e aprova o slogan da escova de limpeza do Agente Redator , nós, humanos, sabemos que a conversa deve terminar. No entanto, se não definirmos quando encerrar a conversa, o Agente Redator continuará enviando slogans desnecessariamente.

### Por que usar uma estratégia de rescisão?
- Eficiência : Evita loops infinitos ou interações prolongadas, economizando recursos computacionais.
- Satisfação do usuário : os usuários recebem respostas concisas e relevantes, evitando frustrações com conversas muito longas.
- Conclusão do objetivo : O uso de um agente é concluir uma tarefa. Encerrando-a adequadamente. Ele confirma quando uma tarefa ou conversa atingiu o objetivo pretendido.

### Como a estrutura implementa estratégias de término?
Semelhante à forma como a estratégia de seleção é especificada, os desenvolvedores podem definir uma estratégia de encerramento ou usar uma estratégia predefinida. Cada estratégia de encerramento suporta um maximum_iterationsparâmetro que encerrará o chat após um número máximo de iterações. O valor padrão é 99 iterações. Cada estratégia de encerramento também requer os agentes que devem executá-la. No cenário de agente escritor-revisor, o ReviewingDirectorAgent deve determinar quando o chat deve ser encerrado.

#### Estratégia de Término Padrão

- A DefaultTerminationStrategyclasse só terminará após o número especificado de iterações máximas.

#### Estratégia de término da função do kernel

- A KernelFunctionTerminationStrategyclasse permite que você defina sua estratégia de encerramento criando uma função kernel a partir de um prompt. No nosso exemplo de escritor e revisor, o prompt da sua estratégia de seleção poderia ser:

```python
prompt="""
    Determine if the copy has been approved.  If so, respond with a single word: yes

    History:
    {{$history}}
    """
```

- Esta classe requer um result_parserparâmetro. A result_parseré uma função que processa a saída da sua função prompt para determinar se a condição de término foi atendida. Ela recebe a saída da função prompt e a processa para retornar Trueou False.

#### Classe base TerminationStrategy

- A TerminationStrategyclasse base contém um should_agent_terminatemétodo substituível onde você pode definir uma lógica personalizada para concluir o chat em grupo do agente. O valor de retorno deve ser um booleano. Por exemplo, você pode definir uma função de encerramento que verifica a entrada mais recente do histórico apenas para a palavra "sim". No entanto, você precisaria fornecer instruções explícitas ao seu agente para retornar a palavra-chave de encerramento.

Depois de decidir sua estratégia de término, você pode atribuí-la ao termination_strategyparâmetro do AgentGroupChatobjeto.

### Truncando o histórico do bate-papo
Como a estratégia de encerramento normalmente depende da última mensagem do chat para determinar se o chat deve ser encerrado, você pode truncar o histórico do chat para reduzir o uso de tokens e ajudar a melhorar o desempenho. O KernelFunctionTerminationStrategyaceita um history_reducerparâmetro que você pode especificar como:

```python
history_reducer = ChatHistoryTruncationReducer(target_count=1)
```

### Estado de conversação
Seja AgentGroupChatpara uma conversa de turno único ou múltiplo, o estado é atualizado para concluído quando atende aos critérios de encerramento. No entanto, você pode querer usar a instância de bate-papo em grupo novamente. Para continuar usando a mesma instância de bate-papo, você precisará redefinir o estado de conclusão para False. Sem uma redefinição de estado, o AgentGroupChatnão poderá aceitar novas interações.

Quando uma conversa atinge o número máximo de iterações permitidas, ela será encerrada, mas não será marcada como concluída . Nesse caso, você pode estender a conversa sem redefinir o estado da conversa.

Ao entender esses componentes, você pode utilizar melhor o Semantic Kernel Agent Framework para criar sistemas multiagentes inteligentes.

## Resumo
Neste módulo, você aprendeu como o Semantic Kernel Agent Framework permite que desenvolvedores criem agentes de IA colaborativos. Você aprendeu sobre seleção de agentes, colaboração multiagente e estratégias de término para entender como os agentes interagem, processam entradas e determinam o fluxo de conversas. Você também aprendeu como as estratégias de seleção e término garantem a eficiência e a conclusão de objetivos em fluxos de trabalho orientados por agentes. Ao aplicar esses conceitos e habilidades, você pode aproveitar o Semantic Kernel Agent Framework para criar soluções de IA dinâmicas e adaptáveis que aprimoram as interações do usuário e automatizam tarefas complexas.










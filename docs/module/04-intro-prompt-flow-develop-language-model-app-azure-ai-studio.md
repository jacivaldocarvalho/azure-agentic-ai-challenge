#  Introdução ao prompt flow para desenvolver aplicativos de modelo de linguagem no Estúdio de IA do Azure 

## Indice
- [Introdução ao prompt flow para desenvolver aplicativos de modelo de linguagem no Estúdio de IA do Azure](#introdução-ao-prompt-flow-para-desenvolver-aplicativos-de-modelo-de-linguagem-no-estúdio-de-ia-do-azure)
  - [Indice](#indice)
  - [Introdução](#introdução)
  - [Entenda o ciclo de vida de desenvolvimento de um aplicativo de modelo de linguagem grande (LLM)](#entenda-o-ciclo-de-vida-de-desenvolvimento-de-um-aplicativo-de-modelo-de-linguagem-grande-llm)
    - [Inicialização](#inicialização)
    - [Experimentação](#experimentação)
    - [Avaliação e refinamento](#avaliação-e-refinamento)
    - [Produção](#produção)
    - [Explore o ciclo de vida de desenvolvimento completo](#explore-o-ciclo-de-vida-de-desenvolvimento-completo)
  - [Compreender os componentes principais e explorar os tipos de fluxo](#compreender-os-componentes-principais-e-explorar-os-tipos-de-fluxo)
    - [Compreender um fluxo](#compreender-um-fluxo)
    - [Explorar as ferramentas disponíveis no prompt flow](#explorar-as-ferramentas-disponíveis-no-prompt-flow)
    - [Compreender os tipos de fluxos](#compreender-os-tipos-de-fluxos)
  - [Explorar conexões e runtimes](#explorar-conexões-e-runtimes)
    - [Explorar conexões](#explorar-conexões)
    - [Explorar runtimes](#explorar-runtimes)
  - [Explorar as variantes e as opções de monitoramento](#explorar-as-variantes-e-as-opções-de-monitoramento)
    - [Explorar variantes](#explorar-variantes)
    - [Implantar seu fluxo em um ponto de extremidade](#implantar-seu-fluxo-em-um-ponto-de-extremidade)
    - [Monitorar as métricas de avaliação](#monitorar-as-métricas-de-avaliação)
      - [Métrica](#métrica)
    - [Resumo](#resumo)

## Introdução
O verdadeiro poder dos Modelos de linguagem grandes (LLMs) está em sua aplicação. Se você deseja usar LLMs para classificar páginas da Web em categorias ou criar um chatbot em seus dados. Para aproveitar o poder das LLMs disponíveis, você precisa criar um aplicativo que combine suas fontes de dados com LLMs e gere a saída desejada.

Para desenvolver, testar, ajustar e implantar aplicativos LLM, você pode usar o fluxo de prompt, acessível no Azure Machine Learning Studio e no IA do Azure Studio.

![](https://learn.microsoft.com/pt-br/training/wwl-data-ai/get-started-prompt-flow-ai-studio/media/prompt-flow-feature.png)

 >Observação
O foco deste módulo é compreender e explorar o prompt flow através do Estúdio de IA do Azure. No entanto, note que o conteúdo se aplica à experiência de fluxo imediato tanto no Azure Machine Learning como no Azure AI Studio.

O prompt flow usa um prompt como entrada, que no contexto de LLMs, refere-se à consulta fornecida ao aplicativo LLM para gerar uma resposta. É o texto ou o conjunto de instruções fornecidas ao aplicativo LLM, solicitando que ele gere a saída ou execute uma tarefa específica.

Por exemplo, quando você quiser usar um modelo de geração de texto, o prompt pode ser uma frase ou um parágrafo que inicia o processo de geração. No contexto de um modelo de resposta a perguntas, o prompt pode ser uma consulta que solicita informações sobre um tópico específico. A eficácia do prompt geralmente depende de quão bem ele transmite a intenção do usuário e o resultado desejado.

O prompt flow permite que você crie fluxos, que se referem à sequência de ações ou etapas executadas para alcançar uma tarefa ou funcionalidade específica. Um fluxo representa o processo geral ou o pipeline que incorpora a interação com o LLM para resolver um caso de uso específico. O fluxo encapsula todo o percurso desde o recebimento de entrada até a geração de saída ou a execução de uma ação desejada.

## Entenda o ciclo de vida de desenvolvimento de um aplicativo de modelo de linguagem grande (LLM)
Entenda o ciclo de vida de desenvolvimento de um aplicativo de modelo de linguagem grande (LLM)

![](https://learn.microsoft.com/pt-br/training/wwl-data-ai/get-started-prompt-flow-ai-studio/media/development-lifecycle.png)

1. Inicialização: Defina o caso de uso e crie a solução.
2. Experimentação: Desenvolva um fluxo e teste com um pequeno conjunto de dados.
3. Avaliação e refinamento: Avalie o fluxo com um conjunto de dados maior.
4. Produção: Implante e monitore o fluxo e o aplicativo.

Durante a avaliação, o refinamento e a produção, você pode descobrir que sua solução precisa ser melhorada. Você pode voltar à experimentação e continuar desenvolvendo o fluxo até ficar satisfeito com os resultados.

Vamos explorar cada uma dessas fases com mais detalhes.

### Inicialização
Imagine que você deseja criar e desenvolver um aplicativo LLM para classificar artigos de notícias. Antes de começar a criar qualquer coisa, você precisa definir quais categorias você deseja como saída. Você precisa da aparência típica de um artigo de notícias, como apresentar o artigo como entrada para seu aplicativo e como o aplicativo gera a saída desejada.

Em outras palavras, durante a inicialização, você:

![](https://learn.microsoft.com/pt-br/training/wwl-data-ai/get-started-prompt-flow-ai-studio/media/initialization.png)

1. Define o objetivo
2. Coleta um conjunto de dados de exemplo
3. Cria um prompt básico
4. Cria o fluxo

Para criar, desenvolver e testar um aplicativo LLM, você precisa de um conjunto de dados de exemplo que serve como entrada. Um conjunto de dados de exemplo é um pequeno subconjunto representativo dos dados que você pretende analisar como entrada para seu aplicativo LLM.

Ao coletar ou criar o conjunto de dados de exemplo, você deve garantir a diversidade nos dados para abranger vários cenários e casos de borda. Você também deve remover informações confidenciais de privacidade do conjunto de dados para evitar vulnerabilidades.

### Experimentação
Você coletou um conjunto de dados de exemplo de artigos de notícias e decidiu em quais categorias deseja que os artigos sejam classificados. Você criou um fluxo que usa um artigo de notícias como entrada e usa um LLM para classificar o artigo. Para testar se o fluxo gera a saída esperada, execute-a no conjunto de dados de exemplo.

![](https://learn.microsoft.com/pt-br/training/wwl-data-ai/get-started-prompt-flow-ai-studio/media/experimentation.png)

A fase de experimentação é um processo iterativo durante o qual você (1) executa o fluxo em um conjunto de dados de exemplo. Em seguida, você (2) avalia o desempenho do prompt. Se você estiver (3) satisfeito com o resultado, poderá passar para avaliação e refinamento. Se você achar que há espaço para melhorias, poderá (4) modificar o fluxo alterando o prompt ou o próprio fluxo.

### Avaliação e refinamento
Quando estiver satisfeito com a saída do fluxo que classifica artigos de notícias, com base no conjunto de dados de exemplo, você poderá avaliar o desempenho do fluxo em relação a um conjunto de dados maior.

Ao testar o fluxo em um conjunto de dados maior, você pode avaliar o quão bem o aplicativo LLM generaliza para novos dados. Durante a avaliação, você pode identificar possíveis gargalos ou áreas para otimização ou refinamento.

Ao editar seu fluxo, primeiro você deve executá-lo em um conjunto de dados menor antes de executá-lo novamente em um conjunto de dados maior. Testar seu fluxo com um conjunto de dados menor permite que você responda mais rapidamente a quaisquer problemas.

Depois que seu aplicativo LLM parecer robusto e confiável no tratamento de vários cenários, você poderá mover o aplicativo LLM para produção.

### Produção
Por fim, seu aplicativo de classificação de artigo de notícias está pronto para produção.

![](https://learn.microsoft.com/pt-br/training/wwl-data-ai/get-started-prompt-flow-ai-studio/media/production.png)

Durante a produção, você:

1. Otimiza o fluxo que classifica os artigos de entrada para eficiência e eficácia.
2. Implanta seu fluxo em um ponto de extremidade. Quando você chama o ponto de extremidade, o fluxo é disparado para ser executado e a saída desejada é gerada.
3. Monitore o desempenho da solução coletando dados de uso e comentários do usuário final. Ao entender como o aplicativo é executado, você pode melhorar o fluxo sempre que necessário.

### Explore o ciclo de vida de desenvolvimento completo
Agora que você entende cada estágio do ciclo de vida de desenvolvimento de um aplicativo LLM, você pode explorar a visão geral completa:

![](https://learn.microsoft.com/pt-br/training/wwl-data-ai/get-started-prompt-flow-ai-studio/media/detailed-lifecycle.png)

## Compreender os componentes principais e explorar os tipos de fluxo
Para criar um aplicativo LLM (Grande Modelo de Linguagem) com prompt flow, você precisa entender os componentes principais do prompt flow.

### Compreender um fluxo
O prompt flow é um recurso no Estúdio de IA do Azure que permite criar fluxos. Os fluxos são fluxos de trabalho executáveis que geralmente consistem em três partes:

1. Entradas: Representa os dados passados para o fluxo. Podem ser diferentes tipos de dados, como cadeias de caracteres, inteiros ou boolianos.
2. Nós: Representam ferramentas que executam processamento de dados, execução de tarefas ou operações algorítmicas.
3. Saídas: Representa os dados produzidos pelo fluxo.

![](https://learn.microsoft.com/pt-br/training/wwl-data-ai/get-started-prompt-flow-ai-studio/media/flow-pipeline.png)

Semelhante a um pipeline, um fluxo pode consistir em vários nós que podem usar as entradas do fluxo ou qualquer saída gerada por outro nó. Você pode adicionar um nó a um fluxo escolhendo um dos tipos de ferramentas disponíveis.

### Explorar as ferramentas disponíveis no prompt flow
Três ferramentas comuns são:

- Ferramenta LLM: Habilita a criação de prompt personalizado utilizando Grandes Modelos de Linguagem.
- Ferramentas Python: Permite a execução de scripts personalizados do Python.
- Ferramenta de Prompt: Prepara os prompts como cadeias de caracteres para cenários complexos ou integração com outras ferramentas.

Cada ferramenta é uma unidade executável com uma função específica. Você pode usar uma ferramenta para executar tarefas como resumir texto ou fazer uma chamada à API. Você pode usar várias ferramentas dentro de um fluxo e usar uma ferramenta várias vezes.

Sempre que você adicionar um novo nó ao seu fluxo, adicionando uma nova ferramenta, você pode definir as entradas e saídas esperadas. Um nó pode usar uma das entradas de todo o fluxo, ou a saída de outro nó, vinculando efetivamente os nós.

Definindo as entradas, conectando nós e definindo as saídas desejadas, você pode criar um fluxo. Os fluxos ajudam você a criar aplicativos LLM para várias finalidades.

### Compreender os tipos de fluxos
Há três tipos diferentes de fluxos que você pode criar com o prompt flow:

- Fluxo padrão: Ideal para o desenvolvimento geral de aplicativos baseados em LLM, oferecendo uma variedade de ferramentas versáteis.
- Fluxo de chat: Projetado para aplicativos de conversa, com suporte aprimorado para funcionalidades relacionadas ao chat.
- Fluxo de avaliação: Focado na avaliação de desempenho, permitindo a análise e o aprimoramento de modelos ou aplicativos por meio de comentários sobre execuções anteriores.
  
Agora que você entende como um fluxo é estruturado e para que finalidade você pode usá-lo, vamos explorar como você pode criar um fluxo.

## Explorar conexões e runtimes
Ao criar um aplicativo LLM (Large Language Model) com prompt flow, primeiro você precisa configurar todas as conexões e runtimes necessários.

### Explorar conexões
Sempre que quiser que seu fluxo se conecte a uma fonte de dados, serviço ou API externa, você precisará que seu fluxo seja autorizado a se comunicar com esse serviço externo. Ao criar uma conexão, você configura um link seguro entre o prompt flow e os serviços externos, garantindo uma comunicação de dados perfeita e segura.

![](https://learn.microsoft.com/pt-br/training/wwl-data-ai/get-started-prompt-flow-ai-studio/media/connections.png)

Dependendo do tipo de conexão criado, a conexão armazena com segurança o ponto de extremidade, a chave de API ou as credenciais necessárias para que o prompt flow se comunique com o serviço externo. Os segredos necessários não são expostos aos usuários, mas são armazenados em um Azure Key Vault.

Ao configurar conexões, os usuários podem facilmente reutilizar serviços externos necessários para ferramentas nos fluxos deles.

Determinadas ferramentas internas exigem que você tenha uma conexão configurada:

| Tipo de conexão       | Ferramentas internas                          |
|------------------------|-----------------------------------------------|
| Open AI do Azure       | LLM ou Python                                 |
| Open AI                | LLM ou Python                                 |
| Cognitive Search       | Pesquisa de banco de dados de vetor ou Python |
| Serp                   | API do Serp ou Python                         |
| Custom                 | Python                                        |

As conexões de prompt flow desempenham funções fundamentais em dois cenários. Elas automatizam o gerenciamento de credenciais de API, simplificando e protegendo o tratamento de informações de acesso confidenciais. Além disso, elas permitem a transferência segura de dados de várias fontes, o que é crucial para manter a integridade e a privacidade dos dados em diferentes ambientes.

### Explorar runtimes
Depois de criar seu fluxo e configurar as conexões necessárias que suas ferramentas usam, você deseja executar seu fluxo. Para executar o fluxo, você precisa de computação, que é oferecida por meio de runtimes de prompt flow.

![](https://learn.microsoft.com/pt-br/training/wwl-data-ai/get-started-prompt-flow-ai-studio/media/runtimes.png)

Runtimes (1) são uma combinação de uma instância de computação (2) fornecendo os recursos de computação necessários e um ambiente (3) especificando os pacotes e bibliotecas necessários que precisam ser instalados antes que seja possível executar o fluxo.

Ao usar runtimes, você tem um ambiente controlado onde os fluxos podem ser executados e validados, garantindo que tudo funcione como pretendido em uma configuração estável. Um ambiente padrão está disponível para desenvolvimento e teste rápidos. Quando você precisar que outros pacotes sejam instalados, poderá criar um [ambiente personalizado](https://learn.microsoft.com/pt-br/azure/machine-learning/prompt-flow/how-to-customize-session-base-image?view=azureml-api-2).

## Explorar as variantes e as opções de monitoramento

Durante a produção, queira otimizar e implantar seu fluxo. Por fim, queira monitorar seus fluxos para entender quando é necessário melhorar seus fluxos.

É possível otimizar o fluxo usando variantes, implantar o fluxo em um ponto de extremidade e monitorar o fluxo avaliando as principais métricas.

### Explorar variantes
As variantes do prompt flows são versões de um nó de ferramenta com configurações distintas. Atualmente, as variantes só têm suporte na ferramenta LLM, em que uma variante pode representar um conteúdo de prompt ou uma configuração de conexão diferente. As variantes permitem que os usuários personalizem sua abordagem para tarefas específicas, como resumir artigos de notícias.

Alguns benefícios de usar variantes são:

- Melhorar a qualidade da sua geração de LLM: A criação de diversas variantes de um nó do LLM ajuda a encontrar o melhor prompt e as melhores configurações para um conteúdo de alta qualidade.
- Economizar tempo e esforço: As variantes permitem fácil gerenciamento e comparação de diferentes versões de prompt, simplificando o controle do histórico e reduzindo o esforço de ajuste do prompt.
- Aumentar a produtividade: Eles simplificam a otimização dos nós LLM, habilitando a criação e o gerenciamento mais rápidos de variações, levando a melhores resultados em menos tempo.
- Facilitar a fácil comparação: As variantes habilitam comparações de resultados lado a lado, auxiliando na escolha da variante mais eficaz com base em decisões controladas por dados.

### Implantar seu fluxo em um ponto de extremidade
Quando estiver satisfeito com o desempenho do fluxo, você poderá optar por implantá-lo em um ponto de extremidade online. Os pontos de extremidade são URLs que podem ser chamados de qualquer aplicativo. Quando você faz uma chamada à API para um ponto de extremidade online, pode esperar uma resposta (quase) imediata.

Ao implantar seu fluxo em um ponto de extremidade online, o prompt flow gera uma URL e uma chave para que você possa integrar seu fluxo com segurança a outros aplicativos ou processos de negócios. Quando você invoca o ponto de extremidade, um fluxo é executado e a saída é retornada em tempo real. Como resultado, a implantação de fluxos em pontos de extremidade pode, por exemplo, gerar respostas de chats ou o Copilot que você deseja retornar em outro aplicativo.

### Monitorar as métricas de avaliação
No prompt flow, o monitoramento das métricas de avaliação é fundamental para o reconhecimento do desempenho do seu aplicativo LLM, certificando-se de que elas atendam às expectativas do mundo real e entreguem resultados precisos.

Para entender se seu aplicativo está atendendo às necessidades práticas, é possível coletar comentários do usuário final e avaliar a utilidade do aplicativo. Outra abordagem para entender se sua aplicação está apresentando um bom desempenho é comparar as previsões do LLM com as respostas esperadas ou verdadeiras para avaliar a precisão e relevância. A avaliação das previsões do LLM é crucial para manter os aplicativos do LLM confiáveis e eficazes.

#### Métrica
As principais métricas usadas para o monitoramento da avaliação no prompt flow oferecem insights exclusivos sobre o desempenho dos LLMs:

- Fundamentação: Mede o alinhamento da saída do aplicativo LLM com a fonte de entrada ou o banco de dados.
- Relevância: Avalia a pertinência da saída do aplicativo LLM em relação à entrada fornecida.
- Coerência: Avalia o fluxo lógico e a legibilidade do texto do aplicativo LLM.
- Fluência: Avalia a precisão gramatical e linguística da saída do aplicativo LLM.
- Similaridade: Quantifica a correspondência contextual e semântica entre a saída do aplicativo LLM e a verdade fundamental.

Métricas como fundamentação, relevância, coerência, fluência e similaridade são fundamentais para garantir a qualidade, assegurando que as interações com seus aplicativos de LLM sejam precisas e eficazes. Sempre que seu aplicativo de LLM não tiver o desempenho conforme o esperado, você precisará voltar à experimentação para explorar iterativamente como melhorar seu fluxo.


### Resumo

Neste módulo, você aprendeu:

- O ciclo de vida de desenvolvimento ao criar aplicativos LLM.
- O que é um fluxo no prompt flow.
- Os componentes principais ao trabalhar com o prompt flow.

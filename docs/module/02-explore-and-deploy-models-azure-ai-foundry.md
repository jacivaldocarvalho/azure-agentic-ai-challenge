# Explore e implante modelos do catálogo de modelos no portal do Azure AI Foundry

Explore os vários modelos de linguagem disponíveis por meio do catálogo de modelos do Azure AI Foundry. Entenda como selecionar, implantar e testar um modelo e melhorar o seu desempenho.

## Índice

- [Explore e implante modelos do catálogo de modelos no portal do Azure AI Foundry](#explore-e-implante-modelos-do-catálogo-de-modelos-no-portal-do-azure-ai-foundry)
  - [Índice](#índice)
  - [Introdução](#introdução)
    - [Noções básicas sobre o processamento de idioma natural](#noções-básicas-sobre-o-processamento-de-idioma-natural)
    - [Entender a importância da arquitetura de Transformador](#entender-a-importância-da-arquitetura-de-transformador)
  - [Explorar os modelos de linguagem no catálogo de modelos](#explorar-os-modelos-de-linguagem-no-catálogo-de-modelos)
    - [Explorar o catálogo de modelos](#explorar-o-catálogo-de-modelos)
    - [Explorar modelos de linguagem](#explorar-modelos-de-linguagem)
    - [Compare benchmarks entre modelos](#compare-benchmarks-entre-modelos)
  - [Implantar um modelo em um ponto de extremidade](#implantar-um-modelo-em-um-ponto-de-extremidade)
    - [Entenda por que implantar um modelo](#entenda-por-que-implantar-um-modelo)
    - [Implantar um modelo de linguagem com o Azure AI Foundry](#implantar-um-modelo-de-linguagem-com-o-azure-ai-foundry)
  - [Melhorar o desempenho de um modelo de linguagem](#melhorar-o-desempenho-de-um-modelo-de-linguagem)
    - [Conversa com um modelo no playground](#conversa-com-um-modelo-no-playground)
    - [Aplicar engenharia de prompts](#aplicar-engenharia-de-prompts)
      - [Fornecer instruções claras: Seja específico sobre a saída desejada.](#fornecer-instruções-claras-seja-específico-sobre-a-saída-desejada)
      - [Formatar suas instruções: Use cabeçalhos e delineadores para facilitar a leitura da pergunta.](#formatar-suas-instruções-use-cabeçalhos-e-delineadores-para-facilitar-a-leitura-da-pergunta)
      - [Usar sugestões: Forneça palavras-chave ou indicadores de como o modelo deve iniciar sua resposta, como uma linguagem de codificação específica.](#usar-sugestões-forneça-palavras-chave-ou-indicadores-de-como-o-modelo-deve-iniciar-sua-resposta-como-uma-linguagem-de-codificação-específica)
    - [Atualizar a mensagem do sistema](#atualizar-a-mensagem-do-sistema)
      - [Usar uma tentativa ou algumas tentativas: Forneça um ou mais exemplos para ajudar o modelo a identificar um padrão desejado. Você pode adicionar uma seção à mensagem do sistema para adicionar um ou mais exemplos.](#usar-uma-tentativa-ou-algumas-tentativas-forneça-um-ou-mais-exemplos-para-ajudar-o-modelo-a-identificar-um-padrão-desejado-você-pode-adicionar-uma-seção-à-mensagem-do-sistema-para-adicionar-um-ou-mais-exemplos)
      - [Usar cadeia de pensamento: Guie o modelo para raciocinar passo a passo, instruindo-o a pensar na tarefa.](#usar-cadeia-de-pensamento-guie-o-modelo-para-raciocinar-passo-a-passo-instruindo-o-a-pensar-na-tarefa)
      - [Adicionar contexto: Aprimore a precisão do modelo fornecendo informações de contexto ou em segundo plano relevantes para a tarefa. Você pode fornecer contexto por meio de dados básicos fornecidos no prompt do usuário ou conectando sua própria fonte de dados.](#adicionar-contexto-aprimore-a-precisão-do-modelo-fornecendo-informações-de-contexto-ou-em-segundo-plano-relevantes-para-a-tarefa-você-pode-fornecer-contexto-por-meio-de-dados-básicos-fornecidos-no-prompt-do-usuário-ou-conectando-sua-própria-fonte-de-dados)
    - [Aplicar estratégias de otimização de modelo](#aplicar-estratégias-de-otimização-de-modelo)
  - [Resumo](#resumo)

## Introdução
Os modelos de base, como GPT-4, são modelos de processamento de linguagem natural de última geração projetados para entender, gerar e interagir com a linguagem humana. Para entender a importância dos modelos de base, é essencial explorar suas origens, que decorrem de avanços no campo de processamento de linguagem natural.

### Noções básicas sobre o processamento de idioma natural
O NLP (processamento de linguagem natural) é um tipo de IA (inteligência artificial) que se concentra na compreensão, interpretação e geração de linguagem humana. Alguns casos de uso comuns do NLP incluem:

- Conversão de fala em texto e conversão de texto em fala. Por exemplo, gerar legendas para vídeos.
- Tradução automática. Por exemplo, traduzir texto do inglês para o japonês.
- Classificação de textos. Por exemplo, rotular um email como spam ou não spam.
- Extração de entidade. Por exemplo, extrair palavras-chave ou nomes de um documento.
- Resumo de texto. Por exemplo, gerar um resumo curto de um parágrafo de um documento de várias páginas.
- Respostas às perguntas. Por exemplo, forneça respostas a perguntas como "Qual é a capital da França?"
de raciocínio. Por exemplo, resolva um problema matemático.

### Entender a importância da arquitetura de Transformador
O último avanço no processamento de linguagem natural (NLP) deve-se ao desenvolvimento da arquitetura de transformador.

Os transformadores foram introduzidos no [artigo Attention Is All You Need de Vaswani e outros, de 2017](https://arxiv.org/abs/1706.03762). A arquitetura de Transformador forneceu duas inovações ao NLP que resultaram no surgimento de modelos de base:

- Em vez de processar palavras sequencialmente, os Transformadores processam cada palavra de maneira independente e paralela usando a atenção.
- Além da similaridade semântica entre palavras, os Transformadores usam codificação posicional para incluir as informações sobre a posição de uma palavra em uma frase.

Os modelos de base projetados para casos de uso de NLP geralmente são chamados de **LLMs (Modelos de Linguagem Grandes)** ou modelos de linguagem. Neste módulo, você explorará os modelos de linguagem disponíveis, como selecionar um modelo para seu caso de uso e como usar um modelo de linguagem com a Azure AI Foundry. Você se concentra em modelos de linguagem que ajudam você a desenvolver aplicativos de IA generativa que servem como aplicativos de chat, que por sua vez respondem a perguntas dos seus usuários.

## Explorar os modelos de linguagem no catálogo de modelos
Selecionar um modelo de linguagem para seu aplicativo de IA generativa é importante, pois isso afeta o desempenho do aplicativo. Ao desenvolver um aplicativo de IA generativa com o Azure AI Foundry, você cria um aplicativo de chat que pode usar modelos de linguagem para várias finalidades:

- Para entender a pergunta do usuário.
- Para pesquisar o contexto relevante.
- Para gerar uma resposta para a pergunta do usuário.

No portal do Azure AI Foundry, você pode navegar pelos modelos de linguagem disponíveis no catálogo de modelos. Vamos explorar o catálogo de modelos e os tipos de modelo de linguagem disponíveis por meio da IA do Azure.

### Explorar o catálogo de modelos
 No portal do Azure AI Foundry, você pode navegar até o catálogo de modelos para explorar todos os modelos de linguagem disponíveis. Além disso, você pode importar qualquer modelo da biblioteca de software livre do Hugging Face para o catálogo de modelos.

 >Dica
 O Hugging Face é uma comunidade de software livre que disponibiliza modelos para o público. Você pode encontrar todos os modelos em seus [catálogos](https://huggingface.co/models). Além disso, você pode explorar a documentação para saber mais sobre como os modelos individuais funcionam, como o [BERT](https://huggingface.co/docs/transformers/main/model_doc/bert).

 ![Catalago de modelos](https://learn.microsoft.com/pt-br/training/wwl-data-ai/explore-models-azure-ai-studio/media/model-catalog.png)

 O catálogo de modelos do Azure AI Foundry se integra a modelos do Hugging Face e de outras fontes. Por meio do catálogo de modelos, você pode explorar, ajustar e implantar modelos.

>Importante!
A disponibilidade de modelos difere por local, também conhecida como região. Sua localização é especificada no nível do hub de IA. Ao criar um novo Hub de IA, você pode usar o Auxiliar de localização para especificar o modelo que deseja implantar para obter uma lista de locais em que você pode implantá-lo. Você também pode explorar a [tabela de resumo do modelo e a disponibilidade por região](https://learn.microsoft.com/pt-br/azure/ai-services/openai/concepts/models?tabs=global-standard%2Cstandard-chat-completions#model-summary-table-and-region-availability?azure-portal=true) para saber mais.

### Explorar modelos de linguagem
Os modelos de base ou de linguagem disponíveis no catálogo de modelos já são pré-treinados. Você pode implantar um modelo de linguagem em um ponto de extremidade ou ajustar um modelo para que ele tenha um desempenho melhor em uma tarefa especializada ou em conhecimentos específicos do domínio.

Seu modelo selecionado depende das preferências de caso de uso e implantação. Em primeiro lugar, você precisa pensar na tarefa que você deseja que o modelo execute. Por exemplo:

- Classificação de texto
- Classificação de token
- Respostas às perguntas
- Resumo
- Tradução
  
Alguns modelos de linguagem que normalmente são usados para várias tarefas são:

| Modelo                                            | Descrição                                                                                                                                                   |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BERT (Representações de codificador bidirecional de transformadores) | Focado na codificação de informações usando o contexto de antes e depois de um token (bidirecional). Normalmente usado quando você deseja ajustar um modelo para executar uma tarefa específica, como classificar texto e responder perguntas. |
| GPT (Transformador generativo pré-treinado)        | Treinado para criar texto coerente e contextualmente relevante e é mais comumente usado para tarefas como geração de texto e conclusões de chat.              |
| LLaMA (Meta AI de modelo de linguagem grande)      | Uma família de modelos criados pelo Meta. Ao treinar modelos LLaMA, o foco tem sido fornecer mais dados de treinamento do que aumentar a complexidade dos modelos. Você pode usar modelos LLaMA para geração de texto e conclusões de chat. |
| Phi-3-mini (variação de parâmetros 3.8B dos modelos phi) | Um modelo leve e de última geração otimizado para ambientes restritos a recursos e inferência local (como em um telefone), oferecendo suporte a prompts de contexto longo de até tokens 128k. Ele é desenvolvido com foco em segurança, alinhamento e aprendizado de reforço com o feedback humano. |

Depois de selecionar uma tarefa e filtrar os modelos disponíveis que são adequados para seu objetivo, você poderá revisar o resumo do modelo no Azure AI Foundry para levar em consideração outros aspectos

- Funcionalidades do modelo: Avalie os recursos do modelo de linguagem e quão bem eles se alinham com a sua tarefa. Por exemplo, um modelo como BERT é melhor para entender textos curtos.
- Pré-treinamento de dados: Considere o conjunto de dados usado para pré-treinar o modelo de linguagem. Por exemplo, o GPT-2 é treinado em conteúdo não filtrado da Internet que pode resultar em vieses.
- Limitações e preconceitos: Lembre-se de quaisquer limitações ou preconceitos que possam estar presentes no modelo de linguagem.
- Suporte a idiomas: explore quais modelos dão suporte a idiomas específicos ou a recursos multilíngues necessários para seu caso de uso.

### Compare benchmarks entre modelos
Ao explorar modelos de linguagem, você também pode comparar os parâmetros de comparação de modelo disponíveis para avaliar a qualidade dos modelos antes de implantar e integrar um modelo. Os parâmetros de comparação são como cartões de relatório para modelos de linguagem. Os parâmetros de comparação ajudam você a entender o desempenho de um modelo comparando-o com outros modelos usando testes ou tarefas específicas. Os modelos de parâmetros de comparação no portal do Azure AI Foundry fornecem uma lista coletada dos modelos de melhor desempenho para uma determinada tarefa, com base em métricas de modelos de parâmetros de comparação.

![benchmarks entre modelos](https://learn.microsoft.com/pt-br/training/wwl-data-ai/explore-models-azure-ai-studio/media/model-benchmarks.png)

Algumas métricas comumente usadas para avaliar o desempenho dos modelos de linguagem são:

| Métrica                    | Descrição                                                                                                                                                                                                                                      |
|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Precisão                   | As pontuações de precisão estão disponíveis no conjunto de dados e nos níveis de modelo. No nível do conjunto de dados, a pontuação é o valor médio de uma métrica de precisão computada em todos os exemplos no conjunto de dados. A métrica de precisão usada é exata em todos os casos, exceto no conjunto de dados HumanEval que usa uma métrica pass@1. A correspondência exata simplesmente compara o texto gerado pelo modelo com a resposta correta de acordo com o conjunto de dados, relatando um se o texto gerado corresponder exatamente à resposta e, caso contrário, zero. Pass@1 mede a proporção de soluções de modelo que passam por um conjunto de testes de unidade em uma tarefa de geração de código. No nível do modelo, a pontuação de precisão é a média das precisões no nível do conjunto de dados para cada modelo. |
| Coerência                  | A coerência avalia o quão bem o modelo de linguagem pode produzir resultados que fluem facilmente, são lidos naturalmente e se assemelham à linguagem humana.                                                                                  |
| Fluência                   | A fluência avalia a proficiência linguística da resposta prevista de uma IA generativa. Ela avalia a adequação do texto gerado às regras gramaticais, às estruturas sintáticas e ao uso adequado do vocabulário, resultando em respostas linguisticamente corretas e naturais. |
| Similaridade com GPT       | O GPTSimilarity é uma medida que quantifica a similaridade entre uma frase real (ou documento) e a frase de previsão gerada por um modelo de IA. Ele é calculado pela primeira vez calculando inserções em nível de frase usando a API de inserções para a verdade básica e a previsão do modelo. Essas incorporações são representações vetoriais de alta dimensão das frases, capturando seu significado semântico e contexto. |
| Fundamentação              | A aterramento mede o quão bem as respostas geradas do modelo de idioma se alinham com as informações da fonte de entrada.                                                                                                                    |
| Relevância                 | A relevância mede até que ponto as respostas geradas pelo modelo de linguagem são pertinentes e diretamente relacionadas às perguntas fornecidas.                                                                                             |

## Implantar um modelo em um ponto de extremidade
Ao desenvolver um aplicativo de IA generativa, você precisa integrar modelos de linguagem ao seu aplicativo. Para poder usar um modelo de linguagem, você precisa implantar o modelo. Vamos explorar como implantar modelos de linguagem no Azure AI Foundry, mas, primeiro, vamos entender por que devemos implantar um modelo.

### Entenda por que implantar um modelo
Os modelos de linguagem, assim como os modelos tradicionais de aprendizado de máquina, são projetados para gerar resultados com base em alguma entrada. Para se beneficiar de um modelo, você deseja uma solução que possa enviar entrada para um modelo, que o modelo processa e, em seguida, visualiza a saída em algum lugar.

Com os aplicativos de IA generativa, você tem um aplicativo de chat que espera entradas de dados de um usuário, geralmente na forma de uma pergunta. Você deseja que o modelo processe essa entrada e gere uma resposta que possa ser enviada de volta ao usuário por meio do aplicativo de chat. Para integrar um modelo de linguagem que possa processar dados de entrada e gerar dados de saída, você precisa que o modelo seja implantado em um ponto de extremidade.

Um ponto de extremidade é uma URL específica em que um modelo ou serviço implantado pode ser acessado. Ele funciona como um gateway para que os usuários enviem suas solicitações ao modelo e recebam os resultados. Cada implantação de modelo geralmente possui seu próprio ponto de extremidade exclusivo, permitindo que diferentes aplicativos se comuniquem com o modelo por meio de uma API (Interface de Programação de Aplicativo).

Ao implantar um modelo de linguagem do catálogo de modelos com o Azure AI Foundry, você recebe um ponto de extremidade que consiste em um URI de destino (Identificador Uniforme de Recursos) e uma chave exclusiva. Por exemplo, um URI de destino para um modelo GPT-3.5 implantado pode ser:

```
https://ai-aihubdevdemo.openai.azure.com/openai/deployments/gpt-35-turbo/chat/completions?api-version=2023-03-15-preview
```

O URI inclui o nome do hub de IA, o nome do modelo implantado e especifica o que você deseja que o modelo faça. No exemplo, o modelo GPT-3.5 é usado para conclusão do chat.

Para proteger seus modelos implantados, cada implantação vem com uma chave. Você só está autorizado a enviar e receber solicitações de e para o URI de destino se também fornecer a chave para autenticação.

Para usar um modelo implantado, você normalmente faz uma chamada à API. Você pode fazer uma chamada à API usando códigos como Python ou C#, ou uma ferramenta como o Azure AI Foundry ou o Postman. Uma chamada à API envolve o envio de uma solicitação ao ponto de extremidade do modelo usando a API. A solicitação geralmente inclui os dados de entrada que você deseja que o modelo processe. Em seguida, o modelo processará os dados e enviará uma resposta com os resultados. Dessa forma, você pode interagir com o modelo implantado e utilizar seus recursos em seus aplicativos.

Agora que você entendeu por que quer implantar um modelo, vamos explorar as opções de implantação no Azure AI Foundry.

### Implantar um modelo de linguagem com o Azure AI Foundry
Ao implantar um modelo de linguagem com o Azure AI Foundry, existem vários tipos disponíveis, dependendo do modelo que você quiser implantar:

- Serviço Azure OpenAI para implantar [modelos do Azure OpenAI](https://learn.microsoft.com/pt-br/azure/ai-services/openai/concepts/models?tabs=global-standard%2Cstandard-chat-completions).
- Inferência de modelo de IA do Azure para implantar [modelos e modelos do Azure OpenAI como um serviço](https://learn.microsoft.com/pt-br/azure/ai-foundry/model-inference/concepts/models).
- APIs sem servidor para implantar modelos [como um serviço](https://learn.microsoft.com/pt-br/azure/ai-foundry/how-to/model-catalog-overview#content-safety-for-models-deployed-via-serverless-apis?azure-portal=true).
- Computação gerenciada para implantar [modelos personalizados e de software livre](https://learn.microsoft.com/pt-br/azure/ai-foundry/how-to/model-catalog-overview#availability-of-models-for-deployment-as-managed-compute?azure-portal=true).

O custo associado dependerá do tipo de modelo que você implanta, qual opção de implantação você escolher e o que está fazendo com o modelo:

| Atividade                              | Modelos do OpenAI do Azure                                 | Inferência do modelo de IA do Azure                | Modelos implantados como APIs sem servidor (pagamento conforme o uso) | Modelos implantados com computação gerenciada pelo usuário                             |
|----------------------------------------|-----------------------------------------------------------|---------------------------------------------------|-------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| Implantar o modelo                     | Não, você não é cobrado por implantar um modelo do OpenAI do Azure em seu projeto. | Não, você não é cobrado por implantar um modelo do OpenAI do Azure em seu projeto. | Sim, há uma cobrança mínima pela infraestrutura do ponto de extremidade. | Sim, você é cobrado por minuto pela infraestrutura que hospeda o modelo.            |
| Chamar o ponto de extremidade          | Sim, você será cobrado com base no uso do token.           | Sim, você será cobrado com base no uso do token.    | Sim, você será cobrado com base no uso do token.                  | Nenhum.                                                                             |

## Melhorar o desempenho de um modelo de linguagem
Depois de implantar um modelo em um ponto de extremidade, você pode interagir com o modelo para explorar como ele se comporta. Quando você deseja que o modelo seja personalizado para seu caso de uso, há várias estratégias de otimização que você pode aplicar para melhorar o desempenho do modelo. Vamos explorar as várias estratégias.

### Conversa com um modelo no playground
Você pode usar sua linguagem de codificação preferida para fazer uma chamada à API para o ponto de extremidade do modelo ou conversar com o modelo diretamente no playground do Azure AI Foundry. O playground de chat é uma maneira rápida e fácil de experimentar e melhorar o desempenho do modelo.

![Playground para testar modelo](https://learn.microsoft.com/pt-br/training/wwl-data-ai/explore-models-azure-ai-studio/media/chat-playground.png)

A qualidade das perguntas enviadas para o modelo de linguagem influencia diretamente a qualidade das respostas que você recebe de volta. Você pode construir cuidadosamente sua pergunta ou prompt, para receber respostas melhores e mais interessantes. O processo de criação e otimização de prompts para melhorar o desempenho do modelo também é conhecido como **engenharia de prompt**. Quando um usuário final fornece prompts relevantes, específicos, sem ambiguidades e bem estruturados, o modelo pode entender melhor o contexto e gerar respostas mais precisas.

### Aplicar engenharia de prompts
Quando estiver conversando com o modelo no playground, você poderá aplicar várias técnicas de engenharia de prompt para explorar se isso melhora o resultado do modelo.

![](https://learn.microsoft.com/pt-br/training/wwl-data-ai/explore-models-azure-ai-studio/media/chat-with-model.png)

Vamos explorar algumas técnicas que um usuário final pode usar para aplicar a engenharia de prompt:

#### Fornecer instruções claras: Seja específico sobre a saída desejada.

![](https://learn.microsoft.com/pt-br/training/wwl-data-ai/explore-models-azure-ai-studio/media/clear-instructions.png)

#### Formatar suas instruções: Use cabeçalhos e delineadores para facilitar a leitura da pergunta.

![](https://learn.microsoft.com/pt-br/training/wwl-data-ai/explore-models-azure-ai-studio/media/format-instructions.png)

#### Usar sugestões: Forneça palavras-chave ou indicadores de como o modelo deve iniciar sua resposta, como uma linguagem de codificação específica.

![](https://learn.microsoft.com/pt-br/training/wwl-data-ai/explore-models-azure-ai-studio/media/use-cues.png)

### Atualizar a mensagem do sistema
No playground de chat, você pode exibir o JSON da conversa atual selecionando Mostrar JSON:

![](https://learn.microsoft.com/pt-br/training/wwl-data-ai/explore-models-azure-ai-studio/media/chat-json.png)

O JSON mostrado são os dados de entrada para o ponto de extremidade do modelo sempre que você envia uma nova mensagem. A mensagem do sistema sempre faz parte dos dados de entrada. Embora não esteja visível para os usuários finais, a mensagem do sistema permite que você, como desenvolvedor, personalize o comportamento do modelo fornecendo instruções para seu comportamento.

Algumas técnicas comuns de engenharia de prompt a serem aplicadas como desenvolvedor atualizando a mensagem do sistema são:

#### Usar uma tentativa ou algumas tentativas: Forneça um ou mais exemplos para ajudar o modelo a identificar um padrão desejado. Você pode adicionar uma seção à mensagem do sistema para adicionar um ou mais exemplos.

![](https://learn.microsoft.com/pt-br/training/wwl-data-ai/explore-models-azure-ai-studio/media/use-shots.png)

#### Usar cadeia de pensamento: Guie o modelo para raciocinar passo a passo, instruindo-o a pensar na tarefa.

![](https://learn.microsoft.com/pt-br/training/wwl-data-ai/explore-models-azure-ai-studio/media/chain-of-thought.png)

#### Adicionar contexto: Aprimore a precisão do modelo fornecendo informações de contexto ou em segundo plano relevantes para a tarefa. Você pode fornecer contexto por meio de dados básicos fornecidos no prompt do usuário ou conectando sua própria fonte de dados.

![](https://learn.microsoft.com/pt-br/training/wwl-data-ai/explore-models-azure-ai-studio/media/add-context.png)

### Aplicar estratégias de otimização de modelo
Como desenvolvedor, você também pode aplicar outras estratégias de otimização para melhorar o desempenho do modelo, sem precisar solicitar que o usuário final escreva prompts específicos. Além da engenharia de prompt, a estratégia escolhida depende de seus requisitos:

![](https://learn.microsoft.com/pt-br/training/wwl-data-ai/explore-models-azure-ai-studio/media/model-optimization.png)

- Otimizar para contexto: Quando o modelo não tem conhecimento contextual e você deseja maximizar a precisão das respostas.
- Otimizar o modelo: Quando você quiser melhorar o formato de resposta, o estilo ou a fala maximizando a consistência do comportamento.

Para otimizar o contexto, você pode aplicar um padrão Recuperação de **geração aumentada (RAG)**. Com o RAG, você fundamentar seus dados recuperando primeiro o contexto de uma fonte de dados, antes de gerar uma resposta. Por exemplo, você deseja que os clientes façam perguntas sobre hotéis que você está oferecendo em seu catálogo de reservas de viagens.

Quando quiser que o modelo responda em um formato ou estilo específico, você pode instruir o modelo a fazer isso adicionando diretrizes na mensagem do sistema. Quando você observar que o comportamento do modelo não é consistente, você pode impor ainda mais a consistência no comportamento ajustando um modelo. Com o ajuste fino, você treina um modelo de linguagem base em um conjunto de dados antes de integrá-lo em seu aplicativo.

Você também pode usar uma combinação de estratégias de otimização, como RAG e um modelo ajustado, para aprimorar o seu aplicativo de linguagem.

## Resumo
Neste módulo, aprendemos:

- Selecionar um modelo de linguagem no catálogo de modelos.
- implantar  um modelo em um ponto de extremidade.
- Testar um modelo e melhore o desempenho do modelo.
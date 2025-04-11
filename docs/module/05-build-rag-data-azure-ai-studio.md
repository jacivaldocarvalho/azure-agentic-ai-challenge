# Criar uma solução de copiloto baseada em RAG com seus próprios dados usando o Azure AI Studio

>Os co-pilotos podem trabalhar junto com você para fornecer sugestões, gerar conteúdo ou ajudá-lo a tomar decisões. Os copilots usam modelos de linguagem como uma forma de IA (inteligência artificial generativa) e responderão às suas perguntas usando os dados nos quais foram treinados. Para garantir que um copilot recupere informações de uma fonte específica, você pode adicionar seus próprios dados ao criar um copilot com o Azure AI Studio.

## Índice

- [Criar uma solução de copiloto baseada em RAG com seus próprios dados usando o Azure AI Studio](#criar-uma-solução-de-copiloto-baseada-em-rag-com-seus-próprios-dados-usando-o-azure-ai-studio)
  - [Índice](#índice)
  - [Introdução](#introdução)
    - [Solicitações e respostas sem aterramento](#solicitações-e-respostas-sem-aterramento)
    - [Solicitações e respostas com aterramento](#solicitações-e-respostas-com-aterramento)
  - [Entender como fundamentar o seu modelo de linguagem](#entender-como-fundamentar-o-seu-modelo-de-linguagem)
    - [Noções básicas sobre o RAG](#noções-básicas-sobre-o-rag)
    - [Adicionar dados de aterramento a um projeto de IA do Azure](#adicionar-dados-de-aterramento-a-um-projeto-de-ia-do-azure)
  - [Tornar seus dados pesquisáveis](#tornar-seus-dados-pesquisáveis)
    - [Como usar um índice de vetor](#como-usar-um-índice-de-vetor)
    - [Como criar um índice de pesquisa](#como-criar-um-índice-de-pesquisa)
    - [Como pesquisar um índice](#como-pesquisar-um-índice)
  - [Criar um copilot com o prompt flow](#criar-um-copilot-com-o-prompt-flow)
    - [Usando o padrão RAG em um prompt flow](#usando-o-padrão-rag-em-um-prompt-flow)
    - [Usar um exemplo para criar um fluxo de chat](#usar-um-exemplo-para-criar-um-fluxo-de-chat)
    - [Modificar a consulta com o histórico](#modificar-a-consulta-com-o-histórico)
    - [Pesquisar informações relevantes](#pesquisar-informações-relevantes)
    - [Gerar contexto de prompt](#gerar-contexto-de-prompt)
    - [Definir variantes de prompt](#definir-variantes-de-prompt)
    - [Chat com contexto](#chat-com-contexto)
  - [Resumo](#resumo)


## Introdução
Os modelos de linguagem estão crescendo em popularidade, pois criam respostas coerentes e impressionantes para as perguntas de um usuário. Especialmente quando um usuário interage com um modelo de linguagem por meio de chat, ele oferece uma maneira intuitiva de obter as informações necessárias.

Um desafio predominante na implantação de modelos de linguagem por meio de chat é a chamada fundamentalidade, que se refere ao fato de uma resposta estar enraizada, conectada ou ancorada na realidade ou em um contexto específico. Em outras palavras, a fundamentação refere-se ao fato de a resposta de um modelo de linguagem ser baseada em informações factuais.

### Solicitações e respostas sem aterramento
Quando você usa um modelo de linguagem para gerar uma resposta a uma solicitação, a única informação em que o modelo precisa basear a resposta vem dos dados nos quais ele foi treinado, que geralmente são apenas grandes quantidades de texto não contextualizado da Internet ou de alguma outra fonte.

![](https://learn.microsoft.com/pt-br/training/wwl-data-ai/build-copilot-ai-studio/media/ungrounded.png)

O resultado provavelmente será uma resposta gramaticalmente coerente e lógica à solicitação, mas como ele não está fundamentado em dados relevantes e fatos, ele não é especificado e pode de fato ser impreciso e incluir informações "inventadas". Por exemplo, a pergunta "Qual produto devo usar para fazer X?" pode incluir detalhes de um produto fictício.

### Solicitações e respostas com aterramento
Por outro lado, você pode usar uma fonte de dados para aterrar o prompt com algum contexto de fato relevante. Em seguida, a solicitação pode ser enviada para um modelo de linguagem, incluindo os dados de aterramento, para gerar uma resposta contextualizada, relevante e precisa.

![](https://learn.microsoft.com/pt-br/training/wwl-data-ai/build-copilot-ai-studio/media/grounded.png)

A fonte de dados pode ser qualquer repositório de dados relevantes. Por exemplo, você pode usar dados de um banco de dados do catálogo de produtos para aterrar o prompt "Qual produto devo usar para fazer X?" para que a resposta inclua detalhes relevantes dos produtos que existem no catálogo.

Neste módulo, você explorará como criar seu próprio aplicativo de modelo de linguagem baseado em chat que seja fundamentado, criando um copiloto com seus próprios dados.

## Entender como fundamentar o seu modelo de linguagem
Os modelos de linguagem se destacam na geração de texto envolvente e são ideais como base para copilotos. Os copilotos fornecem aos usuários um aplicativo intuitivo baseado em chat para receber assistência em seu trabalho. Ao projetar um copiloto para um caso de uso específico, você deseja garantir que seu modelo de linguagem seja fundamentado e use informações factuais relevantes para o que o usuário precisa.

Embora os modelos de linguagem sejam treinados em uma grande quantidade de dados, eles podem não ter acesso ao conhecimento que você deseja disponibilizar aos usuários. Para garantir que um copiloto seja fundamentado em dados específicos para fornecer respostas precisas e específicas do domínio, você pode usar a Geração Aumentada de Recuperação (RAG).

### Noções básicas sobre o RAG
RAG é uma técnica que você pode usar para fundamentar um modelo de linguagem. Em outras palavras, é um processo para recuperar informações que são relevantes para o prompt inicial do usuário. Em termos gerais, o padrão RAG incorpora as seguintes etapas:

![](https://learn.microsoft.com/pt-br/training/wwl-data-ai/build-copilot-ai-studio/media/rag-pattern.png)

1. Recuperar dados de aterramento com base no prompt inicial inserido pelo usuário.
2. Aumentar o prompt com dados de aterramento.
3. Use um modelo de linguagem para gerar uma resposta fundamentada.

Ao recuperar o contexto de uma fonte de dados especificada, você garante que o modelo de linguagem use informações relevantes ao responder, em vez de depender de seus dados de treinamento.

O uso de RAG é uma técnica poderosa e fácil de usar para muitos casos em que você deseja fundamentar seu modelo de linguagem e melhorar a precisão factual das respostas do seu copiloto.

### Adicionar dados de aterramento a um projeto de IA do Azure
Você pode usar o Estúdio de IA do Azure para criar um copiloto personalizado que use seus próprios dados para aterrar os prompts. O Estúdio de IA do Azure dá suporte a uma variedade de conexões de dados que você pode usar para adicionar dados a um projeto, incluindo:

- Armazenamento de Blobs do Azure
- Azure Data Lake Storage Gen2
- Microsoft OneLake

Você também pode carregar arquivos ou pastas no armazenamento usado pelo seu projeto do Estúdio de IA.

![](https://learn.microsoft.com/pt-br/training/wwl-data-ai/build-copilot-ai-studio/media/add-data.png)

## Tornar seus dados pesquisáveis
Quando você deseja criar um copilot que usa seus próprios dados para gerar respostas precisas, você precisa ser capaz de pesquisar seus dados com eficiência. Ao criar um copilot com o Estúdio de IA do Azure, você pode usar a integração com a Pesquisa de IA do Azure para recuperar o contexto relevante em seu fluxo de chat.

A Pesquisa de IA do Azure é um recuperador que você pode incluir ao criar um aplicativo de modelo de linguagem com o prompt flow. A Pesquisa de IA do Azure permite que você traga seus próprios dados, indexe seus dados e consulte o índice para recuperar as informações necessárias.

![](https://learn.microsoft.com/pt-br/training/wwl-data-ai/build-copilot-ai-studio/media/index.png)

### Como usar um índice de vetor
Embora um índice baseado em texto aprimore a eficiência da pesquisa, em geral, você pode obter uma melhor solução de recuperação de dados usando um índice baseado em vetor que contém inserções que representam os tokens de texto na fonte de dados.

Uma inserção é um formato especial de representação de dados que um mecanismo de pesquisa pode usar para localizar facilmente as informações relevantes. Mais especificamente, uma inserção é um vetor de números de ponto flutuante.

Por exemplo, imagine que você tenha dois documentos com o seguinte conteúdo:

- "As crianças brincavam alegremente no parque."
- "Garotos corriam felizes pelo playground."

Esses dois documentos contêm textos semanticamente relacionados, embora palavras diferentes sejam usadas. Ao criar inserções de vetor para o texto nos documentos, a relação entre as palavras no texto pode ser calculada matematicamente.

Imagine as palavras-chave que estão sendo extraídas do documento e plotadas como um vetor em um espaço multidimensional:

![](https://learn.microsoft.com/pt-br/training/wwl-data-ai/build-copilot-ai-studio/media/vector-embeddings.jpg)

A distância entre vetores pode ser calculada medindo o cosseno do ângulo entre dois vetores, também conhecido como similaridade de cosseno. Em outras palavras, a similaridade de cosseno calcula a similaridade semântica entre documentos e uma consulta.

Ao representar palavras e seus significados com vetores, você pode extrair contexto relevante da fonte de dados mesmo quando seus dados são armazenados em diferentes formatos (texto ou imagem) e idiomas.

Quando você quiser poder usar a busca em vetores para pesquisar seus dados, precisará criar inserções ao criar seu índice de pesquisa. Para criar inserções para o índice de pesquisa, você pode usar um modelo de inserção do OpenAI do Azure disponível no Estúdio de IA do Azure.

![](https://learn.microsoft.com/pt-br/training/wwl-data-ai/build-copilot-ai-studio/media/vector-index.png)

>Dica
Saiba mais sobre [inserções](https://learn.microsoft.com/pt-br/azure/ai-services/openai/concepts/understand-embeddings)

### Como criar um índice de pesquisa
Na Pesquisa de IA do Azure, um índice de pesquisa descreve como seu conteúdo é organizado para torná-lo pesquisável. Imagine uma biblioteca contendo muitos livros. Você deseja poder pesquisar pela biblioteca e recuperar o livro relevante de forma fácil e eficiente. Para tornar a biblioteca pesquisável, você cria um catálogo que contém todos os dados relevantes sobre livros para facilitar a localização de qualquer livro. O catálogo de uma biblioteca serve como o índice de pesquisa.

Embora existam diferentes abordagens para criar um índice, a integração da Pesquisa de IA do Azure no Estúdio de IA do Azure facilita a criação de um índice adequado para modelos de linguagem. Você pode adicionar seus dados ao Estúdio de IA do Azure, após o qual você pode usar a Pesquisa de IA do Azure para criar um índice no Estúdio de IA do Azure usando um modelo de inserção. O ativo de índice é armazenado na Pesquisa de IA do Azure e consultado pelo Estúdio de IA do Azure quando usado em um fluxo de chat.

![](https://learn.microsoft.com/pt-br/training/wwl-data-ai/build-copilot-ai-studio/media/create-index.png)

A forma como você configura seu índice de pesquisa depende dos dados que você tem e do contexto que você deseja que seu modelo de linguagem use. Por exemplo, a pesquisa de palavra-chave permite que você recupere informações que correspondam exatamente à consulta de pesquisa. A pesquisa semântica já dá um passo adiante recuperando informações que correspondem ao significado da consulta em vez da palavra-chave exata, usando modelos semânticos. Atualmente, a técnica mais avançada é a busca em vetores, que cria inserções para representar seus dados.

>Dica
Saiba mais sobre a [busca em vetores](https://learn.microsoft.com/pt-br/azure/search/vector-search-overview).

### Como pesquisar um índice
Há várias maneiras de consultar informações em um índice:

- Pesquisa de palavra-chave: Identifica documentos ou passagens relevantes com base em palavras-chave ou termos específicos fornecidos como entrada.
- Pesquisa semântica: Recupera documentos ou passagens compreendendo o significado da consulta e combinando-a com conteúdo semanticamente relacionado, em vez de depender apenas de correspondências exatas de palavra-chave.
- Busca em vetores: Usa representações matemáticas de texto (vetores) para encontrar documentos ou passagens semelhantes com base em seu significado semântico ou contexto.
- Pesquisa híbrida: Combina qualquer uma ou todas as outras técnicas de pesquisa. As consultas são executadas em paralelo e são retornadas em um conjunto de resultados unificado.

Ao criar um índice de pesquisa no Estúdio de IA do Azure, você será orientado a configurar um índice mais adequado para usar em combinação com um modelo de linguagem. Quando os resultados da pesquisa são usados em um aplicativo de IA generativa, a pesquisa híbrida fornece os resultados mais precisos.

A pesquisa híbrida é uma combinação de palavra-chave (e texto completo) e busca em vetores, à qual a classificação semântica é adicionada opcionalmente. Quando você cria um índice compatível com a pesquisa híbrida, as informações recuperadas são precisas quando correspondências exatas estão disponíveis (usando palavras-chave) e ainda relevantes quando apenas informações conceitualmente semelhantes podem ser encontradas (usando a busca em vetores).

>Dica
Saiba mais sobre a [pesquisa híbrida](https://learn.microsoft.com/pt-br/azure/search/hybrid-search-overview).

## Criar um copilot com o prompt flow

Depois de carregar dados no Estúdio de IA do Azure e criar um índice em seus dados usando a integração com a Pesquisa de IA do Azure, você pode implementar o padrão de RAG com o prompt flow para criar um aplicativo do copilot.

O prompt flow é uma estrutura de desenvolvimento para definir fluxos que orquestram interações com uma LLM.

![](https://learn.microsoft.com/pt-br/training/wwl-data-ai/build-copilot-ai-studio/media/prompt-flow.png)

Um fluxo começa com uma ou mais entradas, geralmente uma pergunta ou prompt inserido por um usuário e, no caso de conversas iterativas, o histórico de chat até esse ponto.

Em seguida, o fluxo é definido como uma série de ferramentas conectadas, cada uma das quais executa uma operação específica nas entradas e em outras variáveis ambientais. Há vários tipos de ferramenta que você pode incluir em um prompt flow para executar tarefas como:

- Executar código Python personalizado
- Pesquisar valores de dados em um índice
- Criar variantes de prompt – permitindo que você defina várias versões de um prompt para um LLM (modelo de linguagem grande), mensagens de sistema variadas ou texto de prompt e compare e avalie os resultados de cada variante.
- Enviar um prompt para uma LLM para gerar resultados.

Por fim, o fluxo tem uma ou mais saídas, normalmente para retornar os resultados gerados de uma LLM.

### Usando o padrão RAG em um prompt flow
A chave para usar o padrão RAG em um prompt flow é usar uma ferramenta Pesquisa de Índice para recuperar dados de um índice de modo que as ferramentas subsequentes no fluxo possam usar os resultados para aumentar o prompt usado para gerar saída de uma LLM.

![](https://learn.microsoft.com/pt-br/training/wwl-data-ai/build-copilot-ai-studio/media/rag-prompt-flow.png)

### Usar um exemplo para criar um fluxo de chat
O prompt flow fornece vários exemplos que você pode usar como ponto de partida para criar um aplicativo. Quando quiser combinar a RAG e um modelo de linguagem em seu aplicativo, você pode clonar o exemplo de Q&A de várias rodadas sobre seus dados.

O exemplo contém os elementos necessários para incluir a RAG e um modelo de linguagem:

![](https://learn.microsoft.com/pt-br/training/wwl-data-ai/build-copilot-ai-studio/media/chat-flow.png)

1. Anexar o histórico à entrada do bate-papo para definir um prompt na forma de uma pergunta contextualizada.
2. Procure informações relevantes de seus dados usando seu índice de pesquisa.
3. Gerar o contexto de prompt usando os dados recuperados do índice para aumentar a pergunta.
4. Criar variantes de prompt adicionando uma mensagem do sistema e estruturando o histórico de chat.
5. Enviar o prompt para um modelo de linguagem que gere uma resposta em linguagem natural.

Vamos examinar cada um desses elementos mais detalhadamente.

### Modificar a consulta com o histórico
A primeira etapa no fluxo é um nó de LLM (Modelo de Linguagem Grande) que usa o histórico de chat e a última pergunta do usuário e gera uma nova pergunta que inclui todas as informações necessárias. Ao fazer isso, você gera uma entrada mais sucinta que é processada pelo restante do fluxo.

### Pesquisar informações relevantes
Em seguida, você usa a ferramenta Pesquisa de Índice para consultar o índice de pesquisa criado com o recurso integrado da Pesquisa de IA do Azure e encontrar as informações relevantes a partir da sua fonte de dados.

### Gerar contexto de prompt
A saída da ferramenta Pesquisa de Índice é o contexto recuperado que você deseja usar ao gerar uma resposta ao usuário. Você deseja usar a saída em um prompt enviado para um modelo de linguagem, o que significa que você deseja analisar a saída em um formato mais adequado.

A saída da ferramenta Pesquisa de Índice pode incluir os n principais resultados (dependendo dos parâmetros definidos). Ao gerar o contexto de prompt, você pode usar um nó Python para iterar sobre os documentos recuperados da fonte de dados e combinar seu conteúdo e fontes em uma cadeia de caracteres de documento. A cadeia de caracteres será usada no prompt que você enviar para o modelo de linguagem na próxima etapa do fluxo.

### Definir variantes de prompt
Ao construir o prompt que deseja enviar para seu modelo de linguagem, você pode usar variantes para representar conteúdos de prompt diferentes.

Ao incluir a RAG no fluxo de chat, sua meta é fundamentar as respostas do chatbot. Além de recuperar o contexto relevante da fonte de dados, você também pode influenciar a fundamentação da resposta do chatbot instruindo-o a usar o contexto e buscar ser factual.

Com as variantes de prompt, você pode fornecer várias mensagens do sistema no prompt para explorar qual conteúdo fornece mais fundamentação.

### Chat com contexto
Por fim, você usa um nó LLM para enviar o prompt para um modelo de linguagem para gerar uma resposta usando o contexto relevante recuperado da sua fonte de dados. A resposta desse nó também é a saída de todo o fluxo.

Depois de configurar o fluxo de chat de exemplo para usar seus dados indexados e o modelo de linguagem de sua escolha, você pode implantar o fluxo e integrá-lo a um aplicativo para oferecer aos usuários uma experiência de copilot.

## Resumo
Neste módulo, você aprendeu a:

- Identifique a necessidade de ancorar seu modelo de linguagem com RAG (Geração Aumentada de Recuperação).
- Indexe seus dados com o Azure AI Search para torná-los pesquisáveis por modelos de linguagem.
- Crie um copiloto usando RAG em seus próprios dados no Azure AI Studio.


# **Criando um Aplicativo de IA Generativa com Seus Próprios Dados Usando RAG**

## Índice

- [**Criando um Aplicativo de IA Generativa com Seus Próprios Dados Usando RAG**](#criando-um-aplicativo-de-ia-generativa-com-seus-próprios-dados-usando-rag)
  - [Índice](#índice)
  - [**Introdução**](#introdução)
  - [**Pré-requisitos**](#pré-requisitos)
  - [**Passo 1: Criando um Projeto no Azure AI Foundry**](#passo-1-criando-um-projeto-no-azure-ai-foundry)
  - [**Passo 2: Implantando Modelos Necessários**](#passo-2-implantando-modelos-necessários)
  - [**Passo 3: Adicionando Dados Personalizados**](#passo-3-adicionando-dados-personalizados)
  - [**Passo 4: Criando um Índice de Busca**](#passo-4-criando-um-índice-de-busca)
  - [**Passo 5: Testando o Índice no Playground**](#passo-5-testando-o-índice-no-playground)
  - [**Passo 6: Criando um Aplicativo RAG com SDKs**](#passo-6-criando-um-aplicativo-rag-com-sdks)
    - [**Preparando a Configuração**](#preparando-a-configuração)
    - [**Executando o Aplicativo**](#executando-o-aplicativo)
  - [**Conclusão**](#conclusão)
  - [**Limpeza de Recursos**](#limpeza-de-recursos)
  - [**Referência**](#referência)

## **Introdução**  
Neste artigo, vamos explorar como criar um aplicativo de IA generativa que utiliza seus próprios dados por meio da técnica **Retrieval Augmented Generation (RAG)**. Essa abordagem permite integrar fontes de dados personalizadas em prompts para modelos de IA generativa, melhorando a precisão e relevância das respostas.  

Utilizaremos o **Azure AI Foundry** e os **SDKs do Azure OpenAI** para desenvolver uma solução que consulte documentos personalizados (neste caso, folhetos de viagem) e gere respostas contextualizadas.  


## **Pré-requisitos**  
- Uma conta **Azure** com acesso ao **Azure AI Foundry**.  
- Conhecimento básico de Python ou C# (dependendo da linguagem escolhida).  
- Pacotes necessários instalados (serão detalhados ao longo do artigo).  


## **Passo 1: Criando um Projeto no Azure AI Foundry**  

1. **Acesse o Portal Azure AI Foundry**:  
   - Abra [https://ai.azure.com](https://ai.azure.com) e faça login com suas credenciais Azure.  

2. **Crie um Novo Projeto**:  
   - Selecione **+ Create project**.  
   - Defina um nome para o projeto (ex: `my-ai-project`).  
   - Crie um novo **hub** com as seguintes configurações:  
     - **Hub name**: `my-ai-hub`  
     - **Subscription**: Sua assinatura Azure.  
     - **Resource group**: Crie um novo (ex: `my-ai-resources`).  
     - **Location**: Escolha uma região com suporte para `gpt-4` e `text-embedding-ada-002`.  
     - **AI Services**: Crie um novo recurso (ex: `my-ai-services`).  
     - **Azure AI Search**: Crie um novo recurso.  

3. **Revise e Crie o Projeto**:  
   - Confirme as configurações e selecione **Create**.  


## **Passo 2: Implantando Modelos Necessários**  

Para implementar o RAG, precisamos de dois modelos:  

1. **Modelo de Embedding** (`text-embedding-ada-002`):  
   - Vai vetorizar os dados para indexação e busca eficiente.  
   - Configurações:  
     - **Deployment name**: `text-embedding-ada-002`  
     - **Deployment type**: Standard  
     - **TPM Rate Limit**: 5K  

2. **Modelo de Geração de Respostas** (`gpt-4`):  
   - Responsável por gerar respostas baseadas nos dados recuperados.  
   - Configurações:  
     - **Deployment name**: `gpt-4`  
     - **Deployment type**: Standard  
     - **TPM Rate Limit**: 5K  


## **Passo 3: Adicionando Dados Personalizados**  

1. **Baixe os Dados de Exemplo**:  
   - Faça download dos folhetos de viagem em [https://github.com/MicrosoftLearning/mslearn-ai-studio/raw/main/data/brochures.zip](https://github.com/MicrosoftLearning/mslearn-ai-studio/raw/main/data/brochures.zip).  
   - Extraia os arquivos em uma pasta chamada `brochures`.  

2. **Adicione os Dados ao Projeto**:  
   - No Azure AI Foundry, vá para **Data + indexes**.  
   - Selecione **+ New data** e faça upload da pasta `brochures`.  


## **Passo 4: Criando um Índice de Busca**  

1. **Crie um Novo Índice**:  
   - Vá para **Data + indexes > Indexes**.  
   - Selecione **+ New index**.  
   - Configurações:  
     - **Data source**: `brochures`  
     - **Vector index**: `brochures-index`  
     - **Vector settings**: Habilite **vector search**.  
     - **Embedding model**: `text-embedding-ada-002`  

2. **Aguarde a Indexação**:  
   - Pode levar alguns minutos dependendo do volume de dados.  


## **Passo 5: Testando o Índice no Playground**  

1. **Acesse o Chat Playground**:  
   - No Azure AI Foundry, vá para **Playgrounds > Chat playground**.  

2. **Teste sem Dados Personalizados**:  
   - Envie a pergunta: *"Where can I stay in New York?"*  
   - Observe que a resposta é genérica.  

3. **Adicione o Índice e Teste Novamente**:  
   - No painel **Add your data**, selecione `brochures-index`.  
   - Reenvie a mesma pergunta e veja a resposta baseada nos folhetos.  


## **Passo 6: Criando um Aplicativo RAG com SDKs**  

### **Preparando a Configuração**  

1. **Obtenha a String de Conexão do Projeto**:  
   - No **Overview** do projeto, copie a **Project connection string**.  

2. **Configure o Ambiente de Desenvolvimento**:  
   - Abra o **Azure Cloud Shell** (PowerShell).  
   - Clone o repositório de exemplo:  
     ```bash
     git clone https://github.com/microsoftlearning/mslearn-ai-studio mslearn-ai-foundry
     ```  
   - Navegue até a pasta do projeto (Python ou C#).  

3. **Instale as Dependências**:  
   - **Python**:  
     ```bash
     pip install python-dotenv azure-ai-projects azure-identity openai
     ```  
   - **C#**:  
     ```bash
     dotnet add package Azure.Identity
     dotnet add package Azure.AI.Projects --prerelease
     dotnet add package Azure.AI.OpenAI --prerelease
     ```  

4. **Edite o Arquivo de Configuração**:  
   - Substitua os placeholders no arquivo `.env` (Python) ou `appsettings.json` (C#) com suas credenciais.  

### **Executando o Aplicativo**  

1. **Execute o Código**:  
   - **Python**:  
     ```bash
     python rag-app.py
     ```  
   - **C#**:  
     ```bash
     dotnet run
     ```  

2. **Teste o Chat**:  
   - Faça perguntas como:  
     - *"Where should I stay in London?"*  
     - *"What can I do there?"*  
   - Observe as respostas baseadas nos folhetos.  


## **Conclusão**  

Neste artigo, implementamos um aplicativo de IA generativa usando **RAG (Retrieval Augmented Generation)** no **Azure AI Foundry**. Aprendemos como:  

✅ Criar um projeto e implantar modelos.  
✅ Adicionar e indexar dados personalizados.  
✅ Desenvolver um aplicativo que consulta dados específicos para gerar respostas precisas.  

Essa abordagem é útil para chatbots, assistentes virtuais e outras aplicações que exigem respostas baseadas em informações confiáveis.  


## **Limpeza de Recursos**  

Para evitar custos desnecessários:  

1. Acesse o [Azure Portal](https://portal.azure.com).  
2. Exclua o **Resource Group** criado para este exercício.  

## **Referência**
[Create a generative AI app that uses your own data](https://microsoftlearning.github.io/mslearn-ai-studio/Instructions/04-Use-own-data.html)
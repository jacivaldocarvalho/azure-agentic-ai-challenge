# Desenvolvendo um Agente de IA com o Azure AI Foundry 

**Índice**  
- [Desenvolvendo um Agente de IA com o Azure AI Foundry](#desenvolvendo-um-agente-de-ia-com-o-azure-ai-foundry)
  - [Introdução](#introdução)
  - [Pré-requisitos](#pré-requisitos)
  - [Criando um Projeto no Azure AI Foundry](#criando-um-projeto-no-azure-ai-foundry)
  - [Implantando um Modelo de IA Generativa](#implantando-um-modelo-de-ia-generativa)
  - [Criando um Agente de IA](#criando-um-agente-de-ia)
  - [Testando o Agente](#testando-o-agente)
  - [Limpeza dos Recursos](#limpeza-dos-recursos)
  - [Conclusão](#conclusão)


## Introdução  
Neste artigo, exploraremos como criar um agente de IA simples usando o serviço **Azure AI Agent** no portal **Azure AI Foundry**. O agente será capaz de responder perguntas sobre políticas de reembolso de despesas com base em um documento fornecido.  

## Pré-requisitos  
- Acesso ao **Azure AI Foundry** ([https://ai.azure.com](https://ai.azure.com))  
- Credenciais do Azure  
- Documento da política de despesas (disponível para download)  

## Criando um Projeto no Azure AI Foundry  
Para começar, siga os passos abaixo:  

1. Acesse o portal **Azure AI Foundry** e faça login com suas credenciais do Azure.  
2. Feche quaisquer painéis de dicas ou início rápido que apareçam.  
3. Selecione **+ Criar projeto**.  
4. No assistente de criação:  
   - Defina um nome para o projeto (ex.: `meu-projeto-ia`).  
   - Escolha a opção de criar um novo hub.  
5. Personalize as configurações do hub:  
   - **Nome do hub**: Um nome exclusivo (ex.: `meu-hub-ia`).  
   - **Assinatura**: Sua assinatura do Azure.  
   - **Grupo de recursos**: Crie um novo ou selecione um existente.  
   - **Região**: Escolha entre `eastus`, `eastus2`, `swedencentral`, `westus` ou `westus3`.  
   - **Recursos de IA**: Crie um novo serviço de IA ou use um existente.  
   - **Azure AI Search**: Pule esta etapa.  
6. Revise as configurações e selecione **Criar**.  

## Implantando um Modelo de IA Generativa  
Após criar o projeto, implante um modelo de linguagem generativa:  

1. No menu à esquerda, vá para **Modelos + endpoints**.  
2. Na aba **Implantações de modelo**, selecione **Implantar modelo base**.  
3. Procure pelo modelo **gpt-4o** e confirme a seleção.  
4. Personalize a implantação com:  
   - **Nome da implantação**: Ex.: `gpt-4o`.  
   - **Tipo de implantação**: Global Standard.  
   - **Atualização automática de versão**: Habilitada.  
   - **Versão do modelo**: A mais recente disponível.  
   - **Recurso de IA conectado**: Selecione seu recurso do Azure OpenAI.  
   - **Limite de tokens por minuto**: 50K (ou o máximo permitido).  
   - **Filtro de conteúdo**: DefaultV2.  
5. Aguarde a conclusão da implantação.  

## Criando um Agente de IA  
Com o modelo implantado, crie um agente:  

1. Faça o download do documento **Expenses_policy.docx** [aqui](https://raw.githubusercontent.com/MicrosoftLearning/mslearn-ai-agents/main/Labfiles/01-agent-fundamentals/Expenses_Policy.docx).  
2. No portal **Azure AI Foundry**, vá para a página **Agentes**.  
3. Crie um novo agente (ou use um gerado automaticamente).  
4. Configure o agente:  
   - **Nome do agente**: `ExpensesAgent`.  
   - **Modelo implantado**: Selecione o `gpt-4o` implantado anteriormente.  
   - **Instruções**: "Responda perguntas relacionadas a reembolsos de despesas."  
5. Adicione conhecimento ao agente:  
   - Selecione **+ Adicionar** em **Conhecimento**.  
   - Crie um novo **armazenamento vetorial** chamado `Expenses_Vector_Store`.  
   - Faça upload do arquivo **Expenses_policy.docx**.  

## Testando o Agente  
Para verificar o funcionamento do agente:  

1. No painel de configuração do agente, selecione **Testar no playground**.  
2. Digite perguntas como:  
   - *"Qual é o valor máximo que posso reivindicar para refeições?"*  
   - *"E para hospedagem?"*  
3. Analise as respostas com base no documento carregado.  

## Limpeza dos Recursos  
Para evitar custos desnecessários:  

1. Acesse o **portal do Azure** ([https://portal.azure.com](https://portal.azure.com)).  
2. Navegue até o grupo de recursos criado.  
3. Selecione **Excluir grupo de recursos** e confirme.  

## Conclusão  
Neste artigo, você aprendeu a criar e configurar um agente de IA no **Azure AI Foundry**, utilizando um modelo generativo e dados de contexto para responder perguntas específicas. Experimente expandir o agente com mais funcionalidades ou integrações!
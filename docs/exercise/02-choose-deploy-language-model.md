# **Como Escolher e Implantar um Modelo de Linguagem no Azure AI Foundry**  

O **Azure AI Foundry** oferece um catálogo centralizado de modelos que permite explorar e utilizar diversas opções para criar cenários de IA generativa. Neste artigo, vamos guiá-lo passo a passo na escolha e implantação de um modelo de linguagem adequado para uma aplicação de resolução de problemas.  

## **Explorando o Catálogo de Modelos**  

O **catálogo de modelos do Azure AI Foundry** é um repositório onde você pode comparar e selecionar diferentes modelos para sua solução de IA generativa.  

Neste exercício, você irá:  
1. **Criar um hub e projeto no Azure AI Foundry**  
2. **Explorar e comparar modelos**  
3. **Implantar modelos**  
4. **Testar os modelos em um playground de chat**  


## **1. Criar um Hub e Projeto no Azure AI Foundry**  

Um **Azure AI hub** funciona como um espaço de trabalho colaborativo onde você pode gerenciar projetos. Vamos começar criando um hub e um projeto:  

1. Acesse o portal do **Azure AI Foundry** em [https://ai.azure.com](https://ai.azure.com) e faça login com suas credenciais do Azure.  
2. Na página inicial, selecione **+ Create project**.  
3. No assistente de criação:  
   - Defina um **nome para o projeto** (ex.: `meu-projeto-ai`).  
   - Selecione a opção para **criar um novo hub**.  
4. Personalize as configurações do hub:  
   - **Nome do hub**: Um nome único (ex.: `meu-hub-ai`).  
   - **Assinatura**: Sua assinatura do Azure.  
   - **Grupo de recursos**: Crie um novo (ex.: `meus-recursos-ai`) ou use um existente.  
   - **Localização**: Selecione **Help me choose** e escolha uma região recomendada (como aquela que suporta **GPT-4o**).  
   - **Azure AI Services ou Azure OpenAI**: Crie um novo recurso (ex.: `meus-servicos-ai`) ou use um existente.  
   - **Azure AI Search**: Pule esta configuração.  
5. Revise as configurações e selecione **Create**.  

> **Observação**: Recursos do Azure OpenAI têm cotas regionais. Se exceder o limite, você pode precisar criar um novo recurso em outra região.  


## **2. Configurar a Implantação do Serviço de Inferência**  

O **Azure AI Inference Service** permite implantar modelos em um endpoint comum, facilitando a comparação entre diferentes modelos.  

1. No portal do Azure AI Foundry, vá para **Preview features (📣)** e ative **Deploy models to Azure AI model inference service**.  
2. Feche o painel de recursos de visualização.  


## **3. Analisar Detalhes e Benchmarks dos Modelos**  

Para escolher o melhor modelo, você pode comparar métricas de desempenho.  

1. No painel esquerdo, selecione **Model catalog**.  
2. Pesquise por **GPT-4o** e visualize seus detalhes e benchmarks.  
3. Retorne ao catálogo e pesquise por **Phi-3.5-mini-instruct**, analisando suas métricas.  

### **Comparando Modelos Visualmente**  
1. No catálogo, selecione **Compare models**.  
2. Remova os modelos pré-selecionados e adicione **GPT-4o** e **Phi-3.5-mini-instruct**.  
3. Compare-os em métricas como:  
   - **Índice de Qualidade**  
   - **Custo**  
   - **Precisão**  
   - **Coerência**  
   - **Fluência**  
   - **Relevância**  


## **4. Implantar Modelos**  

Você pode implantar modelos de duas formas:  

### **Opção 1: Implantar pelo Catálogo de Modelos**  
1. No **Model catalog**, selecione **GPT-4o** e clique em **Deploy**.  
2. Personalize as configurações:  
   - **Nome da implantação**: `gpt-4o`  
   - **Tipo de implantação**: Global Standard  
   - **Atualização automática de versão**: Habilitada  
   - **Recurso de IA conectado**: Selecione seu recurso OpenAI  
   - **Limite de tokens por minuto (TPM)**: 50K  
   - **Filtro de conteúdo**: DefaultV2  
3. Aguarde a conclusão da implantação.  

### **Opção 2: Implantar por Models + Endpoints**  
1. No painel esquerdo, vá para **Models + endpoints**.  
2. Selecione **+ Deploy model → Deploy base model** e procure **Phi-3.5-mini-instruct**.  
3. Aceite a licença e configure:  
   - **Nome da implantação**: `phi-3.5-mini-instruct`  
   - **Tipo de implantação**: Global Standard  
4. Aguarde a implantação ser concluída.  


## **5. Testar os Modelos no Playground de Chat**  

Agora, vamos comparar o desempenho dos modelos em um cenário de resolução de problemas.  

### **Configurando o Chat**  
1. No painel esquerdo, selecione **Playgrounds → Chat playground**.  
2. No painel **Setup**, defina a instrução do sistema:  
   - **"You are an AI assistant that helps solve problems."**  
3. Aplique as alterações.  

### **Testando o GPT-4o**  
1. Selecione o modelo **GPT-4o**.  
2. Envie a seguinte pergunta:  
   ```  
   I have a fox, a chicken, and a bag of grain that I need to take over a river in a boat. I can only take one thing at a time. If I leave the chicken and the grain unattended, the chicken will eat the grain. If I leave the fox and the chicken unattended, the fox will eat the chicken. How can I get all three things across the river without anything being eaten?  
   ```  
3. Peça para explicar o raciocínio:  
   ```  
   Explain your reasoning.  
   ```  

### **Testando o Phi-3.5-mini-instruct**  
1. Selecione o modelo **Phi-3.5-mini-instruct**.  
2. Repita os mesmos prompts e compare as respostas.  

### **Desafio Adicional**  
Teste ambos os modelos com este problema (a resposta correta é **40!**):  
```  
I have 53 socks in my drawer: 21 identical blue, 15 identical black, and 17 identical red. The lights are out, and it is completely dark. How many socks must I take out to make 100 percent certain I have at least one pair of black socks?  
```  

---

## **Conclusão**  

Ao comparar modelos, é essencial equilibrar **desempenho** e **custo**. O **catálogo de modelos do Azure AI Foundry** e o **playground de chat** ajudam a tomar decisões informadas antes de implantar uma solução de IA generativa.  

### **Limpeza dos Recursos**  
Para evitar custos desnecessários:  
1. Acesse o **portal do Azure**.  
2. Vá para o **grupo de recursos** usado no exercício.  
3. Selecione **Delete resource group** e confirme a exclusão.  

Com este guia, você está pronto para explorar e implantar modelos de IA generativa no **Azure AI Foundry**! 🚀

## **Referência**
- [Choose and deploy a language model](https://microsoftlearning.github.io/mslearn-ai-studio/Instructions/02-Explore-model-catalog.html)
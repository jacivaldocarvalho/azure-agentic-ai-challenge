"""
Autor: Jacivaldo Carvalho
Data: 10/04/2025
Descrição: Script para enviar perguntas históricas a um modelo Azure OpenAI e
receber respostas como se fosse um professor de história.
"""

import os
from openai import AzureOpenAI
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env (opcional e seguro)
load_dotenv()

# Configurações da API - mantidas em variáveis de ambiente por segurança
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY")
api_version = "2024-12-01-preview"
deployment = "gpt-4o"

# Inicializa o cliente Azure OpenAI
client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
)

# Recebe a pergunta do usuário
pergunta = input("Faça sua pergunta sobre história: ")

# Chamada para o modelo
response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "Você é um professor de história que pode responder perguntas sobre eventos passados ​​ao redor do mundo.",
        },
        {
            "role": "user",
            "content": pergunta,
        }
    ],
    max_tokens=4096,
    temperature=1.0,
    top_p=1.0,
    model=deployment
)

# Exibe a resposta do modelo
print("\nResposta do professor de história:")
print(response.choices[0].message.content)
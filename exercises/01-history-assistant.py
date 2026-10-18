"""
Autor: Jacivaldo Carvalho
Data: 10/04/2025
Descrição: Script para enviar perguntas históricas a um modelo Azure OpenAI e
receber respostas como se fosse um professor de história.
"""

import os
import sys

from dotenv import load_dotenv
from openai import APIConnectionError, APIStatusError, APITimeoutError, AzureOpenAI


def main():
    # Carrega variáveis de ambiente do arquivo .env (opcional e seguro)
    load_dotenv()

    # Configurações da API - mantidas em variáveis de ambiente por segurança
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    subscription_key = os.getenv("AZURE_OPENAI_API_KEY")
    api_version = "2024-12-01-preview"
    deployment = "gpt-4o"

    missing = [
        name
        for name, value in (
            ("AZURE_OPENAI_ENDPOINT", endpoint),
            ("AZURE_OPENAI_API_KEY", subscription_key),
        )
        if not value or not value.strip()
    ]
    if missing:
        print("Missing required environment variables: " + ", ".join(missing), file=sys.stderr)
        return 1

    try:
        # Recebe a pergunta do usuário
        pergunta = input("Ask a history question: ").strip()
        if not pergunta:
            print("Please enter a non-empty question.", file=sys.stderr)
            return 1

        # Inicializa o cliente Azure OpenAI
        with AzureOpenAI(
            api_version=api_version,
            azure_endpoint=endpoint,
            api_key=subscription_key,
        ) as client:
            # Chamada para o modelo
            response = client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "Você é um professor de história que pode responder perguntas sobre eventos passados ​​ao redor do mundo.",
                    },
                    {"role": "user", "content": pergunta},
                ],
                max_tokens=4096,
                temperature=1.0,
                top_p=1.0,
                model=deployment,
            )

        if not response.choices or not response.choices[0].message.content:
            print("The model returned no text response.", file=sys.stderr)
            return 1

        # Exibe a resposta do modelo
        print("\nHistory teacher's answer:")
        print(response.choices[0].message.content)
        return 0
    except APITimeoutError:
        print("The Azure OpenAI request timed out. Try again later.", file=sys.stderr)
    except APIConnectionError:
        print("Could not connect to Azure OpenAI. Check your endpoint and network.", file=sys.stderr)
    except APIStatusError as exc:
        print(
            f"Azure OpenAI returned HTTP {exc.status_code}. "
            "Check credentials, deployment, API version, and quota.",
            file=sys.stderr,
        )
    except ValueError:
        print("Invalid Azure OpenAI configuration. Check your endpoint and API settings.", file=sys.stderr)
    except (EOFError, KeyboardInterrupt):
        print("\nInput cancelled.", file=sys.stderr)
        return 130
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

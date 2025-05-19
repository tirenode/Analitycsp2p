
from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    project=os.getenv("OPENAI_PROJECT_ID")
)

def ejecutar_agente(prompt: str) -> str:
    if not os.getenv("OPENAI_API_KEY"):
        return "Error: No se encontró la clave API de OpenAI."

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un asistente útil especializado en trading P2P."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error al ejecutar el agente: {str(e)}"

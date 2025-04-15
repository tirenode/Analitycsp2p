
from openai import OpenAI
import os
import logging

def ejecutar_agente(prompt: str) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "Error: No se encontró la clave API de OpenAI."

    try:
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Eres un asistente útil especializado en trading P2P"},
                {"role": "user", "content": prompt}
            ]
        )
        logging.info(f"Respuesta OpenAI: {response}")
        return response.choices[0].message.content
    except Exception as e:
        logging.error(f"Error al ejecutar el agente: {e}")
        return f"Error al ejecutar el agente: {e}"

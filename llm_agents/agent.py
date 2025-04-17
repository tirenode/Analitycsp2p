from openai import OpenAI
import os

def ejecutar_agente(prompt: str) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "Error: No se encontró la clave API de OpenAI."

    try:
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un asistente útil especializado en trading P2P."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print("Error detallado:", e)
        return f"Error al ejecutar el agente: {str(e)}"
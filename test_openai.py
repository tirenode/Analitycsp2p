
from openai import OpenAI
import os

try:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",  # Corregido de gpt-4o a gpt-4
        messages=[
            {"role": "user", "content": "¿Está funcionando correctamente la conexión con OpenAI?"}
        ]
    )
    print("Respuesta del modelo:", response.choices[0].message.content)
except Exception as e:
    print("Error de conexión con OpenAI:", e)

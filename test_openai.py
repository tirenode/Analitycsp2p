
import openai
import os
import traceback

client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    project=os.getenv("OPENAI_PROJECT_ID")
)

try:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Eres un asistente útil especializado en trading P2P."},
            {"role": "user", "content": "¿Qué es el arbitraje cripto P2P?"}
        ]
    )
    print("Respuesta del modelo:")
    print(response.choices[0].message.content)

except Exception as e:
    print("ERROR de conexión con OpenAI:")
    traceback.print_exc()

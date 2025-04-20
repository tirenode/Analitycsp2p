
import openai
import os
import json

def root(request):
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "API funcionando correctamente"})
    }

def handler(request):
    try:
        body = request.get_json()
        prompt = body.get("prompt", "")

        openai.api_key = os.environ.get("OPENAI_API_KEY")

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un asistente experto en trading P2P."},
                {"role": "user", "content": prompt}
            ]
        )

        return {
            "statusCode": 200,
            "body": json.dumps({"respuesta": response.choices[0].message.content})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }

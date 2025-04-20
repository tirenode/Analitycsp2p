from openai import OpenAI
import os
import json

def handler(request):
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "¡Bienvenido a AnalitycsP2P API en Vercel!"})
    }

    try:
        body = request.get_json()
        prompt = body.get("prompt", "")

        openai_api_key = os.environ.get("OPENAI_API_KEY")
        client = OpenAI(api_key=openai_api_key)

        response = client.chat.completions.create(
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
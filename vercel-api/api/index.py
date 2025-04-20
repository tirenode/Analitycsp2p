
import json

def handler(request):
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"message": "¡Bienvenido a AnalitycsP2P API en Vercel!"})
    }

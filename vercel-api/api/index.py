
def handler(request):
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": '{"message": "¡Bienvenido a Analitycsp2P API en Vercel!"}'
    }

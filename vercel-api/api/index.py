
def handler(request):
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": '{"message": "Bienvenido a AnalitycsP2P API en Vercel"}'
    }

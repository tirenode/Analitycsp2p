
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "AnalitycsP2P backend funcionando correctamente"}
import os
from fastapi import FastAPI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI()

@app.get("/")
def read_root():
    project_name = os.getenv("PROJECT_NAME", "Default Project")
    return {"message": f"{project_name} backend funcionando correctamente"}

@app.get("/check-env")
def check_env():
    return {
        "project_name": os.getenv("PROJECT_NAME") is not None,
        "openai_key": os.getenv("OPENAI_API_KEY") is not None
    }

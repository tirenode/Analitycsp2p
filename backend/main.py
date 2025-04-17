import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from pydantic import BaseModel
from llm_agents.agent import ejecutar_agente

# Load environment variables
load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    project_name = os.getenv("PROJECT_NAME", "Default Project")
    return {"message": f"{project_name} backend funcionando correctamente"}

@app.get("/check-env")
def check_env():
    api_key = os.getenv("OPENAI_API_KEY")
    return {
        "status": "ok" if api_key else "missing"
    }

class Prompt(BaseModel):
    prompt: str

@app.post("/ia")
def ejecutar_ia(data: Prompt):
    try:
        respuesta = ejecutar_agente(data.prompt)
        return {"respuesta": respuesta}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
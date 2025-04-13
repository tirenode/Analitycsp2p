
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "AnalitycsP2P backend funcionando correctamente"}
import os
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import sys
import os

# Add parent directory to path to allow imports from llm_agents
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from llm_agents.agent import ejecutar_agente

# Load environment variables
load_dotenv()

app = FastAPI()

@app.get("/")


@app.post("/agent")
async def run_agent(prompt: str):
    try:
        result = ejecutar_agente(prompt)
        return {"response": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def read_root():
    project_name = os.getenv("PROJECT_NAME", "Default Project")
    return {"message": f"{project_name} backend funcionando correctamente"}

@app.get("/check-env")
def check_env():
    return {
        "project_name": os.getenv("PROJECT_NAME") is not None,
        "openai_key": os.getenv("OPENAI_API_KEY") is not None
    }

from pydantic import BaseModel

class Prompt(BaseModel):
    prompt: str

@app.post("/ia")
def ejecutar_ia(data: Prompt):
    try:
        respuesta = ejecutar_agente(data.prompt)
        return {"respuesta": respuesta}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

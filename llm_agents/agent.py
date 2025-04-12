
import os
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType

def ejecutar_agente(prompt: str) -> str:
    # Get API key from environment
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    
    # LLM Model setup
    llm = ChatOpenAI(temperature=0.4, model_name="gpt-3.5-turbo", openai_api_key=OPENAI_API_KEY)
    
    # Base test tool
    def tool_saludo(nombre: str) -> str:
        return f"Hola {nombre}, soy tu copiloto IA en AnalitycsP2P."

    tools = [
        Tool(
            name="Saludador",
            func=tool_saludo,
            description="Devuelve un saludo personalizado"
        )
    ]

    # Agent initialization
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    
    return agent.run(prompt)

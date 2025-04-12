
import os
from langchain.agents import initialize_agent, Tool
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType

# Modelo LLM
llm = ChatOpenAI(
    temperature=0.4,
    model_name="gpt-3.5-turbo",
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

# Tool de prueba
def tool_saludo(nombre: str) -> str:
    return f"Hola {nombre}, soy tu copiloto IA en AnalitycsP2P."

tools = [
    Tool(
        name="Saludador",
        func=tool_saludo,
        description="Saluda a un usuario por su nombre."
    )
]

# Inicializar agente
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Función pública para ejecutar el agente
def ejecutar_agente(prompt: str) -> str:
    return agent.run(prompt)

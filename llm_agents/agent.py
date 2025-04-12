
import os
from langchain_community.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType

def ejecutar_agente(prompt: str) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "Error: No se encontró la clave API de OpenAI. Por favor configura la variable de entorno OPENAI_API_KEY"
    
    try:
        # Modelo LLM
        llm = ChatOpenAI(
            temperature=0.4,
            model_name="gpt-3.5-turbo",
            openai_api_key=api_key
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

        return agent.run(prompt)
    except Exception as e:
        return f"Error al ejecutar el agente: {str(e)}"

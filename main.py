from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from tools import search_tool, wiki_tool
# from langchain_ollama import ChatOllama
#from langchain_openai import ChatOpenAI

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str = Field(description="Toma principal de la investigación")
    sources: list[str] = Field(description="Fuentes consultadas durante la investigación")
    summary: str = Field(description="Resumen de la investigación")
    tools_used: list[str] = Field(description="Herramientas utilizadas por el agente")

llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash", temperature=0, max_retries=5)
tools = [search_tool, wiki_tool]
agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="""
You are a research assistant that generates research papers.

Answer the user's query clearly and accurately.
Use the available tools when necessary.
Do not invent sources.
""",
    response_format=ResearchResponse,
)

user_input = input("¿Qué deseas investigar? ")

try:
    res = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": user_input,
                }
            ]
        }
    )
    research = res.get("structured_response")
    
    if research is None:
        print("Error: no se generó una respuesta estructurada.")
    else:
        print("Tema:", research.topic)
        print("Resumen:", research.summary)
        print("Fuentes:", research.sources)
        print("Herramientas utilizadas:", research.tools_used)
except Exception as error:

    print("Ocurrió un error", error)



# llm = ChatOllama(
#     model="mistral-small3.2:24b",
#     temperature=0,
# )

# response = llm.invoke("Cuales son los mejores de programacion?")
# print(response.content.strip('*'))


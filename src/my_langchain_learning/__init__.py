import tavily
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from tavily import TavilyClient

load_dotenv()

tavily = TavilyClient()

@tool
def search(query: str) -> str:
    """
    Tool that searches over internet
    Args:
        query: The query to search for
    Returns:
        The search result
    """
    print(f"Searching for {query}")
    return tavily.search(query=query)


llm = ChatOllama(temperature=0,model="gpt-oss")
tools = [search]
agent = create_agent(model=llm,tools=tools)

def main() -> None:
    print("Hello from my-langchain-learning!")
    result = agent.invoke({"messages":HumanMessage(content="What is the current gold price in India?")})
    print(result)


if __name__ == "__main__":
    main()

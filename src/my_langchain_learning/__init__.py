from typing import List
from langchain.agents.structured_output import ToolStrategy
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch

load_dotenv()

class Source(BaseModel):
    """Schema for a source used by the agent"""

    url: str = Field(description="The URL of the source")


class AgentResponse(BaseModel):
    """Schema for agent response with answer and sources"""

    answer: str = Field(description="Thr agent's answer to the query")
    sources: List[Source] = Field(
        default_factory=list, description="List of sources used to generate the answer"
    )


llm = ChatOllama(temperature=0, model="gpt-oss")
tools = [TavilySearch(max_results=3, include_answer=True)]
agent = create_agent(model=llm, tools=tools, response_format=ToolStrategy(AgentResponse))


def main() -> None:
    print("Hello from my-langchain-learning!")
    result = agent.invoke({"messages": HumanMessage(
        content="Search LinkedIn for 3 currently open AI Engineer job vacancies in India requiring LangChain, and list the job title, company, location, and application URL.")})
    print(result)



if __name__ == "__main__":
    main()

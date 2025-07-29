from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langgraph.prebuilt import create_react_agent
from langgraph_swarm import create_swarm

wikipedia_agent = create_react_agent(
    model="openai:gpt-4.1-nano",
    tools=[WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())],
    prompt="You are a helpful assistant that searches wikipedia",
    name="wikipedia_agent",
)

graph = create_swarm(
    agents=[wikipedia_agent],
    default_active_agent="wikipedia_agent",
).compile()

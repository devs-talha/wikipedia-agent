from langchain_community.agent_toolkits.openapi.toolkit import RequestsToolkit
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.utilities.requests import TextRequestsWrapper
from langchain_core.callbacks import CallbackManagerForToolRun
from langchain_core.tools import BaseTool
from langgraph.prebuilt import create_react_agent
from langgraph_swarm import create_handoff_tool, create_swarm

headers = {
    "user-agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/119.0.0.0 Safari/537.36"
    ),
    "accept": "*/*",
}

toolkit = RequestsToolkit(
    requests_wrapper=TextRequestsWrapper(), allow_dangerous_requests=True
)
requests_tools = toolkit.get_tools()

transfer_to_wikipedia_agent = create_handoff_tool(
    agent_name="wikipedia_agent",
    description="Transfer the task to the wikipedia agent.",
)

transfer_to_local_directories_agent = create_handoff_tool(
    agent_name="local_directories_agent",
    description="Transfer the task to the local directories agent.",
)

wikipedia_agent = create_react_agent(
    model="openai:gpt-4.1-nano",
    tools=[WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())],
    prompt="You are a helpful assistant that searches wikipedia",
    name="wikipedia_agent",
)

init_agent = create_react_agent(
    model="openai:gpt-4.1-nano",
    tools=[transfer_to_wikipedia_agent, transfer_to_local_directories_agent],
    prompt="""
    Your job is to delegate the task to the appropriate agent based on the
    current state.
    You are not supposed to perform any action on your own.
    You can only delegate the task to the appropriate agent.
    If you are not sure about the task, stop the execution.
    """,
    name="init_agent",
)


class ListDirectory(BaseTool):
    """Tool that lists the contents of a directory."""

    name: str = "list_directory"
    description: str = "List the contents of a directory."

    def _run(
        self,
        query: str,
        run_manager: CallbackManagerForToolRun | None = None,
    ) -> list[str]:
        """Use the Wikipedia tool."""
        import os

        return os.listdir(query)


list_directory = ListDirectory()

local_directories_agent = create_react_agent(
    model="openai:gpt-4.1-nano",
    tools=[list_directory],
    prompt="You are a helpful assistant that lists the contents of a directory.",
    name="local_directories_agent",
)

graph = create_swarm(
    agents=[init_agent, wikipedia_agent, local_directories_agent],
    default_active_agent="init_agent",
).compile()

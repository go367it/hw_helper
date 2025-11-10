from langgraph.graph import StateGraph, START, END
import asyncio
from typing import TypedDict, Annotated
from reading_file import read_file
from pathlib import Path

# maingraph node for 
def maingraph():

    # state 
    class State(TypedDict):
        llm_response: str
        messages: Annotated

    graph_builder = StateGraph(State)

    # node for llm call
    async def first_node(state: State):
        
        file_path = Path("file.txt")
        response = read_file(file_path)

        return {"llm_response" : response}


    # adding node
    graph_builder.add_node("first_node", first_node)

    # adding edges
    graph_builder.add_edge(START, "first_node")
    graph_builder.add_edge("first_node", END)

    graph = graph_builder.compile()

    return graph

if __name__ == "__main__":

    graph = maingraph()

    print(graph)

    # asyncio.run(maingraph())
    
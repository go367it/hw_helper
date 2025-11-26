from langgraph.graph import StateGraph, START, END
from typing import TypedDict
from reading_file import read_file
from pathlib import Path
from rich import print
from llm_call import calling_llm


# maingraph node for 
async def category_graph():

    # state 
    class State(TypedDict):
        llm_response: str
        
    
    graph_builder = StateGraph(State)

    # node for llm call
    async def first_node(state: State):

        try:
            prompt : str = "Hi, how are you!"  
            response = calling_llm(prompt)

            # print(response)
            print(response.choices[0].message.content) # type: ignore
            
        except Exception as e:
            print(f"Error Occurred! \n {e}")
        
        # to fetch the type of file
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

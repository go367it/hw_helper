from langgraph.graph import StateGraph, START, END
import asyncio
from typing import TypedDict, Annotated
from reading_file import read_file
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI
import os
from rich import print

# Load the .env file
load_dotenv()

# maingraph node for 
async def maingraph():

    # state 
    class State(TypedDict):
        llm_response: str
        

    graph_builder = StateGraph(State)

    # node for llm call
    async def first_node(state: State):

        try:
            # Fetch API key
            print("Calling open ai for response! \n")
            client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

            # Make a sample request
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": "Hello, world!"}]
            )

            print(response.choices[0].message.content)
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


async def main():
    graph = await maingraph()  # ✅ Await the coroutine

    initial_state = {
        "llm_response": ""
    }

    result = await graph.ainvoke(initial_state)  # type: ignore # ✅ Await async invocation
    print(result)

if __name__ == "__main__":
    
    asyncio.run(main())

import asyncio
from logical_grouping import category_graph


async def main():
    graph = await category_graph()  # Await the coroutine

    initial_state = {
        "llm_response": ""
    }

    result = await graph.ainvoke(initial_state)  # type: ignore # Await async invocation
    # print(result)

if __name__ == "__main__":
    
    asyncio.run(main())

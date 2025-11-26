from openai import OpenAI
from dotenv import load_dotenv
import os
import time
from rich import print

load_dotenv()


def calling_llm(prompt: str, max_retry : int = 4, delay : int = 5):   

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # retry logic 
    for attempt in range (1, max_retry + 1):
        # Make a request
        try:
            response = client.chat.completions.create(
                model="gpt-5-nano",
                messages=[{
                    "role": "user", 
                    "content": prompt
                }]
            )

            return response
        
        except  Exception as e:
            print(f"Trial {attempt} \n")
            print(f"Error: {e} \n")
            if attempt == max_retry:
                raise  # rethrow after max attempts

            time.sleep(delay) # wait before retrying




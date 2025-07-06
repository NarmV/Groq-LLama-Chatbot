from groq import Groq
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("GROQ")
client = Groq(api_key=api_key)


def call_llm(user_qry):
    completion = client.chat.completions.create(
    model="meta-llama/llama-4-maverick-17b-128e-instruct",
    messages=[
      {
        "role": "user",
        "content": user_qry
      }
    ],
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)
 
    for chunk in completion:
      print(chunk.choices[0].delta.content or "", end="")
      

 

while True:
    user_qry = input("\nEnter your query: ")
    call_llm(user_qry)

 

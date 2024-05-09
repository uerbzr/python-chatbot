import openai
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

configure()

openai.api_key = os.getenv()

def chat(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user", "content":"prompt"}]
    )
    
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "q", "quit"]:
            break
        
        response = chat(user_input)
        print("Mother: ", response)
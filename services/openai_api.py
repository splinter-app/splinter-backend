from openai import OpenAI
from config import settings

client = OpenAI()
client.api_key = settings.openai_api_key

def openai_query(prompt: str):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )

    return response.choices[0].message.content

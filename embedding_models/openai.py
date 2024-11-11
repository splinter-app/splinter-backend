from openai import OpenAI
from config import settings

# Load the OpenAI model
model_name = settings.embedding_model_name

def openai_embed(question: str) -> list:
  client = OpenAI()
  client.api_key = settings.openai_api_key

  response = client.embeddings.create(
    input=question,
    model=model_name
  )

  return response.data[0].embedding
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from config import settings
from embedding_models import openai_embed
from db import pinecone_similarity_search
from services import openai_query
from utils import generate_prompt

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

class PromptRequest(BaseModel):
  question: str

@app.get('/')
async def index() -> dict[str, str]:
  return {"message": "Hello World!"}

@app.post('/sandbox/prompt')
async def prompt(request: PromptRequest):
  question = request.question

  # Step 1: Convert question into vector using the same embedding model as used by the vector DB
  embedding = openai_embed(question)

  # Step 2: Perform similarity search using vectorized question to retrieve relevants chunks of data
  context = pinecone_similarity_search(embedding)

  # Step 3: Make OpenAI API call with user question and with retrieved data as context
  prompt = generate_prompt(question, context)
  response = openai_query(prompt)

  # Step 4: Return answer and relevant chunks of data to frontend
  return {"question": question, "response": response , "prompt": prompt, "context": context}

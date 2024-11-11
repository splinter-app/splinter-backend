from sentence_transformers import SentenceTransformer
from config import settings

# Load the Hugging Face model
model_name = settings.embedding_model_name

def hugging_face_embed(question: str) -> list:
  model = SentenceTransformer(model_name)

  # Get the embedding (vector) for the question
  embedding = model.encode(question)

  # Return the embedding (it's a NumPy array, so we convert it into a list)
  return embedding.tolist()

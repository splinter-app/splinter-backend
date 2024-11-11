from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str
    pinecone_api_key: str
    embedding_provider: str = "huggingface"  # Default to 'huggingface' if not set
    embedding_model_name: str = "BAAI/bge-base-en-v1.5"  # Default model name
    pinecone_index_name: str

    class Config:
        env_file = ".env"  # Loads variables from the .env file

# Instantiate the settings, so they can be easily imported across your project
settings = Settings()

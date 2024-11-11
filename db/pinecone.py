from pinecone import Pinecone
from config import settings


def pinecone_similarity_search(embedding: list) -> list:
    top_k = 5

    # Initialize Pinecone and connect to the index
    pc = Pinecone(api_key=settings.pinecone_api_key)
    index = pc.Index(settings.pinecone_index_name)

    all_results = []

    # Find all namespace in index
    namespaces = list(index.describe_index_stats()['namespaces'].keys())

    # Perform similarity search on all namespaces
    for namespace in namespaces:
        query_response = index.query(
            vector=embedding,
            top_k=top_k,
            namespace=namespace,
            include_metadata=True
        )
        all_results.extend(query_response["matches"])
    
    # Sort results across all namespaces by score and return only top_k results
    all_results = sorted(all_results, key=lambda x: x["score"], reverse=True)[:top_k]

    return [result['metadata']['text'] for result in all_results]


import chromadb, ollama, os

client = chromadb.PersistentClient(path=os.getenv("CHROMA_PATH"))
collection = client.get_or_create_collection("company_data")

def embed(text: str) -> list:
    return ollama.embeddings(model="nomic-embed-text", prompt=text)["embedding"]

def add_chunk(chunk_id, text, metadata):
    collection.add(ids=[chunk_id], embeddings=[embed(text)], documents=[text], metadatas=[metadata])

def query(text, allowed_domains, top_k=5):
    results = collection.query(
        query_embeddings=[embed(text)],
        n_results=top_k,
        where={"domain": {"$in": allowed_domains}},  # RBAC filter at retrieval time
    )
    return results
import os
import chromadb
from chromadb.config import Settings

class ChromaClient:
    def __init__(self, id: str):
        self.id = id
        self.client = chromadb.Client(
            Settings(
                chroma_db_impl='duckdb+parquet',
                persist_directory=os.environ.get("CHROMADB_DIR")
            )
        )

    def persist(self):
        self.client.persist()
    
    def use_collection(self):
        self.collection = self.client.get_collection(self.id)

    def create_collection(self):
        self.collection = self.client.create_collection(self.id)
    
    def add(self, embeddings, metadatas, ids):
        self.collection.add(
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids,
        )
    
    def query(self, embeddings, n=1):
        return self.collection.query(
            query_embeddings=embeddings,
            n_results=n
        )
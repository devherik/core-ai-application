import chromadb
from chromadb import Collection
from chromadb.api import ClientAPI
from typing import Optional

class DatabaseModel:
    _instance: Optional["DatabaseModel"] = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, client: Optional[ClientAPI] = None):
        if client is None:
            self.client = chromadb.PersistentClient(path=".chroma_db")
        else:
            self.client = client

    def create_collection(self, name: str) -> Collection:
        return self.client.create_collection(name)

    def get_collection(self, name: str) -> Collection:
        return self.client.get_collection(name)

    def list_collections(self):
        return self.client.list_collections()

    def delete_collection(self, name: str):
        return self.client.delete_collection(name)
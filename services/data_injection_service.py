from sentence_transformers import SentenceTransformer
from models.database_model import DatabaseModel
import uuid

class DataInjectionService:
    """
    Service to handle data injection into the database.
    This service is responsible for:
    - Receiving the client
    - Loading the data
    - Converting it into text
    - Chunking it into smaller pieces
    - Defining metadata
    - Creating embeddings
    - Storing embeddings in the database
    - Returning the collection
    - Parsing into Agno document format
    - Returning the Agno document
    """

    def __init__(self, database: DatabaseModel) -> None:
        self.database = database
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def inject_data(self, data):
        # Implementation of data injection logic goes here.
        try:
            # Step 1: Chunk the data
            chunks = self.chunk_data(data)

            # Step 2: Create embeddings
            embeddings = self.create_embeddings(chunks)
            
            # Step 3: Define Matadata
            metadata = self.create_metadata(chunks)
            
            # Step 4: Store embeddings in the database
            try:
                collection = self.database.get_collection("initial_data")
            except Exception as e:
                print(f"Error occurred while retrieving collection: {e}")
                collection = self.database.create_collection("initial_data")
            for chunk, embedding, meta in zip(chunks, embeddings, metadata):
                unique_id = str(uuid.uuid4())
                collection.add(
                    ids=unique_id,
                    documents=[chunk],
                    embeddings=[embedding],
                    metadatas=[meta]
                )

            return collection
        except Exception as e:
            print(f"Error occurred while injecting data: {e}")
            return None

    def chunk_data(self, data, chunk_size=512, overlap=50):
        """
        Chunk the input data into smaller pieces.

        Args:
            data (str): The input text data to chunk.
            chunk_size (int): The maximum size of each chunk.
            overlap (int): The number of overlapping tokens between chunks.

        Returns:
            list: A list of text chunks.
        """
        # Tokenize the input data
        tokens = data.split()
        chunks = []
        for i in range(0, len(tokens), chunk_size - overlap):
            chunk = tokens[i:i + chunk_size]
            chunks.append(" ".join(chunk))
        return chunks
    
    def create_embeddings(self, chunks):
        """
        Create embeddings for the given text chunks.

        Args:
            chunks (list): A list of text chunks.

        Returns:
            list: A list of embeddings corresponding to the text chunks.
        """
        return self.model.encode(chunks, convert_to_tensor=True).tolist()
    
    def create_metadata(self, chunks):
        """
        Create metadata for the given text chunks.

        Args:
            chunks (list): A list of text chunks.

        Returns:
            list: A list of metadata dictionaries for each chunk.
        """
        return [{"text": chunk, "length": len(chunk)} for chunk in chunks]

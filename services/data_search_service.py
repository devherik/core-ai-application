from sentence_transformers import SentenceTransformer
from models.database_model import DatabaseModel

class DataSearchService:
    """
    Service to handle data search in the database.
    This service is responsible for:
    - Receiving search queries
    - Searching the database for relevant data
    - Returning the results
    """

    def __init__(self) -> None:
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def search_data(self, query: str, collection):
        """
        Search the database for relevant data based on the query.

        Args:
            query (str): The search query string.

        Returns:
            list: A list of documents that match the search criteria.
        """
        try:
            query_embedding = self.model.encode(query, convert_to_tensor=True)
            results = collection.query(
                query_embeddings=query_embedding.tolist(),
                n_results=5,  # Adjust the number of results as needed
            )
            return results
        except Exception as e:
            print(f"Error occurred while searching data: {e}")
            return []
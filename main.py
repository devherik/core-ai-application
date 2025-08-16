from core.settings import settings
from models.database_model import DatabaseModel
from services.data_injection_service import DataInjectionService
from services.data_search_service import DataSearchService

def main():
    print("Hello from core-ai-application!")

    # 1. Start the database and populate it with initial data
    try:
        db_service = DatabaseModel()
        data_injection_service = DataInjectionService(db_service)
        # Example data injection (this should be replaced with actual data)
        example_data = "Sample data to inject into the database."
        collection = data_injection_service.inject_data(example_data)
        data_search_service = DataSearchService()
        search_results = data_search_service.search_data("Sample search query", collection)
        print("Search results:", search_results)
    except Exception as e:
        print(f"Error occurred while initializing services: {e}")

    # 2. Start Celeron and Redis
    # 3. Get knowledge from the database
    # 4. Create a knowledge graph
    # 5. Create a Agno Agent
    # 6. Start agent-user interaction


if __name__ == "__main__":
    main()

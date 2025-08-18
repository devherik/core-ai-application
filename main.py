from core.settings import settings
from models.database_model import DatabaseModel
from services.data_injection_service import DataInjectionService
from services.data_loader_service import DataLoaderService
from agno.agent import Agent
from agno.models.google import Gemini
from agno.knowledge.document import DocumentKnowledgeBase

def main():
    print("Hello from core-ai-application!")

    # 1. Start the database and populate it with initial data
    try:
        db_service = DatabaseModel()
        data_injection_service = DataInjectionService(db_service)
        # Example data injection (this should be replaced with actual data)
        data_loader_service = DataLoaderService()
        example_data = data_loader_service.load_data_from("data/new/Clean Architecture A Craftsman's Guide to Software Structure and Design.pdf")
        collection = data_injection_service.inject_data(example_data)
        knowledge = DocumentKnowledgeBase(documents=collection, vector_db=db_service.vector_db)
        agent = Agent(model=Gemini(
            id=settings.GEMINI_API_KEY
        ), knowledge=knowledge)
        agent.print_response("Tell me about SOLID concepts.")
        # search_results = data_injection_service.search_data("What is a AI Product Engineer?", collection)
        # print("Search results:", search_results)
    except Exception as e:
        print(f"Error occurred while initializing services: {e}")

    # 2. Start Celeron and Redis
    # 3. Get knowledge from the database
    # 4. Create a knowledge graph
    # 5. Create a Agno Agent
    # 6. Start agent-user interaction


if __name__ == "__main__":
    main()

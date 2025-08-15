from core.settings import settings
from services.database_service import ChromaDBService

def main():
    print("Hello from core-ai-application!")

    # 1. Start the database and populate it with initial data
    db_service = ChromaDBService()
    
    # 2. Start Celeron and Redis
    # 3. Get knowledge from the database
    # 4. Create a knowledge graph
    # 5. Create a Agno Agent
    # 6. Start agent-user interaction


if __name__ == "__main__":
    main()

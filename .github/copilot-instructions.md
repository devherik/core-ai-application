# GitHub Copilot Instructions

This document guides AI agents in contributing to the multi-agent AI platform. The architecture is based on a distributed system of microservices, with a central FastAPI orchestrator, Celery workers for agent tasks, and ChromaDB for knowledge bases.

## 1. Core Architecture: FastAPI Orchestrator & Celery Workers

The system's core is a FastAPI application that orchestrates agent workflows. It handles API requests, dispatches tasks to a pool of Celery workers, and manages responses.

- **Orchestrator (FastAPI)**: The main entry point is in `app/main.py`. It should include routers from the `app/routers/` directory.
- **Agent Workers (Celery & Agno)**: Long-running and asynchronous tasks are handled by Celery workers. Each agent type should be a separate, containerized worker. These workers will use the "Agno" agent framework.
- **Task Queue (Redis)**: Redis serves as the message broker and result backend for Celery.

When adding new features, adhere to the prescribed modular structure:
- **API Endpoints**: `app/routers/` (e.g., `agents.py`, `knowledge.py`)
- **Business Logic**: `app/services/` (e.g., `agent_service.py`)
- **Data Models**: `app/schemas/` (Pydantic models for API validation)
- **Core Config**: `app/core/` (settings, security)

## 2. Knowledge Base: ChromaDB

The platform uses ChromaDB in client-server mode for managing multiple knowledge bases.

- **Data Isolation**: Use separate ChromaDB `collections` for each distinct knowledge base.
- **Fine-Grained Access**: Use document `metadata` within collections for filtering and access control.
- **Interaction**: The FastAPI orchestrator and the Agno agent workers will connect to the ChromaDB server as clients.

## 3. Development Workflow & Conventions

- **Dependencies**: Project dependencies are managed with `uv` and defined in `pyproject.toml`. Key libraries include `fastapi`, `celery`, `redis`, `google-genai`, and `sqlalchemy`.
- **Testing**: Use `pytest` for testing. Tests are located in the `tests/` directory (to be created). Run tests with:
  ```bash
  uv run pytest
  ```
- **Linting**: Use `ruff` for linting and formatting. Run the linter with:
  ```bash
  uv run ruff check .
  ```
- **Design Principles**: Development must follow **Clean Architecture** and **SOLID principles**. High-level business logic should be decoupled from low-level implementation details (e.g., specific database clients or LLM providers) through abstraction layers.

## 4. Communication & External Services

- **Response Sending**: Use the **Adapter Design Pattern** for sending responses to external channels like WhatsApp. Create new adapters in `app/services/notification_service.py` for new channels without changing the core logic.
- **Secrets Management**: All secrets (API keys, tokens, etc.) must be loaded from environment variables using `pydantic-settings`, not hardcoded.

By following these guidelines, you will help build a scalable, maintainable, and robust AI platform.

from textwrap import dedent
from core.settings import settings
from models.database_model import DatabaseModel
from services.data_injection_service import DataInjectionService

def main():
    print("Hello from core-ai-application!")

    # 1. Start the database and populate it with initial data
    try:
        db_service = DatabaseModel()
        data_injection_service = DataInjectionService(db_service)
        # Example data injection (this should be replaced with actual data)
        example_data = dedent("""
            As AI automates an increasing number of purely technical tasks, the skills that are uniquely human become the most valuable differentiators.
            These are not "soft skills" to be listed as an afterthought on a resume; they are core competencies that are essential for leadership,
            innovation, and responsible technology development in the age of AI.
            Creativity & Innovation: While AI can generate novel combinations of existing patterns, it lacks genuine understanding and
            the "inspirational spark" of human creativity.4 The most valuable contributions a developer can make will involve asking new questions,
            defining novel problems for AI to help solve, and synthesizing disparate ideas into a coherent product vision.
            AI is a powerful co-creator, but the human remains the creative director.37
            Critical Thinking & Skepticism: AI models, particularly LLMs, are prone to errors, biases, and "hallucinations"—generating
            confident-sounding but factually incorrect information.19 The AI-ready developer must act as a vigilant human filter,
            critically evaluating every AI-generated output for accuracy, relevance, and potential bias.
            An over-reliance on AI tools without this critical oversight can lead to a decrease in critical thinking skills and
            the propagation of flawed software.11
            Ethical AI & Responsible Development: Building AI systems carries significant ethical responsibilities.
            A developer must have a deep understanding of issues like algorithmic bias, data privacy, fairness, and transparency.11
            The ability to build "Explainable AI" (XAI)—systems that can provide insight into their decision-making processes—is becoming
            increasingly important, especially in regulated industries.27 This is no longer a niche concern but a fundamental aspect of professional
            practice required to build public trust and ensure compliance.5
            Communication & Collaboration: The complexity of AI systems requires tighter collaboration between diverse teams of software engineers,
            data scientists, product managers, and business stakeholders.9 The ability to clearly articulate complex technical concepts and
            their business implications to a non-technical audience is a superpower.26 As development becomes more about orchestrating systems and
            less about solitary coding, strong collaboration and communication skills become paramount for success.4
            The mastery of these four pillars creates a professional who is more than just an engineer or a product manager.
            It creates an AI Product Engineer. This emerging role blurs the traditional lines, combining deep technical and
            architectural expertise with a strong sense of product vision and business acumen.
            An AI Product Engineer can own the entire lifecycle of an AI-powered feature or product, from initial conception and architectural
            design through to implementation, deployment, monitoring, and ethical oversight.
            This ability to operate across the full spectrum of product development is the ultimate competitive advantage in the AI-driven future.
        """)
        collection = data_injection_service.inject_data(example_data)
        search_results = data_injection_service.search_data("What is a AI Product Engineer?", collection)
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

from app.llm.manager import LLMManager
from app.memory.database import initialize_database

def main():
    initialize_database()
    print("Inicializando base de datos...")

    print("=" * 50)
    print("        Bienvenido a Atenea")
    print("=" * 50)

    brain = LLMManager()

    while True:

        question = input("\nTú: ")

        if question.lower() in ["salir", "exit", "quit"]:
            print("\nAtenea: Hasta pronto")
            break

        answer = brain.ask(question)

        print(f"\nAtenea: {answer}")


if __name__ == "__main__":
    main()





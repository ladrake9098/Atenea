from .ollama_provider import OllamaProvider


class LLMManager:
    """Coordinates which provider is used"""

    def __init__(self):
        self.provider = OllamaProvider()

    def ask(self,prompt: str) -> str:
        return self.provider.ask(prompt)
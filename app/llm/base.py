"""
Base classes for Language Model providers.

Every provider (Ollama, OpenAi, etc.) must implement this interface.
"""

from abc import ABC, abstractmethod

class LLMProvider(ABC):
    """Abstract base class for  every language model provider. """

    @abstractmethod
    def ask(self,prompt: str) -> str:
        """
    Send a prompt to the model.

    Args:
        prompt: User message.

    Returns:
        Model response.
    """
    pass







import requests

from app.core.config import settings
from .base import LLMProvider


class OllamaProvider(LLMProvider):
    """Proveedor para modelos servidos por Ollama."""

    def ask(self,prompt: str) -> str:
        url = f"{settings.ollama_url}/api/generate"

        payload = {
            "model": settings.model_name,
            "prompt": prompt,
            "stream": False,
        }

        try:
            response = requests.post(url, json=payload, timeout=120)
            response.raise_for_status()

            data = response.json()

            return data.get("response", "No se recibió ninguna respuesta del modelo.")
        except requests.exceptions.RequestException as exc:
            return f"Error al conectar con Ollama: {exc}"

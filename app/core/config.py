from dataclasses import dataclass

@dataclass(frozen=True)
class Settings:
    ollama_url: str = "http://127.0.0.1:11434"
    model_name: str = "qwen2.5:1.5b"


settings = Settings()

from langchain_ollama import ChatOllama
from app.llm.base import LLMProvider


class OllamaProvider(LLMProvider):

    def __init__(self, model_name: str):
        super().__init__(model_name)

    def get_llm_instance(self):
        llm = ChatOllama(model=self.model_name)
        return llm

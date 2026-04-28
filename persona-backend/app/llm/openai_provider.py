from langchain_core.language_models import BaseChatModel
from langchain_openai import ChatOpenAI
from app.llm.base import LLMProvider


class OpenAIProvider(LLMProvider):

    def __init__(self, model_name: str):
        super().__init__(model_name)

    def get_llm_instance(self) -> BaseChatModel:
        """
        Return an OpenAI LLM instance
        """
        llm = ChatOpenAI(model=self.model_name)
        return llm

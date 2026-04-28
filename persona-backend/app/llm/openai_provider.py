from app.llm.base import LLMProvider
from langchain_openai import ChatOpenAI


class OpenAIProvider(LLMProvider):

    def __init__(self, model_name: str):
        super().__init__(model_name)

    def get_llm_instance(self):
        """
        Return an OpenAI LLM instance
        """
        llm = ChatOpenAI(model=self.model_name)
        return llm

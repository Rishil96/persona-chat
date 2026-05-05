from langchain_core.language_models import BaseChatModel
from langchain_anthropic import ChatAnthropic
from app.llm.base import LLMProvider


class AnthropicProvider(LLMProvider):

    def __init__(self, model_name: str):
        super().__init__(model_name)

    def get_llm_instance(self) -> BaseChatModel:
        """
        Returns an Anthropic LLM instance
        """
        llm = ChatAnthropic(model=self.model_name)
        return llm

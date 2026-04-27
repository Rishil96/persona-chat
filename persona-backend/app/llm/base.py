from abc import ABC, abstractmethod


class LLMProvider(ABC):

    def __init__(self, model_name: str):
        self.model_name = model_name

    @abstractmethod
    def get_llm_instance(self):
        pass

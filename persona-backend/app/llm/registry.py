from langchain_core.language_models import BaseChatModel
from app.llm.openai_provider import OpenAIProvider
from app.llm.anthropic_provider import AnthropicProvider
from app.llm.ollama_provider import OllamaProvider
from app.logger import get_logger

# Initialize logger
logger = get_logger()

# Supported models in Chatbot application
SUPPORTED_OPENAI_MODELS = ["gpt-4o", "gpt-4o-mini"]
SUPPORTED_ANTHROPIC_MODELS = ["claude-opus-4-7-20250514", "claude-sonnet-4-6-20250514", "claude-haiku-4-5-20251001"]
SUPPORTED_OLLAMA_MODELS = ["llama3.1:8b", "mistral", "qwen2.5:7b", "deepseek-r1:7b"]


def get_llm_instance(model_name: str) -> BaseChatModel:
    """
    Returns the LLM instance selected by the user
    """
    if model_name in SUPPORTED_OPENAI_MODELS:
        llm_obj = OpenAIProvider(model_name=model_name)
    elif model_name in SUPPORTED_ANTHROPIC_MODELS:
        llm_obj = AnthropicProvider(model_name=model_name)
    elif model_name in SUPPORTED_OLLAMA_MODELS:
        llm_obj = OllamaProvider(model_name=model_name)
    else:
        logger.error(f"Model {model_name} not supported or doesn't exist")
        raise ValueError(f"{model_name} is not either not supported or not a valid model")
    logger.info(f"Using model: {model_name}")
    return llm_obj.get_llm_instance()

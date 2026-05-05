import logging
import os
from app.constants import LOGGER_NAME, DEFAULT_LOGGER


def get_logger():
    """
    Function to create and return a singleton logger
    """
    logger = logging.getLogger(os.getenv(LOGGER_NAME, DEFAULT_LOGGER))
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger

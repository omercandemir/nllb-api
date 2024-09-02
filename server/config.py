from pydantic_settings import BaseSettings
from typing import TypeVar, Type

T = TypeVar('T')

def singleton(cls: Type[T]) -> T:
    """
    Summary
    -------
    a decorator to make a class a singleton

    Parameters
    ----------
    cls (Type[T]) : the class to make a singleton

    Returns
    -------
    instance (T) : the singleton instance
    """
    return cls()


@singleton
class Config(BaseSettings):
    """
    Summary
    -------
    the general config class

    Attributes
    ----------
    server_port (int) : the port to run the server on
    server_root_path (str) : the root path for the server
    worker_count (int) : the number of workers to use
    use_cuda (bool) : whether to use CUDA for inference
    translator_model_name (str) : the name of the translator model
    language_detector_model_name (str) : the name of the language detector model
    """

    server_port: int = 8000
    server_root_path: str = '/api'
    worker_count: int = 1
    translator_pool_count: int = 2
    use_cuda: bool = False
    translator_model_name: str = 'winstxnhdw/nllb-200-distilled-1.3B-ct2-int8'
    language_detector_model_name: str = 'facebook/fasttext-language-identification'
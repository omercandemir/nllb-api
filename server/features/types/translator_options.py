from typing import TypedDict

from server.types import Devices


class TranslatorOptions(TypedDict):
    """
    Summary
    -------
    the parameters to initialise the LLM

    Attributes
    ----------
    model_path (str) : the path to the model
    device (Devices) : the device to use
    compute_type (ComputeTypes) : the compute type or string
    inter_threads (int) : the number of inter-threads
    """

    model_path: str
    device: Devices
    compute_type: str
    inter_threads: int

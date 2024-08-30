from typing import Annotated

from msgspec import Meta, Struct



class Language(Struct):
    """
    Summary
    -------
    the NLLB language schema

    Attributes
    ----------
    language (Languages) : the detected language
    """

    language: Annotated[str, Meta(examples=['eng_Latn'])]

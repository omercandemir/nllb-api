from typing import Annotated

from litestar import Controller, get, post
from litestar.openapi.spec.example import Example
from litestar.params import Parameter
from litestar.status_codes import HTTP_200_OK

from server.features import TranslatorPool, LanguageDetector
from server.schemas.v1 import Translated, Translation


class TranslateController(Controller):
    """
    Summary
    -------
    the `/translate` route translates an input from a source language to a target
    """

    path = '/translate'

    @get(cache=True)
    async def translate_get(
        self,
        text: Annotated[str, Parameter(examples=[Example(value='Hello, world!')])],
        source: Annotated[str, Parameter(examples=[Example(value='eng_Latn')])],
        target: Annotated[str, Parameter(examples=[Example(value='spa_Latn')])],
    ) -> Translated:
        """
        Summary
        -------
        the GET variant of the `/translate` route
        """
        return Translated(result=await TranslatorPool.translate(text, source, target))

    @post(status_code=HTTP_200_OK)
    async def translate_post(self, data) -> Translated:
        """
        Summary
        -------
        the POST variant of the `/translate` route
        """
        if data.source == "autodetect":
            data.source = LanguageDetector.detect(data.text)
        print(data.source)
        return Translated(result=await TranslatorPool.translate(data.text, data.source, data.target))

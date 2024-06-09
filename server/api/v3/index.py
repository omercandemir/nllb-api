from typing import Literal

from starlette.responses import PlainTextResponse

from server.api.v3 import v3


@v3.get('/', response_model=Literal['Welcome to v3 of the API!'])
def index() -> PlainTextResponse:
    """
    Summary
    -------
    the `/` route
    """
    return PlainTextResponse('Welcome to v3 of the API!')

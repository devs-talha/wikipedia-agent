from langgraph_sdk import Auth

from config import settings

auth = Auth()


@auth.authenticate
async def authorize_api_key(authorization: str | None) -> None:
    assert authorization

    if authorization != settings.api_key:
        raise Auth.exceptions.HTTPException(status_code=401, detail="Invalid api key")

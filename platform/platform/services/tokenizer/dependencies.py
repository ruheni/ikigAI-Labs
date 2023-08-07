from fastapi import Request

from ltl_platform.services.tokenizer.token_service import TokenService


def get_token_service(request: Request) -> TokenService:
    return TokenService(request.app.state.token_encoding)

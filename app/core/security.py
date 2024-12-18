from fastapi import HTTPException, Header
from typing import Optional
from app.core.logger import get_security_logger

logger = get_security_logger()


class SecurityService:
    def __init__(self, allowed_tokens: list):
        self.allowed_tokens = allowed_tokens

    async def verify_authorization(
        self, authorization: Optional[str] = Header(None)
    ) -> str:
        if not authorization:
            logger.error("Missing Authorization header")
            raise HTTPException(status_code=401, detail="Missing Authorization header")

        if not authorization.startswith("Bearer "):
            logger.error("Invalid Authorization header format")
            raise HTTPException(
                status_code=401, detail="Invalid Authorization header format"
            )

        token = authorization.replace("Bearer ", "")
        if token not in self.allowed_tokens:
            logger.error("Invalid token")
            raise HTTPException(status_code=401, detail="Invalid token")

        return token

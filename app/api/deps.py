from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_session
from app.core.security import decode_access_token

bearer = HTTPBearer(auto_error=False)

async def db_session(session: AsyncSession = Depends(get_session)) -> AsyncSession:
    return session

def get_current_user_id(creds: HTTPAuthorizationCredentials | None = Depends(bearer)) -> int:
    if creds is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    payload = decode_access_token(creds.credentials)
    sub = payload.get("sub")
    if not sub:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return int(sub)

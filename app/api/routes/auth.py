from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.deps import db_session
from app.schemas.user import LoginRequest, Token
from app.services.users import UsersService

router = APIRouter()

@router.post("/login", response_model=Token)
async def login(payload: LoginRequest, session: AsyncSession = Depends(db_session)):
    token = await UsersService(session).login(payload.email, payload.password)
    return Token(access_token=token)

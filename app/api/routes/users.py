from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.deps import db_session, get_current_user_id
from app.schemas.user import UserCreate, UserPublic
from app.services.users import UsersService

router = APIRouter()

@router.post("", response_model=UserPublic, status_code=201)
async def register(payload: UserCreate, session: AsyncSession = Depends(db_session)):
    user = await UsersService(session).register(payload.email, payload.password)
    return UserPublic(id=user.id, email=user.email)

@router.get("/me", response_model=UserPublic)
async def me(user_id: int = Depends(get_current_user_id)):
    return UserPublic(id=user_id, email="hidden@demo.local")

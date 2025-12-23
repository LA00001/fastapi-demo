from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.security import hash_password, verify_password, create_access_token
from app.repositories.users import UsersRepository

class UsersService:
    def __init__(self, session: AsyncSession):
        self.repo = UsersRepository(session)

    async def register(self, email: str, password: str):
        if await self.repo.get_by_email(email):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered")
        return await self.repo.create(email=email, password_hash=hash_password(password))

    async def login(self, email: str, password: str) -> str:
        user = await self.repo.get_by_email(email)
        if not user or not verify_password(password, user.password_hash):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        return create_access_token(subject=str(user.id))

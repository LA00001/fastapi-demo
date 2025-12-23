# FastAPI demo (external API + Redis cache + JWT + async Postgres)

Демо-проект для pet-репозитория:
- FastAPI + async/await
- JWT (python-jose) + bcrypt (passlib)
- Redis кеш (async redis-py)
- async PostgreSQL (SQLAlchemy 2.x + asyncpg)
- Alembic (async env.py)
- httpx AsyncClient (пул соединений)
- APScheduler (пример фоновой задачи)

## Запуск через Docker
```bash
cp .env.example .env
docker compose up --build
```
Swagger: http://localhost:8000/docs

## Полезные эндпоинты
- `GET  /api/v1/health`
- `POST /api/v1/users` (register)
- `POST /api/v1/auth/login` (JWT)
- `GET  /api/v1/market/quote/{ticker}` (external API + Redis TTL)

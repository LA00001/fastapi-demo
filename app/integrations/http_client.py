import httpx

class HttpPool:
    def __init__(self) -> None:
        self.client = httpx.AsyncClient(
            timeout=httpx.Timeout(10.0),
            limits=httpx.Limits(max_connections=50, max_keepalive_connections=20),
            headers={"User-Agent": "fastapi-demo/0.1"},
        )

    async def close(self) -> None:
        await self.client.aclose()

http_pool = HttpPool()

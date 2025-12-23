from app.core.config import settings
from app.integrations.http_client import http_pool

class FMPClient:
    base_url = "https://financialmodelingprep.com/api/v3"

    async def quote(self, ticker: str) -> dict:
        if not settings.FMP_API_KEY:
            return {"symbol": ticker.upper(), "price": None, "note": "Set FMP_API_KEY to call real API"}
        url = f"{self.base_url}/quote/{ticker.upper()}"
        r = await http_pool.client.get(url, params={"apikey": settings.FMP_API_KEY})
        r.raise_for_status()
        data = r.json()
        return data[0] if isinstance(data, list) and data else {"symbol": ticker.upper(), "price": None}

fmp_client = FMPClient()

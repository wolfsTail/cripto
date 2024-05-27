from service.clients.http_client import CMCClient
from service.config import settings


async def get_async_client():
    return CMCClient(
        url=settings.CRIPTO_API_DOMAIN,
        api_key=settings.CRIPTO_API_KEY
    )

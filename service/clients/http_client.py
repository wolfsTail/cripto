from service.clients.http_base_client import HTTPClientBase


class CMCClient(HTTPClientBase):
    async def get_crypto_list(self):
        async with self._session.get(
            url="/v1/cryptocurrency/listings/latest"
        ) as response:
            result = await response.json()
            return result["data"]
    
    async def get_crypto_instance(self, currency_id: int):
        async with self._session.get(
            url="/v2/cryptocurrency/quotes/latest",
            params={"id": currency_id},
        ) as response:
            result = await response.json()
            return result["data"][str(currency_id)]            

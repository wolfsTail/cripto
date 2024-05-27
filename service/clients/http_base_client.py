from aiohttp import ClientSession


class HTTPClientBase:
    def __init__(self, url: str, api_key: str):
        self._session = ClientSession(
            base_url=url,
            headers={
                'Accepts': 'application/json',
                'X-CMC_PRO_API_KEY': api_key,
                },
        )
    
    async def get_crypto_list(self):
        pass
    
    async def get_crypto_instance(self, currency_id: int):
        pass

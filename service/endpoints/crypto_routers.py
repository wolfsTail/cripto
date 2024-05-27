from fastapi import APIRouter, Depends

from service.clients import HTTPClientBase, get_async_client


router = APIRouter(
    prefix="/currencies"
)


@router.get("/list/")
async def get_crypto_currencies_list(
    async_client: HTTPClientBase = Depends(get_async_client)
):
    return await async_client.get_crypto_list()

@router.get("/{currency_id}")
async def get_crypto_currency(
    currency_id: int, async_client: HTTPClientBase = Depends(get_async_client)
    ):
    return await async_client.get_crypto_instance(currency_id=currency_id)

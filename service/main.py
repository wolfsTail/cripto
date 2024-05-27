from fastapi import FastAPI

from service.endpoints import crypto_routers


app = FastAPI(
    title="Crypto Proxy!"
)

app.include_router(crypto_routers)

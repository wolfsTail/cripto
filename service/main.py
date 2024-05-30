from fastapi import FastAPI

from service.endpoints import crypto_routers
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="Crypto Proxy!"
)

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(crypto_routers)

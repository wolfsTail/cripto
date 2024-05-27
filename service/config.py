from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    CRIPTO_API_KEY: str
    CRIPTO_API_DOMAIN: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()

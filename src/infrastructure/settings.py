from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    FRONTEND_BASE_URL: str
    DATABASE_URL: str
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_EXPIRE_DAYS: int
    
    class Config:
        env_file = ".env"


settings = Settings()
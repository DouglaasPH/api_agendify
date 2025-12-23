from fastapi_mail import ConnectionConfig

from pydantic_settings import BaseSettings
from pydantic import EmailStr

from jinja2 import Environment, FileSystemLoader

import os

class MailSettings(BaseSettings):
    MAIL_USERNAME: EmailStr
    MAIL_PASSWORD: str
    MAIL_FROM: EmailStr
    MAIL_PORT: int = 587
    MAIL_SERVER: str = "smtp.gmail.com"
    MAIL_STARTTLS: bool = True
    MAIL_SSL_TLS: bool = False
    USE_CREDENTIALS: bool = True
    TEMPLATE_FOLDER: str = "templates"
    
    class Config:
        env_file = os.path.join(os.path.dirname(__file__), "../../.env")
        env_file_encoding = "utf-8"
        extra = "ignore"
        

templates_path = os.path.join(os.path.dirname(__file__), "templates")
templates_env = Environment(loader=FileSystemLoader(templates_path))

settings = MailSettings()

conf = ConnectionConfig(
    MAIL_USERNAME=settings.MAIL_USERNAME,
    MAIL_PASSWORD=settings.MAIL_PASSWORD,
    MAIL_FROM=settings.MAIL_FROM,
    MAIL_PORT=settings.MAIL_PORT,
    MAIL_SERVER=settings.MAIL_SERVER,
    MAIL_STARTTLS=settings.MAIL_STARTTLS,
    MAIL_SSL_TLS=settings.MAIL_SSL_TLS,
    USE_CREDENTIALS=settings.USE_CREDENTIALS,
    TEMPLATE_FOLDER=settings.TEMPLATE_FOLDER,
)
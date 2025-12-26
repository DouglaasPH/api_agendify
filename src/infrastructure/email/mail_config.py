from pathlib import Path

from fastapi_mail import ConnectionConfig
from jinja2 import Environment, FileSystemLoader

from infrastructure.settings import settings

# Base path do projeto (src/)
BASE_DIR = Path(__file__).resolve().parents[2]

# Pasta real dos templates
TEMPLATE_FOLDER = BASE_DIR / "infrastructure" / "email" / "templates"

# Jinja2 environment (usado manualmente se quiser)
templates_env = Environment(loader=FileSystemLoader(TEMPLATE_FOLDER))


conf = ConnectionConfig(
    MAIL_USERNAME=settings.MAIL_USERNAME,
    MAIL_PASSWORD=settings.MAIL_PASSWORD,
    MAIL_FROM=settings.MAIL_FROM,
    MAIL_PORT=settings.MAIL_PORT,
    MAIL_SERVER=settings.MAIL_SERVER,
    MAIL_STARTTLS=settings.MAIL_STARTTLS,
    MAIL_SSL_TLS=settings.MAIL_SSL_TLS,
    USE_CREDENTIALS=settings.USE_CREDENTIALS,
    TEMPLATE_FOLDER=TEMPLATE_FOLDER,
)

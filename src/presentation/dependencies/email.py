from domain.services.email_service import EmailService
from infrastructure.email.fastapi_mail_service import FastAPIMailService


def get_email_service() -> EmailService:
    return FastAPIMailService()

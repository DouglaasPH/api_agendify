from fastapi_mail import FastMail, MessageSchema

from domain.services.email_service import EmailService
from infrastructure.email.mail_config import conf, templates_env


class FastAPIMailService(EmailService):
    def __init__(self):
        self._mailer = FastMail(conf)

    async def _send_html_email(
        self,
        subject: str,
        recipients: list[str],
        template_name: str,
        context: dict,
    ) -> None:
        html_content = templates_env.get_template(template_name).render(**context)

        message = MessageSchema(
            subject=subject,
            recipients=recipients,
            body=html_content,
            subtype="html",
        )

        await self._mailer.send_message(message)

    async def send_welcome_email(self, username: str, email: str) -> None:
        await self._send_html_email(
            subject="Welcome to Agendify!",
            recipients=[email],
            template_name="welcome_email.html",
            context={"username": username},
        )

    async def send_verification_email(self, verification_link: str, email: str) -> None:
        await self._send_html_email(
            subject="Agendify - Verify your email",
            recipients=[email],
            template_name="verification_email.html",
            context={"verification_link": verification_link},
        )

    async def send_login_email(self, username: str, email: str) -> None:
        await self._send_html_email(
            subject="Agendify - Login detected",
            recipients=[email],
            template_name="login_email.html",
            context={"username": username},
        )

    async def send_password_reset_email(
        self,
        username: str,
        email: str,
        reset_link: str,
    ) -> None:
        await self._send_html_email(
            subject="Agendify – Password reset request",
            recipients=[email],
            template_name="password_reset_email.html",
            context={
                "user_name": username,
                "reset_link": reset_link,
            },
        )

    async def send_email_change_confirmation(
        self,
        username: str,
        old_email: str,
        new_email: str,
        confirm_link: str,
    ) -> None:
        await self._send_html_email(
            subject="Agendify – Confirm your new email address",
            recipients=[new_email],
            template_name="email_change_confirmation.html",
            context={
                "user_name": username,
                "old_email": old_email,
                "new_email": new_email,
                "confirm_link": confirm_link,
            },
        )

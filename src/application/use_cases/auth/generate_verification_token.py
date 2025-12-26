from domain.services.email_service import EmailService
from infrastructure.security.password_hasher import PasswordHasher
from infrastructure.security.token_service import TokenService


class GenerateVerificationToken:
    def __init__(
        self,
        password_hasher: PasswordHasher,
        token_service: TokenService,
        email_service: EmailService,
    ):
        self.password_hasher = password_hasher
        self.token_service = token_service
        self.email_service = email_service

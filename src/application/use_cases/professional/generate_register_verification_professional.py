import uuid
from datetime import timedelta

from domain.repositories.professional_repository import ProfessionalRepository
from domain.services.email_service import EmailService
from infrastructure.security.password_hasher import PasswordHasher
from infrastructure.security.token_service import TokenService


class GenerateRegisterVerificationProfessional:
    def __init__(
        self,
        professional_repository: ProfessionalRepository,
        password_hasher: PasswordHasher,
        token_service: TokenService,
        email_service: EmailService,
        frontend_base_url: str,
    ):
        self.professional_repository = professional_repository
        self.password_hasher = password_hasher
        self.token_service = token_service
        self.email_service = email_service
        self.frontend_base_url = frontend_base_url
    
    async def execute(self, data):
        if self.professional_repository.get_by_email(data.email):
            raise ValueError("email already registered")
        
        hashed_password = self.password_hasher.hash(data.password)
        chat_code = str(uuid.uuid4())
        
        token = self.token_service.create_token_for_register_professional(
            subject={
                "sub": data.email,
                "role": "professional",
                "iss": "api_agendify",
                "aud": "api_agendify",
                "name": data.name,
                "email": data.email,
                "profession": data.profession,
                "hashed_password": hashed_password,
                "profile_avatar_id": data.profileAvatarId,
                "phone_number": data.phoneNumber,
                "chat_code": chat_code,
            },
            expires_delta=timedelta(minutes=5)
        )
        
        verification_link = f"{self.frontend_base_url}/validate-email-in-register/{token}"
        
        await self.email_service.send_verification_email(
            verification_link,
            email=data.email
        )

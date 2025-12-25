from domain.repositories.professional_repository import ProfessionalRepository
from infrastructure.security.token_service import TokenService
from domain.services.email_service import EmailService

class RequestPasswordResetForProfessional:
    def __init__(self, professional_repository: ProfessionalRepository, token_service: TokenService, email_service: EmailService):
        self.professional_repository = professional_repository
        self.token_service = token_service
        self.email_service = email_service
    
    async def execute(self, email: str):
        professional = self.professional_repository.get_by_email(email)
        
        if not professional:
            return
        
        payload = {
            "professional_id": professional.id,
            "email": professional.email
        }
        
        token = self.token_service.create_temporary_token(
            payload=payload,
            expires_minutes=15
        )
        
        link = f"http://localhost:5173/forgot-your-password/reset-password/{token}"
        
        await self.email_service.send_password_reset_email(
            username=professional.name,
            email=professional.email,
            reset_link=link,
        )

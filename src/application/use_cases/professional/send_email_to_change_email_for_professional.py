from domain.repositories.professional_repository import ProfessionalRepository
from infrastructure.security.token_service import TokenService
from domain.services.email_service import EmailService

class SendEmailToChangeEmailForProfessional:
    def __init__(
        self,
        professional_repository: ProfessionalRepository,
        token_service: TokenService,
        email_service: EmailService,
        frontend_base_url: str
    ):
        self.professional_repository = professional_repository
        self.token_service = token_service
        self.email_service = email_service
        self.frontend_base_url = frontend_base_url

    async def execute(self, professional_id: int, new_email: str):
        professional = self.professional_repository.get_by_id(professional_id)
        
        if not professional:
            raise ValueError("Professional not found")
        
        email_in_use = self.professional_repository.get_by_email(new_email)
        
        if email_in_use:
            raise ValueError("The email is already linked to an account")
        
        payload = {
            "current_email": professional.email,
            "new_email": new_email
        }
        
        token = self.token_service.create_temporary_token(payload=payload, expires_minutes=15)
        
        link = f"{self.frontend_base_url}/change-email/{token}"
        
        await self.email_service.send_email_change_confirmation(
            username=professional.name,
            old_email=professional.email,
            new_email=new_email,
            link=link,
        )

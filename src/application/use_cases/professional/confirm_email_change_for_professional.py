from domain.repositories.professional_repository import ProfessionalRepository
from domain.repositories.refresh_token_repository import RefreshTokenRepository
from infrastructure.security.token_service import TokenService

class ConfirmEmailChange:
    def __init__(self, professional_repository: ProfessionalRepository, refresh_token_repository: RefreshTokenRepository, token_service: TokenService):
        self.professional_repository = professional_repository
        self.refresh_token_repository = refresh_token_repository
        self.token_service = token_service

    def execute(self, token: str):
        payload = self.token_service.decode_token(token)
        
        current_email = payload.get("current_email")
        new_email = payload.get("new_email")
        
        if not current_email or not new_email:
            raise ValueError("Invalid token payload")
        
        professional = self.professional_repository.get_by_email(current_email)
        
        if not professional:
            raise ValueError("Professional not found")
        
        email_in_use = self.professional_repository.get_by_email(new_email)
        
        if email_in_use:
            raise ValueError("Email already in use")
        
        professional.email = new_email
        self.professional_repository.save(professional)
        
        self.refresh_token_repository.revoke_all_by_professional(professional.id)

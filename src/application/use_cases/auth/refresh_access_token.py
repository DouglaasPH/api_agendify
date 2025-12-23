from datetime import datetime, timezone

from domain.repositories.refresh_token_repository import RefreshTokenRepository
from domain.repositories.professional_repository import ProfessionalRepository
from infrastructure.security.token_service import TokenService


class RefreshAccessToken:
    def __init__(
        self,
        refresh_token_repository: RefreshTokenRepository,
        professional_repository: ProfessionalRepository,
        token_service: TokenService,
    ):
        self.refresh_token_repository = refresh_token_repository
        self.professional_repository = professional_repository
        self.token_service = token_service
    
    def execute(self, refresh_token_value: str):
        refresh_token = self.refresh_token_repository.get_by_token(refresh_token_value)
        
        if not refresh_token:
            raise ValueError("Invalid refresh token")
        
        if refresh_token.is_revoked:
            raise ValueError("Refresh token revoked")
        
        if refresh_token.expires_at < datetime.now(timezone.utc):
            raise ValueError("Refresh token expired")
        
        professional = self.professional_repository.get_by_id(refresh_token.professional_id)
        
        if not professional or professional.status != "active":
            raise ValueError("Professional not active")
        
        return self.token_service.create_access_token(
            subject=professional.id,
            role="professional"
        )

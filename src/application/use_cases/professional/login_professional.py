import uuid
from datetime import datetime, timedelta, timezone

from domain.entities.refresh_token import RefreshToken
from domain.repositories.professional_repository import ProfessionalRepository
from domain.repositories.refresh_token_repository import RefreshTokenRepository

from infrastructure.security.token_service import TokenService
from infrastructure.security.password_hasher import PasswordHasher
from infrastructure.settings import settings


class LoginProfessional:
    def __init__(
        self, 
        professional_repository: ProfessionalRepository, 
        refresh_token_repository: RefreshTokenRepository,
        token_service: TokenService, 
        password_hasher: PasswordHasher,
        
    ):
        self.professional_repository = professional_repository
        self.refresh_token_repository = refresh_token_repository
        self.token_service = token_service
        self.password_hasher = password_hasher
        self.refresh_expire_days = settings.REFRESH_EXPIRE_DAYS
    
    def execute(self, email: str, password: str):
        professional = self.professional_repository.get_by_email(email)
        
        if not professional:
            raise ValueError("Invalid email")
        
        is_password = self.password_hasher.verify(password, professional.hashed_password)
        
        if not is_password:
            raise ValueError("invalid password")
        
        access_token = self.token_service.create_access_token(str(professional.id), "professional")

        refresh_token_value = str(uuid.uuid4())
        expires_at = datetime.now(timezone.utc) + timedelta(days=self.refresh_expire_days)
                
        refresh_token = RefreshToken(
            id=None,
            professional_id=professional.id,
            token=refresh_token_value,
            expires_at=expires_at
        )
        
        self.refresh_token_repository.save(refresh_token)

        return {
            **access_token,
            "refresh_token": refresh_token.token
        }

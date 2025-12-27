from domain.repositories.professional_repository import ProfessionalRepository
from domain.repositories.refresh_token_repository import RefreshTokenRepository
from infrastructure.security.password_hasher import PasswordHasher
from infrastructure.security.token_service import TokenService


class ResetPassword:
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

    def without_login(self, token: str, new_password: str):
        payload = self.token_service.decode_token(token)

        professional_id = payload.get("professional_id")

        if not professional_id:
            raise ValueError("Invalid token")

        professional = self.professional_repository.get_by_id(professional_id)

        if not professional:
            raise ValueError("Professional not found")

        hashed_password = self.password_hasher.hash(new_password)

        professional.change_password(hashed_password)
        self.professional_repository.save(professional)

        self.refresh_token_repository.revoke_all_by_professional(professional_id)

    def with_login(self, old_password: str, new_password: str, professional_id: int):
        professional = self.professional_repository.get_by_id(professional_id)

        if not professional:
            raise ValueError("Professional not found")

        if not self.password_hasher.verify(old_password, professional.hashed_password):
            raise ValueError("The current password is not the same")

        hashed_password = self.password_hasher.hash(new_password)

        professional.change_password(hashed_password)
        self.professional_repository.save(professional)

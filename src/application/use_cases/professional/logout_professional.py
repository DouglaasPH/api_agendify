from domain.repositories.refresh_token_repository import RefreshTokenRepository
from domain.repositories.professional_repository import ProfessionalRepository


class LogoutProfessional:
    def __init__(
        self,
        refresh_token_repository: RefreshTokenRepository,
        professional_repository: ProfessionalRepository,
    ):
        self.refresh_token_repository = refresh_token_repository
        self.professional_repository = professional_repository

    def execute(self, professional_id: int, refresh_token_value: str) -> None:
        professional = self.professional_repository.get_by_id(professional_id)

        if not professional:
            raise ValueError("Professional not found")

        refresh_token = self.refresh_token_repository.get_by_token(refresh_token_value)

        if not refresh_token:
            raise ValueError("Refresh token not found")

        if refresh_token.professional_id != professional_id:
            raise PermissionError("Token does not belong to this professional")

        refresh_token.revoke()
        self.refresh_token_repository.save(refresh_token)

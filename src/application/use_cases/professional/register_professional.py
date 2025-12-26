from domain.entities.professional import Professional, ProfessionalStatus
from domain.repositories.professional_repository import ProfessionalRepository
from infrastructure.security.token_service import TokenService


class RegisterProfessional:
    def __init__(
        self,
        professional_repository: ProfessionalRepository,
        token_service: TokenService,
    ):
        self.professional_repository = professional_repository
        self.token_service = token_service

    def execute(self, token):
        payload = self.token_service.decode_token(token)

        email = payload.get("email")

        if not email:
            raise ValueError("Invalid token")

        professional = Professional(
            id=None,
            name=payload["name"],
            email=payload["email"],
            profession=payload["profession"],
            hashed_password=payload["hashed_password"],
            profile_avatar_id=payload["profile_avatar_id"],
            phone_number=payload["phone_number"],
            chat_code=payload["chat_code"],
            status=ProfessionalStatus.active,
        )

        self.professional_repository.save(professional)

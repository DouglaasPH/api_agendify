from domain.repositories.professional_repository import ProfessionalRepository


class CheckProfessionalEmail:
    def __init__(self, professional_repository: ProfessionalRepository):
        self.professional_repository = professional_repository

    def execute(self, email: str) -> bool:
        return self.professional_repository.get_by_email(email)

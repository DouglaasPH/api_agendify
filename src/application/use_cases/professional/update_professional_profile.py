from domain.repositories.professional_repository import ProfessionalRepository

class UpdateProfessionalProfile:
    def __init__(self, professional_repository: ProfessionalRepository):
        self.professional_repository = professional_repository

    def execute(
        self,
        professional_id: int,
        name: str | None = None,
        profession: str | None = None,
        profile_avatar_id: int | None = None,
        phone_number: str | None = None,
    ):
        professional = self.professional_repository.get_by_id(professional_id)

        if not professional:
            raise ValueError("Professional not found")

        professional.update_profile(
            name=name,
            profession=profession,
            phone_number=phone_number,
        )

        if profile_avatar_id is not None:
            professional.update_profile_avatar_id(profile_avatar_id)

        self.professional_repository.save(professional)

        return professional

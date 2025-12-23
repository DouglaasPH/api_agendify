from application.dto.professional_dto import ProfessionalOutputDTO
from domain.repositories.professional_repository import ProfessionalRepository

class GetProfessional:
    def __init__(self, professional_repository: ProfessionalRepository):
        self.professional_repository = professional_repository
    
    def get_by_id(self, professional_id: int):
        professional = self.professional_repository.get_by_id(professional_id)
        
        if not professional:
            raise ValueError("Professional not found")
        
        return ProfessionalOutputDTO(
            id=professional.id,
            name=professional.name,
            email=professional.email,
            phone_number=professional.phone_number,
            profession=professional.profession,
            profile_avatar_id=professional.profile_avatar_id,
            chat_code=professional.chat_code,
        )

    def get_by_chat_code(self, chat_code: str):
        professional = self.professional_repository.get_by_chat_code(chat_code)
        
        if not professional:
            raise ValueError("Professional not found")
        
        return ProfessionalOutputDTO(
            id=professional.id,
            name=professional.name,
            email=professional.email,
            phone_number=professional.phone_number,
            profession=professional.profession,
            profile_avatar_id=professional.profile_avatar_id,
            chat_code=professional.chat_code,
        )

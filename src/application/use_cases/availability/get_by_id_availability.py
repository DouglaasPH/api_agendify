from domain.entities.availability import Availability
from domain.repositories.availability_repository import AvailabilityRepository
from domain.repositories.professional_repository import ProfessionalRepository


class GetByIdAvailability:
    def __init__(self, availability_repository: AvailabilityRepository, professional_repository: ProfessionalRepository):
        self.availability_repository = availability_repository
        self.professional_repository = professional_repository
    
    def execute(
        self,
        professional_id: int,
        availability_id: int,
    ) -> Availability:
        professional = self.professional_repository.get_by_id(professional_id)
        
        if not professional:
            raise ValueError("Professional not found")
        
        availability = self.availability_repository.get_by_id(
            professional_id=professional_id,
            availability_id=availability_id,
        )
        
        if not availability:
            raise ValueError("Availability not found")
        
        if availability.professional_id != professional_id:
            raise PermissionError("You do not have access to this availability")
        
        return availability
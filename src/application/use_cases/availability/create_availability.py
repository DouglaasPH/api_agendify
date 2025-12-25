from datetime import date, datetime

from domain.entities.availability import Availability, AvailabilityStatus
from domain.entities.professional import ProfessionalStatus
from domain.repositories.availability_repository import AvailabilityRepository
from domain.repositories.professional_repository import ProfessionalRepository


class CreateAvailability:
    def __init__(self, availability_repository: AvailabilityRepository, professional_repository: ProfessionalRepository):
        self.availability_repository = availability_repository
        self.professional_repository = professional_repository
    
    def execute(self, professional_id: int, date: date, start_time: datetime, end_time: datetime, slot_duration_minutes: int) -> None:
        professional = self.professional_repository.get_by_id(professional_id)
        
        if not professional:
            raise ValueError("Professional not found")
        
        if professional.status != ProfessionalStatus.active:
            raise ValueError("Professional is not active")
        
        availability = Availability(
            id=None,
            professional_id=professional_id,
            date=date,
            start_time=start_time,
            end_time=end_time,
            slot_duration_minutes=slot_duration_minutes,
            status= AvailabilityStatus.available,
        )
        
        self.availability_repository.save(availability)

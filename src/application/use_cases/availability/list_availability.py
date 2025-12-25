from datetime import date, datetime
from typing import List, Optional

from domain.entities.availability import Availability
from domain.repositories.availability_repository import AvailabilityRepository
from domain.repositories.professional_repository import ProfessionalRepository


class ListAvailability:
    def __init__(self, availability_repository: AvailabilityRepository, professional_repository: ProfessionalRepository):
        self.availability_repository = availability_repository
        self.professional_repository = professional_repository
    
    def execute(
        self,
        professional_id: int,
        availability_id: Optional[int] = None,
        date: Optional[date] = None,
        start_time: Optional[datetime] = None,
        end_time: Optional[datetime] = None,
        slot_duration_minutes: Optional[int] = None,
        status: Optional[str] = None,
    ) -> List[Availability]:
        professional = self.professional_repository.get_by_id(professional_id)
        
        if not professional:
            raise ValueError("Professional not found")
        
        return self.availability_repository.list_by_professional(
            professional_id=professional_id,
            filters={
                "id": availability_id,
                "date": date,
                "start_time": start_time,
                "end_time": end_time,
                "slot_duration_minutes": slot_duration_minutes,
                "status": status,
            }
        )

from abc import ABC, abstractmethod
from datetime import date, datetime

from domain.entities.availability import Availability, AvailabilityStatus


class AvailabilityRepository(ABC):
    @abstractmethod
    def get_by_id(self, availability_id: int) -> Availability | None:
        pass
    
    @abstractmethod
    def list_by_professional(
        self,
        professional_id: int,
        availability_id: int | None = None,
        date: date | None = None,
        start_time: datetime | None = None,
        end_time: datetime | None = None,
        slot_duration_minutes: int | None = None,
        status: AvailabilityStatus | None = None,
    ) -> list[Availability]:
        pass
    
    @abstractmethod
    def save(self, availability: Availability) -> None:
        pass
    
    @abstractmethod
    def delete(self, availability_id: int) -> None:
        pass
    
    @abstractmethod
    def delete_by_professional(self, professional_id: int) -> None:
        pass
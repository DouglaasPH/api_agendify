from abc import ABC, abstractmethod

from domain.entities.availability import Availability


class AvailabilityRepository(ABC):
    @abstractmethod
    def get_by_id(self, availability_id: int, professional_id: int) -> Availability | None:
        pass
    
    @abstractmethod
    def list_by_professional(
        self,
        professional_id: int,
        filters: dict,
    ) -> list[Availability]:
        pass
    
    @abstractmethod
    def save(self, availability: Availability) -> None:
        pass

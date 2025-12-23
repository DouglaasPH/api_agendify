from abc import ABC, abstractmethod
from datetime import date, datetime

from domain.entities.appointment import Appointment


class AppointmentRepository(ABC):
    @abstractmethod
    def get_by_id(self, appointment_id: int) -> Appointment | None:
        pass
    
    @abstractmethod
    def list_by_professional(
        self,
        professional_id: int,
        availability_id: int | None = None,
        status: str | None = None,
        customer_name: str | None = None,
        customer_email: str | None = None,
        date: date | None = None,
        start_time: datetime | None = None,
        end_time: datetime | None = None,
        slot_duration_minutes: int | None = None,
    ) -> list[Appointment]:
        pass
    
    @abstractmethod
    def save(self, appointment: Appointment) -> None:
        pass
    
    @abstractmethod
    def delete(self, appointment_id: int) -> None:
        pass
    
    @abstractmethod
    def list_by_customer(self, customer_id: int) -> list[Appointment]:
        pass
    
    @abstractmethod
    def list_by_professional(
        self,
        professional_id: int,
        availability_id: int | None = None,
        status: str | None = None,
        customer_name: str | None = None,
        customer_email: str | None = None,
        date: date | None = None,
        start_time: datetime | None = None,
        end_time: datetime | None = None,
        slot_duration_minutes: int | None = None,
    ) -> list[Appointment]:
        pass
    
    @abstractmethod
    def delete_by_professional(self, professional_id: int) -> None:
        pass
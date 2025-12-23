from datetime import date, datetime
from typing import List, Optional

from domain.entities.appointment import Appointment, AppointmentStatus
from domain.repositories.appointment_repository import AppointmentRepository
from domain.repositories.customer_repository import CustomerRepository
from domain.repositories.professional_repository import ProfessionalRepository


class ListAppointments:
    def __init__(self, appointment_repository: AppointmentRepository, customer_repository: CustomerRepository, professional_repository: ProfessionalRepository):
        self.appointment_repository = appointment_repository
        self.customer_repository = customer_repository
        self.professional_repository = professional_repository
        
    def list_for_customer(self, customer_id: int) -> List[Appointment]:
        customer = self.customer_repository.get_by_id(customer_id)
        
        if not customer:
            raise ValueError("Costumer not found")
        
        return self.appointment_repository.list_by_customer(customer_id)
    
    def list_for_professional(
        self,
        professional_id: int,
        availability_id: Optional[int] = None,
        status: Optional[AppointmentStatus] = None,
        customer_name: Optional[str] = None,
        customer_email: Optional[str] = None,
        date: Optional[date] = None,
        start_time: Optional[datetime] = None,
        end_time: Optional[datetime] = None,
        slot_duration_minutes: Optional[int] = None,
    ) -> List[Appointment]:
        professional = self.professional_repository.get_by_id(professional_id)
        
        if not professional:
            raise ValueError("Professional not found")
        
        return self.appointment_repository.list_by_professional(
            professional_id=professional_id, 
            availability_id=availability_id,
            status=status,
            customer_name=customer_name,
            customer_email=customer_email,
            date=date,
            start_time=start_time,
            end_time=end_time,
            slot_duration_minutes=slot_duration_minutes,
        )

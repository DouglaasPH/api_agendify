from domain.entities.appointment import Appointment
from domain.repositories.appointment_repository import AppointmentRepository
from domain.repositories.availability_repository import AvailabilityRepository
from domain.repositories.customer_repository import CustomerRepository
from domain.repositories.professional_repository import ProfessionalRepository


class CreateAppointment:
    def __init__(self, appointment_repository: AppointmentRepository, availability_repository: AvailabilityRepository, customer_repository: CustomerRepository, professional_repository: ProfessionalRepository):
        self.appointment_repository = appointment_repository
        self.availability_repository = availability_repository
        self.customer_repository = customer_repository
        self.professional_repository = professional_repository
    
    def execute(self, professional_id: int, customer_id: int, availability_id: int) -> None:
        customer = self.customer_repository.get_by_id(customer_id)
        
        if not customer:
            raise ValueError("customer not found")
        
        professional = self.professional_repository.get_by_id(professional_id)
        
        if not professional:
            raise ValueError("professional not found")
        
        if not customer.can_create_appointment():
            raise ValueError("customer is not active")
        
        availability = self.availability_repository.get_by_id(availability_id)
        
        if not availability:
            raise ValueError("Availability not found")
        
        if availability.professional_id != professional_id:
            raise PermissionError("Availability does not belong to this professional")
        
        if not availability.is_available():
            raise ValueError("Availability is not available")
        
        availability.occupy()
        
        appointment = Appointment(
            id=None,
            availability_id=availability_id,
            professional_id=professional_id,
            customer_id=customer_id
        )
        
        self.appointment_repository.save(appointment)
        self.availability_repository(availability)

from domain.repositories.appointment_repository import AppointmentRepository
from domain.repositories.customer_repository import CustomerRepository
from domain.repositories.professional_repository import ProfessionalRepository


class CancelAppointment:
    def __init__(self, professional_repository: ProfessionalRepository, customer_repository: CustomerRepository, appointment_repository: AppointmentRepository):
        self.professional_repository = professional_repository
        self.customer_repository = customer_repository
        self.appointment_repository = appointment_repository
    
    def _get_confirmed_appointment(self, appointment_id: int):
        appointment = self.appointment_repository.get_by_id(appointment_id)
        
        if not appointment:
            raise ValueError("Appointment not found")
        
        if not appointment.is_confirmed():
            raise ValueError("Appointment is not confirmed")
        
        return appointment

    def cancel_by_professional(self, appointment_id: int, professional_id: int) -> None:
        professional = self.professional_repository.get_by_id(professional_id)
        
        if not professional:
            raise ValueError("professional not found")
        
        appointment = self._get_confirmed_appointment(appointment_id)
        
        if appointment.professional_id != professional_id:
            raise PermissionError("Appointment does not belong to this professional")
                
        appointment.cancel()
        self.appointment_repository.save(appointment)

    def cancel_by_customer(self, appointment_id: int, customer_id:int):
        customer = self.customer_repository.get_by_id(customer_id)
        
        if not customer:
            raise ValueError("customer not found")

        if not customer.can_cancel_appointment():
            raise ValueError("customer is not active")
        
        appointment = self._get_confirmed_appointment(appointment_id)
        
        if appointment.customer_id != customer_id:
            raise PermissionError("Appointment does not belong to this customer")
        
        appointment.cancel()
        self.appointment_repository.save(appointment)

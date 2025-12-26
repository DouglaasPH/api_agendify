from domain.repositories.appointment_repository import AppointmentRepository
from domain.repositories.professional_repository import ProfessionalRepository


class GetByIdAppointment:
    def __init__(
        self,
        appointment_repository: AppointmentRepository,
        professional_repository: ProfessionalRepository,
    ):
        self.appointment_repository = appointment_repository
        self.professional_repository = professional_repository

    def execute(
        self,
        professional_id: int,
        appointment_id: int,
    ) -> AppointmentRepository:
        professional = self.professional_repository.get_by_id(professional_id)

        if not professional:
            raise ValueError("Professional not found")

        appointment = self.appointment_repository.get_by_id(
            appointment_id=appointment_id
        )

        if not appointment:
            raise ValueError("Appointment not found")

        if appointment.professional_id != professional_id:
            raise PermissionError("You do not have access to this appointment")

        return appointment

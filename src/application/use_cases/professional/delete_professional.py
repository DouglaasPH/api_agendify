from domain.repositories.appointment_repository import AppointmentRepository
from domain.repositories.availability_repository import AvailabilityRepository
from domain.repositories.professional_repository import ProfessionalRepository
from domain.repositories.refresh_token_repository import RefreshTokenRepository


class DeleteProfessionalAccount:
    def __init__(
        self,
        professional_repository: ProfessionalRepository,
        appointment_repository: AppointmentRepository,
        availability_repository: AvailabilityRepository,
        refresh_token_repository: RefreshTokenRepository,
    ):
        self.professional_repository = professional_repository
        self.appointment_repository = appointment_repository
        self.availability_repository = availability_repository
        self.refresh_token_repository = refresh_token_repository

    def execute(self, professional_id: int) -> None:
        professional = self.professional_repository.get_by_id(professional_id)

        if not professional:
            raise ValueError("Professional not found")

        self.refresh_token_repository.revoke_all_by_professional(professional_id)

        all_appointments = self.appointment_repository.list_by_professional(
            professional_id,
            {}
        )

        for appointment in all_appointments:
            appointment.delete()
            self.appointment_repository.save(appointment)

        all_availabilities = self.availability_repository.list_by_professional(
            professional_id,
            {}
        )

        for availability in all_availabilities:
            availability.delete()
            self.availability_repository.save(availability)

        professional.delete()
        self.professional_repository.save(professional)

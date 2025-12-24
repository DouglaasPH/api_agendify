from application.use_cases.appointment.cancel_appointment import CancelAppointment
from application.use_cases.appointment.create_appointment import CreateAppointment
from application.use_cases.appointment.get_by_id_appointment import GetByIdAppointment
from application.use_cases.appointment.list_appointment import ListAppointments

from infrastructure.database.repositories.appointment_repository import AppointmentRepositorySQLAlchemy
from infrastructure.database.repositories.availability_repository import AvailabilityRepositorySQLAlchemy
from infrastructure.database.repositories.customer_repository import CustomerRepositorySQLAlchemy
from infrastructure.database.repositories.professional_repository import ProfessionalRepositorySQLAlchemy


def get_create_appointment_use_case() -> CreateAppointment:
    return CreateAppointment(
        appointment_repository=AppointmentRepositorySQLAlchemy(),
        availability_repository=AvailabilityRepositorySQLAlchemy(),
        customer_repository=CustomerRepositorySQLAlchemy(),
        professional_repository=ProfessionalRepositorySQLAlchemy(),
    )


def get_cancel_appointment() -> CancelAppointment:
    return CancelAppointment(
        professional_repository=ProfessionalRepositorySQLAlchemy(),
        customer_repository=CustomerRepositorySQLAlchemy(),
        appointment_repository=AppointmentRepositorySQLAlchemy(),
    )


def get_by_id_appointment() -> GetByIdAppointment:
    return GetByIdAppointment(
        appointment_repository=AppointmentRepositorySQLAlchemy(),
        professional_repository=ProfessionalRepositorySQLAlchemy(),
    )


def get_list_appointment() -> ListAppointments:
    return ListAppointments(
        appointment_repository=AppointmentRepositorySQLAlchemy(),
        customer_repository=CustomerRepositorySQLAlchemy(),
        professional_repository=ProfessionalRepositorySQLAlchemy(),
    )

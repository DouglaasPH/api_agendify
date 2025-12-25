from fastapi import Depends

from database import get_db

from application.use_cases.appointment.cancel_appointment import CancelAppointment
from application.use_cases.appointment.create_appointment import CreateAppointment
from application.use_cases.appointment.get_by_id_appointment import GetByIdAppointment
from application.use_cases.appointment.list_appointment import ListAppointments

from infrastructure.database.repositories.appointment_repository import AppointmentRepositorySQLAlchemy
from infrastructure.database.repositories.availability_repository import AvailabilityRepositorySQLAlchemy
from infrastructure.database.repositories.customer_repository import CustomerRepositorySQLAlchemy
from infrastructure.database.repositories.professional_repository import ProfessionalRepositorySQLAlchemy


def get_create_appointment_use_case(
    db = Depends(get_db)
) -> CreateAppointment:
    return CreateAppointment(
        appointment_repository=AppointmentRepositorySQLAlchemy(db),
        availability_repository=AvailabilityRepositorySQLAlchemy(db),
        customer_repository=CustomerRepositorySQLAlchemy(db),
        professional_repository=ProfessionalRepositorySQLAlchemy(db),
    )


def get_cancel_appointment(
    db = Depends(get_db)
) -> CancelAppointment:
    return CancelAppointment(
        professional_repository=ProfessionalRepositorySQLAlchemy(db),
        customer_repository=CustomerRepositorySQLAlchemy(db),
        appointment_repository=AppointmentRepositorySQLAlchemy(db),
        availability_repository=AvailabilityRepositorySQLAlchemy(db),
    )


def get_by_id_appointment(
    db = Depends(get_db)
) -> GetByIdAppointment:
    return GetByIdAppointment(
        appointment_repository=AppointmentRepositorySQLAlchemy(db),
        professional_repository=ProfessionalRepositorySQLAlchemy(db),
    )


def get_list_appointment(
    db = Depends(get_db)
) -> ListAppointments:
    return ListAppointments(
        appointment_repository=AppointmentRepositorySQLAlchemy(db),
        customer_repository=CustomerRepositorySQLAlchemy(db),
        professional_repository=ProfessionalRepositorySQLAlchemy(db),
    )

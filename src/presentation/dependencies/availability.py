from application.use_cases.availability.create_availability import CreateAvailability
from application.use_cases.availability.delete_availability import DeleteAvailability
from application.use_cases.availability.get_by_id_availability import GetByIdAvailability
from application.use_cases.availability.list_availability import ListAvailability

from infrastructure.database.repositories.availability_repository import AvailabilityRepositorySQLAlchemy
from infrastructure.database.repositories.professional_repository import ProfessionalRepositorySQLAlchemy


def get_create_availability_use_case() -> CreateAvailability:
    return CreateAvailability(
        availability_repository=AvailabilityRepositorySQLAlchemy(),
        professional_repository=ProfessionalRepositorySQLAlchemy(),
    )


def get_delete_availability_use_case() -> DeleteAvailability:
    return DeleteAvailability(
        availability_repository=AvailabilityRepositorySQLAlchemy(),
        professional_repository=ProfessionalRepositorySQLAlchemy(),
    )


def get_by_id_availability_use_case() -> GetByIdAvailability:
    return GetByIdAvailability(
        availability_repository=AvailabilityRepositorySQLAlchemy(),
        professional_repository=ProfessionalRepositorySQLAlchemy(),
    )


def get_list_availability_use_case() -> ListAvailability:
    return ListAvailability(
        availability_repository=AvailabilityRepositorySQLAlchemy(),
        professional_repository=ProfessionalRepositorySQLAlchemy(),
    )

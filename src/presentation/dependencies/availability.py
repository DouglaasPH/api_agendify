from fastapi import Depends

from database import get_db

from application.use_cases.availability.create_availability import CreateAvailability
from application.use_cases.availability.delete_availability import DeleteAvailability
from application.use_cases.availability.get_by_id_availability import (
    GetByIdAvailability,
)
from application.use_cases.availability.list_availability import ListAvailability

from infrastructure.database.repositories.availability_repository import (
    AvailabilityRepositorySQLAlchemy,
)
from infrastructure.database.repositories.professional_repository import (
    ProfessionalRepositorySQLAlchemy,
)


def get_create_availability_use_case(db=Depends(get_db)) -> CreateAvailability:
    return CreateAvailability(
        availability_repository=AvailabilityRepositorySQLAlchemy(db),
        professional_repository=ProfessionalRepositorySQLAlchemy(db),
    )


def get_delete_availability_use_case(db=Depends(get_db)) -> DeleteAvailability:
    return DeleteAvailability(
        availability_repository=AvailabilityRepositorySQLAlchemy(db),
        professional_repository=ProfessionalRepositorySQLAlchemy(db),
    )


def get_by_id_availability_use_case(db=Depends(get_db)) -> GetByIdAvailability:
    return GetByIdAvailability(
        availability_repository=AvailabilityRepositorySQLAlchemy(db),
        professional_repository=ProfessionalRepositorySQLAlchemy(db),
    )


def get_list_availability_use_case(db=Depends(get_db)) -> ListAvailability:
    return ListAvailability(
        availability_repository=AvailabilityRepositorySQLAlchemy(db),
        professional_repository=ProfessionalRepositorySQLAlchemy(db),
    )

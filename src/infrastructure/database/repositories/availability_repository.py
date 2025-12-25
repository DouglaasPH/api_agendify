from sqlalchemy.orm import Session

from domain.entities.availability import Availability, AvailabilityStatus
from domain.repositories.availability_repository import AvailabilityRepository
from infrastructure.database.models.availability import AvailabilityModel


class AvailabilityRepositorySQLAlchemy(AvailabilityRepository):

    def __init__(self, session: Session):
        self.session = session

    def save(self, availability: Availability) -> None:
        model = AvailabilityModel(
            professional_id=availability.professional_id,
            date=availability.date,
            start_time=availability.start_time,
            end_time=availability.end_time,
            slot_duration_minutes=availability.slot_duration_minutes,
            status=availability.status,
        )
        self.session.add(model)
        self.session.commit()

    def get_by_id(self, availability_id: int, professional_id: int):
        model = (
            self.session.query(AvailabilityModel)
            .filter_by(id=availability_id, professional_id=professional_id)
            .first()
        )

        if not model:
            return None

        return Availability(
            id=model.id,
            professional_id=model.professional_id,
            date=model.date,
            start_time=model.start_time,
            end_time=model.end_time,
            slot_duration_minutes=model.slot_duration_minutes,
            status=model.status,
        )

    def list_by_professional(self, professional_id: int, filters: dict):
        query = (
            self.session.query(AvailabilityModel)
            .filter(AvailabilityModel.professional_id == professional_id)
            .filter(AvailabilityModel.status != AvailabilityStatus.canceled.value)
            .filter(AvailabilityStatus.status != AvailabilityStatus.deleted.value)
        )

        for field, value in filters.items():
            if value is not None:
                query = query.filter(getattr(AvailabilityModel, field) == value)

        return [
            Availability(
                id=m.id,
                professional_id=m.professional_id,
                date=m.date,
                start_time=m.start_time,
                end_time=m.end_time,
                slot_duration_minutes=m.slot_duration_minutes,
                status=m.status,
            )
            for m in query.all()
        ]

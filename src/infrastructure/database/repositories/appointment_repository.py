from datetime import date, datetime

from sqlalchemy.orm import Session, joinedload

from domain.entities.appointment import Appointment, AppointmentStatus
from domain.repositories.appointment_repository import AppointmentRepository
from infrastructure.database.models.appointment import AppointmentModel
from infrastructure.database.models.availability import AvailabilityModel
from infrastructure.database.models.customer import CustomerModel


class AppointmentRepositorySQLAlchemy(AppointmentRepository):

    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, appointment_id: int) -> Appointment | None:
        model = (
            self.session.query(AppointmentModel)
            .options(joinedload(AppointmentModel.availability))
            .options(joinedload(AppointmentModel.customer))
            .filter(AppointmentModel.id == appointment_id)
            .first()
        )

        if not model:
            return None

        return self._to_entity(model)

    def list_by_professional(
        self,
        professional_id: int,
        availability_id: int | None = None,
        status: AppointmentStatus | None = None,
        customer_name: str | None = None,
        customer_email: str | None = None,
        date: date | None = None,
        start_time: datetime | None = None,
        end_time: datetime | None = None,
        slot_duration_minutes: int | None = None,
    ) -> list[Appointment]:

        query = (
            self.session.query(AppointmentModel)
            .join(AppointmentModel.availability)
            .join(AppointmentModel.customer)
            .filter(AppointmentModel.professional_id == professional_id)
            .filter(AppointmentModel.status != AppointmentStatus.canceled.value)
            .filter(AppointmentModel.status != AppointmentStatus.deleted.value)
        )

        if availability_id:
            query = query.filter(AppointmentModel.availability_id == availability_id)

        if status:
            query = query.filter(AppointmentModel.status == status)

        if customer_name:
            query = query.filter(CustomerModel.name.ilike(f"%{customer_name}%"))

        if customer_email:
            query = query.filter(CustomerModel.email.ilike(f"%{customer_email}%"))

        if date:
            query = query.filter(AvailabilityModel.date == date)

        if start_time:
            query = query.filter(AvailabilityModel.start_time <= start_time)

        if end_time:
            query = query.filter(AvailabilityModel.end_time >= end_time)

        if slot_duration_minutes:
            query = query.filter(
                AvailabilityModel.slot_duration_minutes == slot_duration_minutes
            )

        models = query.all()
        return [self._to_entity(model) for model in models]

    def list_by_customer(
        self,
        customer_id: int,
    ) -> list[Appointment]:

        query = (
            self.session.query(AppointmentModel)
            .join(AppointmentModel.availability)
            .filter(AppointmentModel.customer_id == customer_id)
            .filter(AppointmentModel.status != AppointmentStatus.canceled.value)
            .filter(AppointmentModel.status != AppointmentStatus.deleted.value)
        )

        models = query.all()
        return [self._to_entity(model) for model in models]

    def save(self, appointment: Appointment) -> None:
        model = AppointmentModel(
            id=appointment.id,
            professional_id=appointment.professional_id,
            customer_id=appointment.customer_id,
            availability_id=appointment.availability_id,
            status=appointment.status,
        )

        self.session.merge(model)
        self.session.commit()

    def _to_entity(self, model: AppointmentModel) -> Appointment:
        return Appointment(
            id=model.id,
            professional_id=model.professional_id,
            customer_id=model.customer_id,
            availability_id=model.availability_id,
            status=(
                model.status.value if hasattr(model.status, "value") else model.status
            ),
        )

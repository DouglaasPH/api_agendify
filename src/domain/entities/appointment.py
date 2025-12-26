from enum import Enum


class AppointmentStatus(Enum):
    confirmed = "confirmed"
    canceled = "canceled"
    past = "past"
    deleted = "deleted"


class Appointment:
    def __init__(
        self,
        id: int | None,
        professional_id: int,
        availability_id: int,
        customer_id: int,
        status: AppointmentStatus = AppointmentStatus.confirmed,
    ):
        self.id = id
        self.professional_id = professional_id
        self.availability_id = availability_id
        self.status = status
        self.customer_id = customer_id

    def cancel(self):
        if self.status == AppointmentStatus.canceled:
            raise ValueError("Appointment already cancelled.")

        if self.status == AppointmentStatus.past:
            raise ValueError("A past appointment cannot be cancelled.")

        self.status = AppointmentStatus.canceled

    def delete(self):
        if self.status == AppointmentStatus.deleted:
            raise ValueError("Appointment already deleted.")

        self.status = AppointmentStatus.deleted

    def mark_as_past(self):
        if self.status != AppointmentStatus.confirmed:
            return

        self.status = AppointmentStatus.past

    def is_confirmed(self):
        return self.status == AppointmentStatus.confirmed.value

from enum import Enum


class AppointmentStatus(Enum):
    CONFIRMED = "confirmed"
    CANCELED = "canceled"
    PAST = "past"
    DELETED = "deleted"


class Appointment:
    def __init__(self, id: int | None, professional_id: int, availability_id: int, customer_id: int, status: AppointmentStatus = AppointmentStatus.CONFIRMED):
        self.id = id
        self.professional_id = professional_id
        self.availability_id = availability_id
        self.status = status
        self.customer_id = customer_id
    
    def cancel(self):
        if self.status == AppointmentStatus.CANCELED:
            raise ValueError("Appointment already cancelled.")
        
        if self.status == AppointmentStatus.PAST:
            raise ValueError("A past appointment cannot be cancelled.")
        
        self.status = AppointmentStatus.CANCELED
        
    def delete(self):
        if self.status == AppointmentStatus.DELETED:
            raise ValueError("Appointment already deleted.")
        
        self.status = AppointmentStatus.DELETED
    
    def mark_as_past(self):
        if self.status != AppointmentStatus.CONFIRMED:
            return
        
        self.status = AppointmentStatus.PAST

    def is_confirmed(self):
        return self.status == AppointmentStatus.CONFIRMED

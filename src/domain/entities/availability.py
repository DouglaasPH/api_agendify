from enum import Enum
from datetime import date, datetime


class AvailabilityStatus(Enum):
    available = "available"
    occupied = "occupied"
    canceled = "canceled"
    past = "past"
    deleted = "deleted"


class Availability:
    def __init__(self, id: int, professional_id: int, date: date, start_time: datetime, end_time: datetime, slot_duration_minutes: int, status: AvailabilityStatus):
        self.id = id
        self.professional_id = professional_id
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.slot_duration_minutes = slot_duration_minutes
        self.status = status
    
    def cancel(self):
        if self.status == AvailabilityStatus.canceled:
            raise ValueError("Availability already cancelled.")
        
        if self.status == AvailabilityStatus.past:
            raise ValueError("A past availability cannot be cancelled.")
        
        self.status = AvailabilityStatus.canceled
    
    def delete(self):
        if self.status == AvailabilityStatus.deleted:
            raise ValueError("Availability already deleted.")
        
        self.status = AvailabilityStatus.deleted
    
    def mark_as_past(self):
        if self.status != AvailabilityStatus.available:
            return
        
        self.status = AvailabilityStatus.past
    
    def occupy(self):
        if self.status == AvailabilityStatus.occupied:
            raise ValueError("Availability already occupied")
        self.status = AvailabilityStatus.occupied

    def release(self):
        self.status = AvailabilityStatus.available
        
    def is_available(self):
        return self.status == AvailabilityStatus.available.value
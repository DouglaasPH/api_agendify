from enum import Enum
from datetime import date, datetime


class AvailabilityStatus(Enum):
    AVAILABLE = "available"
    OCCUPIED = "occupied"
    CANCELED = "canceled"
    PAST = "past"
    DELETED = "deleted"


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
        if self.status == AvailabilityStatus.CANCELED:
            raise ValueError("Availability already cancelled.")
        
        if self.status == AvailabilityStatus.PAST:
            raise ValueError("A past availability cannot be cancelled.")
        
        self.status = AvailabilityStatus.CANCELED
    
    def delete(self):
        if self.status == AvailabilityStatus.DELETED:
            raise ValueError("Availability already deleted.")
        
        self.status = AvailabilityStatus.DELETED
    
    def mark_as_past(self):
        if self.status != AvailabilityStatus.AVAILABLE:
            return
        
        self.status = AvailabilityStatus.PAST
    
    def occupy(self):
        if self.status == AvailabilityStatus.OCCUPIED:
            raise ValueError("Availability already occupied")
        self.status = AvailabilityStatus.OCCUPIED

    def release(self):
        self.status = AvailabilityStatus.AVAILABLE
        
    def is_available(self):
        return self.status == AvailabilityStatus.AVAILABLE
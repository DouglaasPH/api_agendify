from enum import Enum


class CustomerStatus(Enum):
    active = "active"
    deleted = "deleted"


class Customer:
    def __init__(self, id: int | None, name: str, email: str, status: CustomerStatus):
        self.id = id
        self.name = name
        self.email = email
        self.status = status
    
    def can_create_appointment(self) -> bool:
        return self.status == CustomerStatus.active
    
    def can_cancel_appointment(self) -> bool:
        return self.status == CustomerStatus.active
    
    def deactive(self):
        self.status = CustomerStatus.delete

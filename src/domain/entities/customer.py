class Customer:
    def __init__(self, id: int | None, name: str, email: str, is_active: bool):
        self.id = id
        self.name = name
        self.email = email
        self.is_active = is_active
    
    def can_create_appointment(self) -> bool:
        return self.is_active
    
    def can_cancel_appointment(self) -> bool:
        return self.is_active
    
    def deactive(self):
        self.is_active = False

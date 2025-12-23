from enum import Enum

class ProfessionalStatus(Enum):
    ACTIVE = "active"
    DELETED = "deleted"


class Professional:
    def __init__(
        self, 
        id: int, 
        profile_avatar_id: int, 
        name: str, 
        hashed_password: str, 
        email: str, 
        profession: str, 
        phone_number: str, 
        chat_code: str, 
        status: ProfessionalStatus
    ):
        self.id = id
        self.profile_avatar_id = profile_avatar_id
        self.name = name
        self.hashed_password = hashed_password
        self.email = email
        self.profession = profession
        self.phone_number = phone_number
        self.chat_code = chat_code
        self.status = status
    
    def update_profile(self, name: str, profession: str, phone_number: str):
        if not name:
            raise ValueError("Required name")
        
        self.name = name
        self.profession = profession
        self.phone_number = phone_number
    
    def update_profile_avatar_id(self, new_profile_avatar_id: int):
        if not new_profile_avatar_id:
            raise ValueError("Invalid Avatar ID")
        
        self.profile_avatar_id = new_profile_avatar_id
    
    def change_password(self, new_hashed_password: str):
        if not new_hashed_password:
            raise ValueError("Invalid password")
        
        self.hashed_password = new_hashed_password
    
    def is_active(self) -> bool:
        return self.status == ProfessionalStatus.ACTIVE

    def delete(self):
        if self.status == ProfessionalStatus.DELETED:
            raise ValueError("Professional already deleted")

        self.status = ProfessionalStatus.DELETED

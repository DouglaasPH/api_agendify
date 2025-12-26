from enum import Enum


class ProfessionalStatus(Enum):
    active = "active"
    deleted = "deleted"


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
        status: ProfessionalStatus,
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

    def update_profile(
        self,
        name: str | None = None,
        profession: str | None = None,
        phone_number: str | None = None,
    ):
        if name is not None:
            self.name = name

        if profession is not None:
            self.profession = profession

        if phone_number is not None:
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
        return self.status == ProfessionalStatus.active

    def delete(self):
        if self.status == ProfessionalStatus.deleted:
            raise ValueError("Professional already deleted")

        self.status = ProfessionalStatus.deleted

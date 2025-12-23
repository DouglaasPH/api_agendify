class ProfessionalOutputDTO:
    def __init__(
        self,
        id: int,
        name: str,
        email: str,
        phone_number: str,
        profession: str,
        profile_avatar_id: int | None,
        chat_code: str,
    ):
        self.id = id
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.profession = profession
        self.profile_avatar_id = profile_avatar_id
        self.chat_code = chat_code

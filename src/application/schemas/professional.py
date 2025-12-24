from typing import Optional
from pydantic import BaseModel


class DataToVerifyAccount(BaseModel):
    name: str
    email: str
    password: str
    profession: str
    profileAvatarId: int
    phoneNumber: str


class ProfessionalOutputSchema(BaseModel):
    id: int
    name: str
    email: str
    phone_number: str
    profession: str
    profile_avatar_id: int | None
    chat_code: str


class Token(BaseModel):
    token: str


class DataToUpdate(BaseModel):
    name: Optional[str] = None
    profession: Optional[str] = None
    profile_avatar_id: Optional[int] = None
    phone_number: Optional[str] = None


class ProfessionalEmailToUpdate(BaseModel):
    new_email: str


class EmailData(BaseModel):
    email: str


class ResetPasswordData(BaseModel):
    new_password: str
    token: str

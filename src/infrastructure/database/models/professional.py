from sqlalchemy import Column, Enum, Integer, String, Index
from sqlalchemy.orm import relationship

from domain.entities.professional import ProfessionalStatus
from infrastructure.database.database import Base


class ProfessionalModel(Base):
    __tablename__ = "professional"

    id = Column(Integer, primary_key=True, index=True)
    profile_avatar_id = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    email = Column(String, nullable=False)
    profession = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    chat_code = Column(String, nullable=False)
    status = Column(
        Enum(ProfessionalStatus, name="professional_status"),
        default=ProfessionalStatus.active,
        nullable=False,
    )

    refresh_tokens = relationship(
        "RefreshTokenModel", back_populates="professional", cascade="all, delete-orphan"
    )

    __table_args__ = (
        Index(
            "unique_active_professional_email",
            "email",
            unique=True,
            postgresql_where=(status == ProfessionalStatus.active),
        ),
    )

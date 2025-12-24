from enum import Enum

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from domain.entities.professional import ProfessionalStatus
from infrastructure.database.base import Base


class ProfessionalModel(Base):
    __tablename__ = "professional"
    
    id = Column(Integer, primary_key=True, index=True)
    profile_avatar_id = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    profession = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    chat_code = Column(String, nullable=False)
    status = Column(Enum(ProfessionalStatus), default=ProfessionalStatus.ACTIVE, nullable=False)
    
    refresh_tokens = relationship("RefreshTokenModel", back_populates="professional")

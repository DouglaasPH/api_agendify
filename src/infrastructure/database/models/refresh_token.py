from datetime import datetime, timezone
from sqlalchemy.orm import relationship
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, DateTime

from infrastructure.database.base import Base

class RefreshTokenModel(Base):
    __tablename__ = "refresh_token"
    
    id = Column(Integer, primary_key=True, index=True)
    professional_id = Column(Integer, ForeignKey("professional.id"))
    token = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.now(timezone.utc))
    expires_at = Column(DateTime(timezone=True), nullable=False)
    is_revoked = Column(Boolean, default=False)
    
    professional = relationship(
        "ProfessionalModel",
        back_populates="refresh_tokens"
    )

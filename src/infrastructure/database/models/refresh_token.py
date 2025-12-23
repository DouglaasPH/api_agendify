from datetime import datetime, timezone
from sqlalchemy.orm import relationship
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, DateTime

from database import Base

class RefreshTokenModel(Base):
    __tablename__ = "refresh_token"
    
    id = Column(Integer, primary_key=True, index=True)
    profession_id = Column(Integer, ForeignKey("professional.id"))
    token = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    expires_at = Column(DateTime, nullable=False)
    is_revoked = Column(Boolean, default=False)
    
    professionals = relationship("ProfessionalModel", back_populates="refresh_token")
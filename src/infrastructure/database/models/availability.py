import enum

from sqlalchemy import Column, Integer, DateTime, ForeignKey, Date, Enum
from sqlalchemy.orm import relationship

from infrastructure.database.base import Base
from domain.entities.availability import AvailabilityStatus


class AvailabilityModel(Base):
    __tablename__ = "availability"
    
    id = Column(Integer, primary_key=True, index=True)
    professional_id = Column(Integer, ForeignKey("professional.id"))
    date = Column(Date, nullable=False)
    start_time = Column(DateTime(timezone=True), nullable=False)
    end_time = Column(DateTime(timezone=True), nullable=False)
    slot_duration_minutes = Column(Integer, nullable=False)
    status = Column(Enum(AvailabilityStatus), default=AvailabilityStatus.available, nullable=False)
    
    appointments = relationship(
        "AppointmentModel",
        back_populates="availability",
        cascade="all, delete-orphan"
    )

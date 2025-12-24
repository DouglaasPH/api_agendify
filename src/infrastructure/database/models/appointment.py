import enum

from sqlalchemy import Column, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship

from infrastructure.database.base import Base
from domain.entities.appointment import AppointmentStatus


class AppointmentModel(Base):
    __tablename__ = "appointments"
    
    id = Column(Integer, primary_key=True, index=True)
    professional_id = Column(Integer, ForeignKey("professionals.id"))
    availability_id = Column(Integer, ForeignKey("availability.id"), unique=False)
    status = Column(Enum(AppointmentStatus), default=AppointmentStatus.CONFIRMED, nullable=False)    
    customer_id = Column(Integer, ForeignKey("customers.id"), unique=False)
    
    availabilities = relationship("Availability", back_populates="appointment")
    customers = relationship("Customer", back_populates="appointment")

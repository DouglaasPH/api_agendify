import enum

from sqlalchemy import Column, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship

from infrastructure.database.base import Base
from domain.entities.appointment import AppointmentStatus


class AppointmentModel(Base):
    __tablename__ = "appointment"
    
    id = Column(Integer, primary_key=True, index=True)
    professional_id = Column(Integer, ForeignKey("professional.id"))
    availability_id = Column(Integer, ForeignKey("availability.id"), unique=False)
    status = Column(Enum(AppointmentStatus), default=AppointmentStatus.confirmed, nullable=False)    
    customer_id = Column(Integer, ForeignKey("customer.id"), unique=False)
    
    availability = relationship(
        "AvailabilityModel",
        back_populates="appointments"
    )

    customer = relationship(
        "CustomerModel",
        back_populates="appointments"
    )

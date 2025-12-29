from sqlalchemy import Column, Enum, ForeignKey, Integer
from sqlalchemy.orm import relationship

from domain.entities.appointment import AppointmentStatus
from infrastructure.database.database import Base


class AppointmentModel(Base):
    __tablename__ = "appointment"

    id = Column(Integer, primary_key=True, index=True)
    professional_id = Column(Integer, ForeignKey("professional.id"))
    availability_id = Column(Integer, ForeignKey("availability.id"), unique=False)
    status = Column(
        Enum(AppointmentStatus), default=AppointmentStatus.confirmed, nullable=False
    )
    customer_id = Column(Integer, ForeignKey("customer.id"), unique=False)

    availability = relationship("AvailabilityModel", back_populates="appointments")

    customer = relationship("CustomerModel", back_populates="appointments")

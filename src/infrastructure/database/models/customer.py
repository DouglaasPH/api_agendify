from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship

from domain.entities.customer import CustomerStatus
from infrastructure.database.base import Base


class CustomerModel(Base):
    __tablename__ = "customer"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    status = Column(
        Enum(CustomerStatus),
        default=CustomerStatus.ACTIVE,
        nullable=False
    )
    
    appointments = relationship("AppointmentModel", back_populates="customer", uselist=False)

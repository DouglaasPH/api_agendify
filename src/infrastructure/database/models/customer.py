from sqlalchemy import Column, Enum, Integer, String, Index
from sqlalchemy.orm import relationship

from domain.entities.customer import CustomerStatus
from infrastructure.database.database import Base


class CustomerModel(Base):
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    status = Column(Enum(CustomerStatus), default=CustomerStatus.active, nullable=False)

    appointments = relationship("AppointmentModel", back_populates="customer")

    __table_args__ = (
        Index(
            "unique_active_customer_email",
            "email",
            unique=True,
            postgresql_where=(status == CustomerStatus.active),
        ),
    )

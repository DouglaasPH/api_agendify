from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from infrastructure.database.base import Base

class CustomerModel(Base):
    __tablename__ = "customer"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    
    appointments = relationship("Appointment", back_populates="customer", uselist=False)

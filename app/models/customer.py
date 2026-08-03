from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(255), nullable=True)
    phone = Column(String(20), nullable=True)

    sales = relationship("Sale", back_populates="customer")
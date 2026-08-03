from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(255), nullable=False)
    username = Column(String(50), nullable=True)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(20), nullable=True)

    sales = relationship("Sale", back_populates="user")
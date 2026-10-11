from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String, default="staff")  # admin ya staff

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, index=True)
    phone_number = Column(String)
    bike_model = Column(String)
    battery_number = Column(String, unique=True)
    created_at = Column(DateTime, default=func.now())

    # Relations
    service_logs = relationship("ServiceLog", back_populates="customer", cascade="all, delete-orphan")

class ServiceLog(Base):
    __tablename__ = "service_logs"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    note = Column(String)
    service_date = Column(DateTime, default=func.now())

    customer = relationship("Customer", back_populates="service_logs")
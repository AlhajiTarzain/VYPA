from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(50), unique=True, index=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    unit = Column(String(50))
    service_number = Column(String(50), unique=True, index=True)
    hashed_password = Column(String(50))


class Car(Base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key=True, index=True)
    car_make = Column(String(50), index=True)
    car_model = Column(String(50), index=True)
    year = Column(Integer)
    registration_number = Column(String(50), unique=True, index=True)
    car_type = Column(String(50))


class Driver(Base):
    __tablename__ = "drivers"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    date_of_birth = Column(Date)
    arm_of_service = Column(String(50))
    car_types = Column(String(50))  # Assuming it stores types as a comma-separated string
    photo_upload = Column(String(50))  # File path or URL
    driver_license_upload = Column(String(50))  # File path or URL
    military_license_upload = Column(String(50))  # 
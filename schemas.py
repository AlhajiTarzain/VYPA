from datetime import date
from typing import Optional
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    unit: str
    service_number: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class CarBase(BaseModel):
    car_make: str
    car_model: str
    year: int
    registration_number: str
    car_type: str

class CarCreate(CarBase):
    pass

class Car(CarBase):
    id: int

    class Config:
        orm_mode = True

class DriverBase(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: date
    arm_of_service: str
    car_types: str
    photo_upload: Optional[str] = None
    driver_license_upload: Optional[str] = None
    military_license_upload: Optional[str] = None

class DriverCreate(DriverBase):
    pass

class Driver(DriverBase):
    id: int

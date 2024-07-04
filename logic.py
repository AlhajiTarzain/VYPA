from sqlalchemy.orm import Session
import models, schemas
from utils import get_password_hash

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_user_by_service_number(db: Session, service_number: str):
    return db.query(models.User).filter(models.User.service_number == service_number).first()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        unit=user.unit,
        service_number=user.service_number,
        hashed_password=get_password_hash(user.password),
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_car(db: Session, car: schemas.CarCreate):
    db_car = models.Car(
        car_make=car.car_make,
        car_model=car.car_model,
        year=car.year,
        registration_number=car.registration_number,
        car_type=car.car_type,
    )
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

def get_cars(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Car).offset(skip).limit(limit).all()


def get_car_count(db: Session):
    return db.query(models.Car).count()
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
import models, database, logic, schemas
from auth import router as auth_router

# models.Base.metadata.drop_all(bind=database.engine)
models.Base.metadata.create_all(bind=database.engine)


app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["auth"])

@app.post("/cars/", response_model=schemas.Car)
def create_car(car: schemas.CarCreate, db: Session = Depends(database.get_db)):
    return logic.create_car(db=db, car=car)

@app.get("/cars/", response_model=list[schemas.Car])
def read_cars(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    cars = logic.get_cars(db, skip=skip, limit=limit)
    return cars

@app.get("/cars/count/", response_model=int)
def count_cars(db: Session = Depends(database.get_db)):
    return logic.get_car_count(db)
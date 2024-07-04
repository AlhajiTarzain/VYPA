from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
import models, database, logic, schemas
from auth import router as auth_router
from fastapi.middleware.cors import CORSMiddleware

# models.Base.metadata.drop_all(bind=database.engine)
models.Base.metadata.create_all(bind=database.engine)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

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


@app.post("/drivers/", response_model=schemas.Driver)
def create_driver(driver: schemas.DriverCreate, db: Session = Depends(database.get_db)):
    return logic.create_driver(db=db, driver=driver)

@app.get("/drivers/", response_model=list[schemas.Driver])
def read_drivers(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return logic.get_drivers(db, skip=skip, limit=limit)

@app.get("/drivers/count/", response_model=int)
def count_drivers(db: Session = Depends(database.get_db)):
    return logic.get_driver_count(db)
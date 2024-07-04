from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

MYSQL_USER = 'root'
MYSQL_PASSWORD = ''
MYSQL_HOST = 'localhost:3306'
MYSQL_DATABASE = 'vypa_db'

# Create an engine that stores data in the local directory's sqlite database file.
engine = create_engine(f'mysql+mysqldb://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DATABASE}')

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

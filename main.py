from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

MYSQL_USER = 'root'
MYSQL_PASSWORD = ''
MYSQL_HOST = 'localhost:3306'
MYSQL_DATABASE = 'vypa_db'

# Create an engine that stores data in the local directory's sqlite database file.
engine = create_engine(f'mysql+mysqldb://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DATABASE}')

# Create a base class for declarative class definitions.
Base = declarative_base()

# Define a class representing a table in the database.
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    email = Column(String(50))
    first_name = Column(String(50))
    last_name = Column(String(50))
    unit = Column(String(50))
    service_number = Column(String(50))
    password = Column(String(50))
    nickname = Column(String(50))

    def __repr__(self):
        return f"<User(name='{self.email}', fullname='{self.first_name}', nickname='{self.nickname}')>"

# Create the table in the database.
Base.metadata.create_all(engine)

# Create a configured "Session" class.
Session = sessionmaker(bind=engine)

# Create a session.
session = Session()

# Create instances of the User class.
new_user = User(email='john@gmail.com', first_name='John', last_name='Doe', unit='Signal', service_number='GH1246', password='test', nickname='johnny',)

# Add the record to the session object.
session.add(new_user)

# Commit the record to the database.
session.commit()

# Query the database.
for user in session.query(User).all():
    print(user)


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
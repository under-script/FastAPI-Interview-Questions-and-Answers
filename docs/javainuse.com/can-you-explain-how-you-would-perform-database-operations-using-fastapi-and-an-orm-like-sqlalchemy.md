Here's an explanation of how you can perform database operations using FastAPI and SQLAlchemy.
FastAPI is a modern, fast (high-performance), web framework for building APIs with Python. SQLAlchemy is a popular Object-Relational Mapping (ORM) library that allows you to work with databases using Python objects.

To get started, you'll need to install FastAPI and SQLAlchemy, which can be done with pip, by running the following commands:
```
pip install fastapi
pip install sqlalchemy
```
Once you have them installed, you can start building your API. First, import the required modules:
```python
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
```
Next, create an instance of the FastAPI app and configure your database connection:
```python
app = FastAPI()

SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
```
With the database connection established, you can define your models. Create a Python class for each table in your database, by inheriting from the `Base` class:
```python
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
```
To perform database operations, you'll need to define routes and API endpoints in your FastAPI app. Here's an example of retrieving all users:
```python
from fastapi import Depends

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users
```
In the code above, we use a dependency (`get_db`) to get a database session for each request. Then, within the endpoint function, we query the database to retrieve all users.
This is a simple example, but SQLAlchemy provides a rich set of tools to perform various database operations, including create, read, update, and delete (CRUD). You can refer to SQLAlchemy's documentation for more details on specific operations you want to perform.

Remember to run the FastAPI app using a server like uvicorn:
```
uvicorn main:app --reload
```
With this setup, you can perform database operations using FastAPI and SQLAlchemy. Ensure you modify the code to fit your specific database and requirements.

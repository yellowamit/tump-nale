from sqlmodel import SQLModel, create_engine, Session
from config import DATABASE_URL
engine = create_engine(DATABASE_URL, echo=False,connect_args={"check_same_thread": False})
#by default, SQLite does not allow multiple threads to access the same database connection. The connect_args={"check_same_thread": False} argument allows multiple threads to access the same database connection, which is necessary for FastAPI applications that use SQLite as the database. 
def create_tables():
    SQLModel.metadata.create_all(engine)
def get_session():
    with Session(engine) as session:
        yield session   



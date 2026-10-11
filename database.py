from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Tumhara PostgreSQL connection URL
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Shahzaib@localhost:5432/ebike_db"

# Engine create kar rahe hain PostgreSQL ke liye
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SessionLocal session factory banani hai database operations ke liye
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class jisse hamari models inherit karengi
Base = declarative_base()

# Dependency function jo FastAPI routes mein DB session provide karegi
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
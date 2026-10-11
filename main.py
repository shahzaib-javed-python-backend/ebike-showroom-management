from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from contextlib import asynccontextmanager

# SQLite Database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./ebike.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# SQLAlchemy Model (Database Table)
class CustomerDB(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String, index=True)
    phone_number = Column(String)
    bike_model = Column(String)
    battery_number = Column(String)

# App startup par tables create karne ke liye lifespan context manager
@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(title="E-Bike Showroom Management API", lifespan=lifespan)

# Setup Jinja2 Templates
templates = Jinja2Templates(directory="templates")

# Database Session Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic Model for Request Body Validation
class EBikeCustomer(BaseModel):
    customer_name: str
    phone_number: str
    bike_model: str
    battery_number: str

    class Config:
        from_attributes = True

# --- HTML Template Navigation Routes ---

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse(request, "index.html")

@app.get("/about", response_class=HTMLResponse)
def read_about(request: Request):
    return templates.TemplateResponse(request, "about.html")

@app.get("/services", response_class=HTMLResponse)
def read_services(request: Request):
    return templates.TemplateResponse(request, "services.html")

@app.get("/dashboard", response_class=HTMLResponse)
def read_dashboard(request: Request):
    return templates.TemplateResponse(request, "dashboard.html")

@app.get("/contact", response_class=HTMLResponse)
def read_contact(request: Request):
    return templates.TemplateResponse(request, "contact.html")


# --- API Endpoints for E-Bike Customers ---

# 1. Add Customer (POST)
@app.post("/add-customer")
def add_customer(customer: EBikeDashboardModel if 'EBikeDashboardModel' in globals() else EBikeCustomer, db: Session = Depends(get_db)):
    db_customer = CustomerDB(
        customer_name=customer.customer_name,
        phone_number=customer.phone_number,
        bike_model=customer.bike_model,
        battery_number=customer.battery_number
    )
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return {"message": "Customer & E-Bike data successfully saved in database!", "data": db_customer}

# 2. Get All Customers (GET)
@app.get("/customers")
def get_customers(db: Session = Depends(get_db)):
    customers = db.query(CustomerDB).all()
    return {"total_customers": len(customers), "customers": customers}

# 3. Get Single Customer by ID (GET)
@app.get("/customers/{customer_id}")
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(CustomerDB).filter(CustomerDB.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found!")
    return {"customer": customer}

# 4. Update Customer (PUT)
@app.put("/customers/{customer_id}")
def update_customer(customer_id: int, updated_data: EBikeCustomer, db: Session = Depends(get_db)):
    customer = db.query(CustomerDB).filter(CustomerDB.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found!")
    
    customer.customer_name = updated_data.customer_name
    customer.phone_number = updated_data.phone_number
    customer.bike_model = updated_data.bike_model
    customer.battery_number = updated_data.battery_number
    
    db.commit()
    db.refresh(customer)
    return {"message": "Customer data successfully updated!", "data": customer}

# 5. Delete Customer (DELETE)
@app.delete("/customers/{customer_id}")
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(CustomerDB).filter(CustomerDB.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found!")
    
    db.delete(customer)
    db.commit()
    return {"message": f"Customer with ID {customer_id} successfully deleted!"}
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from backend.database import Base


class Patient(Base):
    __tablename__ = "patients"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    severity = Column(String)
    admitted_at = Column(DateTime, default=datetime.utcnow)

class ICUResource(Base):
    __tablename__ = "icu_resources"
    id = Column(Integer, primary_key=True, index=True)
    resource_type = Column(String)
    status = Column(String)  # available / occupied

class Allocation(Base):
    __tablename__ = "allocations"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    resource_id = Column(Integer, ForeignKey("icu_resources.id"))
    allocated_at = Column(DateTime, default=datetime.utcnow)

class PredictionLog(Base):
    __tablename__ = "prediction_logs"
    id = Column(Integer, primary_key=True, index=True)
    predicted_demand = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)

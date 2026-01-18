from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend.models import Patient


router = APIRouter(prefix="/patients", tags=["Patients"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def add_patient(name: str, severity: str, db: Session = Depends(get_db)):
    patient = Patient(name=name, severity=severity)
    db.add(patient)
    db.commit()
    return {"message": "Patient added"}

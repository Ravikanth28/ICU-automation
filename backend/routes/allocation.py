from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend.models import Patient, ICUResource, Allocation, PredictionLog
from ml.predict import predict_demand
from blockchain.log_allocation import log_to_blockchain


router = APIRouter(prefix="/allocate", tags=["Allocation"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def allocate(db: Session = Depends(get_db)):
    prediction = predict_demand()
    db.add(PredictionLog(predicted_demand=prediction))
    db.commit()

    patient = db.query(Patient).filter(Patient.severity == "high").first()
    resource = db.query(ICUResource).filter(ICUResource.status == "available").first()

    if not patient or not resource:
        return {"message": "No allocation possible"}

    resource.status = "occupied"
    allocation = Allocation(patient_id=patient.id, resource_id=resource.id)
    db.add(allocation)
    db.commit()

    log_to_blockchain(allocation.id)

    return {"message": "Resource allocated", "allocation_id": allocation.id}

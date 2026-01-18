from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend.models import ICUResource


router = APIRouter(prefix="/resources", tags=["Resources"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def add_resource(resource_type: str, db: Session = Depends(get_db)):
    resource = ICUResource(resource_type=resource_type, status="available")
    db.add(resource)
    db.commit()
    return {"message": "Resource added"}

@router.get("/")
def list_resources(db: Session = Depends(get_db)):
    return db.query(ICUResource).all()

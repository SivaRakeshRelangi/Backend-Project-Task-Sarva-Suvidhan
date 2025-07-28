from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from . import models, schemas
from .database import SessionLocal
from typing import List, Optional

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/api/forms/wheel-specifications", status_code=201)
def create_wheel_spec(form: schemas.WheelSpecificationCreate, db: Session = Depends(get_db)):
    if db.query(models.WheelSpecification).filter(models.WheelSpecification.formNumber == form.formNumber).first():
        raise HTTPException(status_code=400, detail="Form already exists.")
    db_form = models.WheelSpecification(**form.dict())
    db.add(db_form)
    db.commit()
    return {
        "success": True,
        "message": "Wheel specification submitted successfully.",
        "data": {
            "formNumber": form.formNumber,
            "submittedBy": form.submittedBy,
            "submittedDate": form.submittedDate,
            "status": "Saved"
        }
    }

@router.get("/api/forms/wheel-specifications", response_model=List[schemas.WheelSpecificationOut])
def get_wheel_specs(
    formNumber: Optional[str] = Query(None),
    submittedBy: Optional[str] = Query(None),
    submittedDate: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(models.WheelSpecification)
    if formNumber:
        query = query.filter(models.WheelSpecification.formNumber == formNumber)
    if submittedBy:
        query = query.filter(models.WheelSpecification.submittedBy == submittedBy)
    if submittedDate:
        query = query.filter(models.WheelSpecification.submittedDate == submittedDate)
    results = query.all()
    return results

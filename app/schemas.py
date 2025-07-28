from pydantic import BaseModel
from datetime import date
from typing import Dict, Optional

class WheelSpecificationCreate(BaseModel):
    formNumber: str
    submittedBy: str
    submittedDate: date
    fields: Dict[str, str]

class WheelSpecificationOut(BaseModel):
    formNumber: str
    submittedBy: str
    submittedDate: date
    fields: Dict[str, str]

    class Config:
        orm_mode = True

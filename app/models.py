from sqlalchemy import Column, String, Date, JSON
from .database import Base

class WheelSpecification(Base):
    __tablename__ = "wheel_specifications"

    formNumber = Column(String, primary_key=True, index=True)
    submittedBy = Column(String, nullable=False)
    submittedDate = Column(Date, nullable=False)
    fields = Column(JSON, nullable=False)

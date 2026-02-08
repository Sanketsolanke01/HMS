from sqlalchemy import Column, Integer, String,ForeignKey
from database import Base

class Patient(Base):
    __tablename__="patient"

    id=Column(Integer,primary_key=True,index=True,nullable=False)
    name=Column(String,nullable=False)
    age=Column(Integer,nullable=False)
    mob=Column(String,nullable=False)
    address=Column(String,nullable=False)
    symptoms=Column(String,nullable=False)
    date_time=Column(String,nullable=False)
    gender=Column(String,nullable=False)

class Doctor(Base):
    __tablename__="doctor"

    id=Column(Integer,primary_key=True,index=True,nullable=False)
    name=Column(String,nullable=False)
    dept=Column(String,nullable=False)
    qualification=Column(String,nullable=False)
    exp=Column(Integer,nullable=False)
    gender=Column(String,nullable=False)

class Appointment(Base):
    __tablename__="appointment"
    id=Column(Integer,primary_key=True,index=True,nullable=False)
    patient_id=Column(Integer,ForeignKey("patient.id"),nullable=False)
    doctor_id=Column(Integer,ForeignKey("doctor.id"),nullable=False)
    date=Column(String,nullable=False)
    time=Column(String,nullable=False)
    reason=Column(String,nullable=False)





class patientAccount(Base):
    __tablename__ = "patientaccount"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)





class AI_Doc(Base):
    __tablename__="ai_queries"
    
    id=Column(Integer,primary_key=True,index=True, nullable=False)
    query=Column(String,nullable=False)
    resolution=Column(String,nullable=False)


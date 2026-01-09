from fastapi import HTTPException
from sqlalchemy.orm import Session

import models, schemas
from hash import generate_hash_password, verify_password


def create_patients(db: Session, patient_data: schemas.patient_Register):
    db_patient = models.Patient(
        name=patient_data.name,
        age=patient_data.age,
        mob=patient_data.mob,
        address=patient_data.address,
        symptoms=patient_data.symptoms,
        date_time=patient_data.date_time,
        gender=patient_data.gender
    )
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient


def create_doctors(db: Session, doctor_data: schemas.create_doctor):
    db_doctor = models.Doctor(
        name=doctor_data.name,
        dept=doctor_data.dept,
        qualification=doctor_data.qualification,
        exp=doctor_data.exp,
        gender=doctor_data.gender
    )
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor


def create_appointments(db: Session, appointment_data: schemas.create_appointment):
    if not db.query(models.Patient).filter(models.Patient.id == appointment_data.patient_id).first():
        raise HTTPException(status_code=404, detail="Patient not found")

    if not db.query(models.Doctor).filter(models.Doctor.id == appointment_data.doctor_id).first():
        raise HTTPException(status_code=404, detail="Doctor not found")

    db_appointment = models.Appointment(
        patient_id=appointment_data.patient_id,
        doctor_id=appointment_data.doctor_id,
        date=appointment_data.date,
        time=appointment_data.time,
        reason=appointment_data.reason
    )

    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment


def get_all_patients(db: Session):
    return db.query(models.Patient).all()


def get_patient_by_id(db: Session, patient_id: int):
    patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient


def get_all_doctors(db: Session):
    return db.query(models.Doctor).all()


def get_doctor_by_id(db: Session, doctor_id: int):
    doctor = db.query(models.Doctor).filter(models.Doctor.id == doctor_id).first()
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor


def get_all_appointments(db: Session):
    return db.query(models.Appointment).all()


def get_appointment_by_id(db: Session, appointment_id: int):
    appointment = db.query(models.Appointment).filter(models.Appointment.id == appointment_id).first()
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return appointment


def create_patient_account(db: Session, register_data: schemas.accountRegister_patient):
    if db.query(models.patientAccount).filter(models.patientAccount.email == register_data.email).first():
        raise HTTPException(status_code=409, detail="Email already exists")

    db_account = models.patientAccount(
        email=register_data.email,
        password=generate_hash_password(register_data.password)
    )

    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account


# from hash import verify_password

def authenticate_patient(db: Session, email: str, password: str):
    patient = db.query(models.patientAccount).filter(
        models.patientAccount.email == email
    ).first()

    if not patient:
        return None

    if not verify_password(password, patient.password):
        return None

    return patient


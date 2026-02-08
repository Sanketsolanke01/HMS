from fastapi import FastAPI, Depends,HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import engine,SessionLocal,Base
import httpx
from jwt_code import create_token, get_current_patient

from fastapi.middleware.cors import CORSMiddleware



Base.metadata.create_all(bind=engine)

app=FastAPI()

# origins = [
#     "http://127.0.0.1:5500/"
# ]


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register",response_model=schemas.patient_Response,status_code=201,tags=["Patient"])
def create_patient(patient_data:schemas.patient_Register,db:Session=Depends(get_db)):
    return crud.create_patients(db=db,patient_data=patient_data)

@app.post("/docRegister",response_model=schemas.doctor_response,status_code=201,tags=["Doctor"])
def create_doctor(doctor_data:schemas.create_doctor,db:Session=Depends(get_db)):
    return crud.create_doctors(db=db,doctor_data=doctor_data)

@app.post("/appointment",response_model=schemas.appointment_response,status_code=201,tags=["Appointment"])
def create_appointment(appointment_data:schemas.create_appointment,db:Session=Depends(get_db)):
    return crud.create_appointments(db=db,appointment_data=appointment_data)

from typing import List

@app.get("/patients",response_model=List[schemas.patient_Response],tags=["Patient"])
def read_all_patients(db: Session = Depends(get_db)):
    return crud.get_all_patients(db)

@app.get("/patients/{patient_id}",response_model=schemas.patient_Response,tags=["Patient"])
def read_patient_by_id(patient_id: int,db: Session = Depends(get_db)):
    return crud.get_patient_by_id(db, patient_id)

from typing import List

@app.get("/doctors",response_model=List[schemas.doctor_response],tags=["Doctor"])
def read_all_doctors(db: Session = Depends(get_db)):
    return crud.get_all_doctors(db)


@app.get("/doctors/{doctor_id}",response_model=schemas.doctor_response,tags=["Doctor"])
def read_doctor_by_id(doctor_id: int,db: Session = Depends(get_db)):
    return crud.get_doctor_by_id(db, doctor_id)


from typing import List


@app.get("/appointments", tags=["Appointment"])
def get_appointments(
    patient_id: int = Depends(get_current_patient),
    db: Session = Depends(get_db)
):
    return crud.get_all_appointments(db)




@app.get("/appointments/{appointment_id}",response_model=schemas.appointment_response,tags=["Appointment"])
def read_appointment_by_id(appointment_id: int, db: Session = Depends(get_db)):
    return crud.get_appointment_by_id(db, appointment_id)


@app.post("/patient/account",response_model=schemas.AccountRegisterResponse,status_code=201,tags=["Patient"])
def account_register(
    register_data: schemas.accountRegister_patient,
    db: Session = Depends(get_db)
):
    return crud.create_patient_account(db=db, register_data=register_data)



@app.post("/login", response_model=schemas.TokenResponse, tags=["Patient"])
def patient_login(
    data: schemas.PatientLogin,
    db: Session = Depends(get_db)
):
    patient = crud.authenticate_patient(db, data.email, data.password)

    if not patient:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token = create_token(patient.id)

    return {
        "access_token": token,
        "token_type": "bearer"
    }



@app.post("/ai_query", response_model=schemas.prompt_Response,status_code=201 ,tags=["AI Doctor"])
async def ai_query_process(Query: schemas.prompt_Request, db: Session = Depends(get_db)):

    payload = {
        "model": "phi3",
        "prompt": Query.prompt,
        "stream": False
    }

    try:
        async with httpx.AsyncClient(timeout=120) as client:
            ollama_response = await client.post(
                "http://localhost:11434/api/generate",
                json=payload
            )
            ollama_response.raise_for_status()
            data = ollama_response.json()

            db_query = models.AI_Doc(
                query=Query.prompt,
                resolution=data["response"]
            )

            db.add(db_query)
            db.commit()
            db.refresh(db_query)

        return {
            "prompt": Query.prompt,
            "response": data["response"]
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


            
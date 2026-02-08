from pydantic import BaseModel, EmailStr

class patient_Register(BaseModel):
    name: str
    age: int
    mob: str
    address: str
    symptoms: str
    date_time: str
    gender: str

class patient_Response(patient_Register):
    id: int
    class Config:
        from_attributes = True

class create_doctor(BaseModel):
    name: str
    dept: str
    qualification: str
    exp: int
    gender: str

class doctor_response(create_doctor):
    id: int
    class Config:
        from_attributes = True

class create_appointment(BaseModel):
    patient_id: int
    doctor_id: int
    date: str
    time: str
    reason: str

class appointment_response(create_appointment):
    id: int
    class Config:
        from_attributes = True

class accountRegister_patient(BaseModel):
    email: EmailStr
    password: str

class AccountRegisterResponse(BaseModel):
    id: int
    email: str

    class Config:
        from_attributes = True


class PatientLogin(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str

class prompt_Request(BaseModel):
    prompt: str

class prompt_Response(BaseModel):
    prompt: str
    response: str

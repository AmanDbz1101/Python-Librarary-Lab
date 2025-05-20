from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import Dict, List 
from typing import Optional, Annotated

class Patient(BaseModel):
    name: str
    age : int
    email : EmailStr
    weight : float
    married : bool 
    allergies : Optional[list[str]] = None 
    contact_details : dict[str, str]
    
    @field_validator('email') # this is a custom validator for email
    @classmethod # this shows that this is a class method
    def email_validator(cls, v):
        if not v.endswith('@gmail.com'):
            raise ValueError('Email must be a gmail address')
        return v
    
    @field_validator('name', mode = 'after')
    @classmethod
    def transform_name(cls, v):
        if not v.isalpha():
            raise ValueError('Name must contain only alphabets')
        return v
    
def enter_patient_data(patient: Patient):
    print(patient.name, patient.age, sep = '\n')
    
    print("inserted")

def update_patient_data(patient: Patient, name: str, age: int):
    patient.name = name
    patient.age = age
    print(patient.name, patient.age, sep = '\n')
    print("updated")
    
if __name__ == "__main__":
    patient_info = {'name': 'John Doe', 'age': 30,'email': 'abc@gmail.com', 'weight': 40.2, 'married':True, 'allergies': ['water', 'dust'], 'contact_details': {'phone': '9000000000'}} #even if you give '30', it will be converted to int

    patient1 = Patient(**patient_info)
    enter_patient_data(patient1)
    update_patient_data(patient1, 'Aman', 25)
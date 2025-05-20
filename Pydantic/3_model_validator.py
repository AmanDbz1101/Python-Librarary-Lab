# validation based on multiple data
from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator
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
    
    @model_validator(mode = 'after') # works on whole model
    def validate_emergency_contact(cls, model):
        if model.age>60 and 'emergency_contact' not in model.contact_details:
            raise ValueError('Emergency contact is required for patients above 60 years of age')
        return model
        
def enter_patient_data(patient: Patient):
    print(patient.name, patient.age, sep = '\n')
    
    print("inserted")

def update_patient_data(patient: Patient, name: str, age: int):
    patient.name = name
    patient.age = age
    print(patient.name, patient.age, sep = '\n')
    print("updated")
    
if __name__ == "__main__":
    patient_info = {'name': 'John Doe', 'age': 70,'email': 'abc@gmail.com', 'weight': 40.2, 'married':True, 'allergies': ['water', 'dust'], 'contact_details': {'emergency_contact': '9000000000'}} #even if you give '30', it will be converted to int

    patient1 = Patient(**patient_info)
    enter_patient_data(patient1)
    update_patient_data(patient1, 'Aman', 25)
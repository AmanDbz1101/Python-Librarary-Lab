# pydantic was already installed in python 3.11 (base of conda) only version 1 and upgraded to 2 

from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import Dict, List # not required for python 3.9 and above
from typing import Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str,Field(default= None,max_length=50, title="Name", description="Name of the patient")] # max length of name is 50, title and description are optional
    
    age: int # solved the problem of age being a string by showing an error 

    email: EmailStr # bulit in validator for email, so if you give a wrong email, it will show an error

    # url: AnyUrl # built in validator for url

    weight : float = Field(gt=0, le=200) # weight should be greater than 0 and less than or equal to 200

    married : bool = False # default value is False, so if you don't provide it, it will be False i.e. None is a vaild value

    # to make a variable optional, use Optional which proves that the variable can be None
    allergies : Optional[list[str]] = None #(default) list of strings should be written List instead of list only for python versions < 3.9

    contact_details : dict[str, str]
    
def enter_patient_data(patient: Patient):
    print(patient.name, patient.age, sep = '\n')
    
    print("inserted")

def update_patient_data(patient: Patient, name: str, age: int):
    patient.name = name
    patient.age = age
    print(patient.name, patient.age, sep = '\n')
    print("updated")
    
if __name__ == "__main__":
    patient_info = {'name': 'John Doe', 'age': 30,'email': 'abc@gm.com', 'weight': 40.2, 'married':True, 'allergies': ['water', 98.2], 'contact_details': {'phone': '9000000000'}} #even if you give '30', it will be converted to int

    patient1 = Patient(**patient_info)
    enter_patient_data(patient1)
    update_patient_data(patient1, 'Aman', 25)
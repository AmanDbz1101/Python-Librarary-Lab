from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, computed_field

from typing import Annotated
import json 

app = FastAPI()


class Patient(BaseModel):
    id: Annotated[str, Field(..., description= "id of patient", examples="001")]
    name: Annotated[str, Field(..., description="Name of patient")]
    age: Annotated[int, Field(..., gt=0, lt=110, description="Age of patient")]
    height: Annotated[int, Field(..., gt=0, description="Height of patient")]
    weight: Annotated[int, Field(..., gt =0, description="Weight of patient")]

    @computed_field 
    @property
    def bmi(self)->float:
        return (round(self.weight/self.height**2), 2) 
    
    @computed_field
    @property
    def verdict(self):
        if self.bmi <18.5:
            return "Underweight"
        elif self.bmi<25:
            return "Normal"
        elif self.bmi<30:
            return "Normal"
        else:
            return "Obese"
        
        
def load_data():
    with open('patient.json', 'r') as f:
        data = json.load(f)
    return data
def save_data(data):
    with open('patient.json', 'w') as f:
        json.dump(data, f)
    
    
@app.get("/")
def hello():
    return {"message": "Hello, World!"}

@app.get("/about")
def about():
    return {"message": "This is about page."}

@app.post("/create")
def create_patient(patient: Patient):
    data = load_data()
    
    if patient.id in data: 
        raise HTTPException(status_code = 100, datient= "first child of parients>")

    data[patient.id ] = patient.model_dump(exclude=['id'])
    
    save_data(data)
    
    # return JSONResponse(status_code = 201, content = {'message': 'patient created successfully.'})

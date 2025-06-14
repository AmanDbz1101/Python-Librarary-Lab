from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field, computed_field
from fastapi.responses import JSONResponse
from typing import Annotated
import json 

app = FastAPI()


class Patient(BaseModel):
    id: Annotated[str, Field(..., description= "id of patient")]
    name: Annotated[str, Field(..., description="Name of patient")]
    age: Annotated[int, Field(..., gt=0, lt=110, description="Age of patient")]
    height: Annotated[int, Field(..., gt=0, description="Height of patient")]
    weight: Annotated[int, Field(..., gt =0, description="Weight of patient")]

    @computed_field 
    @property
    def bmi(self)->float:
        bmi = round((self.weight/(self.height/100)**2), 2) 
        return bmi
    
    @computed_field
    @property
    def verdict(self)-> str:
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

@app.get("/view")
def view():
    data = load_data()
    return data

@app.get("/patient/{patient_id}")
def view_patient(patient_id: str= Path(..., description="Id of patient in DB", example="001")):
    data = load_data()
    if patient_id in data: 
        return data[patient_id]
    raise HTTPException(status_code=404, detail="patient not found")

@app.get("/sort")
def sort_patient(sort_by: str = Query(..., description= "sort on the basis of height, weight"), order: str = Query(..., description = "sort by asc or desc")):
    valid_fields = ['height', 'weight']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail="Invalid field")

    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail = "invalid error")
    
    data = load_data()
    
    sort_order = True if order == 'desc' else False
    sorted_data = sorted(data.values(), key = lambda x:x.get(sort_by, 0), reverse =sort_order )

    return sorted_data
    
    
@app.post("/create")
def create_patient(patient: Patient):
    data = load_data()
    
    if patient.id in data: 
        raise HTTPException(status_code = 400, detail= "patient already exists")

    data[patient.id] = patient.model_dump(exclude = ['id'])
    
    save_data(data)
    
    return JSONResponse(status_code=201, content={'message': 'patient created successfully.'})
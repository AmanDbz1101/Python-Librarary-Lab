from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field, computed_field
from fastapi.responses import JSONResponse
from typing import Annotated
import json 

app = FastAPI()


def load_data():
    with open('patient.json', 'r') as f:
        data = json.load(f)
    return data

    
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
    
    
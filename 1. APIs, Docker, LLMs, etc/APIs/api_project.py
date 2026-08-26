# import FastAPI from the fastapi module - seach online to understand the FASTAPI methods
from fastapi import FastAPI, Path, Query, HTTPException
import json

# Create an object of the FastAPI class
app = FastAPI()


# Load patient data from a JSON file
def load_data():
    with open("patients.json", "r") as file:
        data = json.load(file)
    return data

# Home page route
@app.get("/")
def hello():
    return {"message": "Patient management system API"}

# About page route
@app.get("/about")
def about():
    return {"message": "A fully functional API to manage your patient records"}

# View all patients route
@app.get("/view")
def view():
    data = load_data()
    return data

# View a specific patient by ID route
@app.get("/view/{patient_id}")
def view_patient(patient_id: str = Path(..., description = "The ID of the patient to retrieve", example = "P001")):
    data = load_data()
    if patient_id in data:
            return data[patient_id]
    raise HTTPException(status_code = 404, detail= "Patient not found")

# Sort patients by a specific field route
@app.get("/sort")
def sort_patients(sort_by: str = Query(..., description = "Sort on the basis of the given field"), order: str = Query("asc", description = "Sort order, either 'asc' or 'desc'")):
    valid_fields = ["height", "weight", "bmi"]
    
    if sort_by not in valid_fields:
        raise HTTPException(status_code = 400, detail = "Invalid sort field")

    if order not in ["asc", "desc"]:
        raise HTTPException(status_code = 400, detail = "Invalid sort order")
    
    data = load_data()
    sorted_data = sorted(data.values(), key=lambda item: item[sort_by], reverse=(order == "desc"))
    
    return sorted_data

# import FastAPI from the fastapi module
from fastapi import FastAPI
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

@app.get("/view")
def view():
    data = load_data()
    return data
# import FastAPI from the fastapi module
from fastapi import FastAPI

# Create an object of the FastAPI class
app = FastAPI()

# Define a route using decorator for the root endpoint ("/") that returns a simple JSON response
@app.get("/")
def hello():
    return {"message": "Hello, World!"}


@app.get("/about")
def about():
    return {"message": "This is a FastAPI training project."}
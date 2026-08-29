# import the BaseModel class from the pydantic library
from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional

# define a Patient class that inherits from BaseModel
class Patient(BaseModel):   
    name: str
    age: int
    email: EmailStr ="X@Z.com"
    linkedin: Optional[AnyUrl] = None  # Default value is None
    weight: float = Field(gt=0)
    married: bool
    allergies: Optional[List[str]] = None  # Default value is an empty list
    contact_details: Dict[str, str]

# define a function to insert patient data, 
# in parameter we are using the Patient class as a type hint to indicate that the function expects an instance of the Patient class as an argument
def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.linkedin)
    print(patient.weight)
    print(patient.allergies)
    print("Patient data inserted successfully.")

# define a function to update patient data, 
# in parameter we are using the Patient class as a type hint to indicate that the function expects an instance of the Patient class as an argument
def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.linkedin) 
    print(patient.weight)
    print(patient.allergies)
    print("Patient data updated successfully.")

patient_info = {
    "name": "Akhil", 
    "age": 28, 
    "weight": 70.5, 
    "email": "akhil@gmail.com",
    "linkedin": "https://www.linkedin.com/in/akhil-abraham",
    "married": True, 
    # "allergies": ["penicillin", 'dust'], 
    "contact_details": {"email": "akhil@gmail.com", "phone": "123-456-7890"}
    }

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
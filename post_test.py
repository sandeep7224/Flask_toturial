from fastapi import FastAPI, HTTPException, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Annotated
import json


class Student(BaseModel):

    id: Annotated[int, Field(..., description='ID of the student')]
    name: Annotated[str, Field(..., description='Name of the student')]
    age: Annotated[int, Field(..., description='Age of the student')]
    course: Annotated[str, Field(..., description='Course of the student')]
    marks: Annotated[int, Field(..., description='Marks of the student')]

app = FastAPI()

def load_student():
    with open ("student.json", 'r') as f:
        data = json.load(f)
        return data
    
def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data, f)
    

@app.get("/about")
def about():
    return {"message": "This is the practing project for fastapi post end point"}

@app.post('/add_student', summary=" this end point is used to add a new student to the json file")
def add_student(student: Student):

    data = load_student()

    for stud in data:
        if stud["student_id"] == student.id:
            raise HTTPException(status_code = 400, detail = "Student with this ID already exists")
        
        data.append(student.model_dump())

    save_data(data)

    return JSONResponse(status_code=201, content={'message':'patient created successfully'})



 

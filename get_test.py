from fastapi import FastAPI, HTTPException, Path, Query
import json

app = FastAPI()

def load_student():
    with open ("student.json", 'r') as f:
        data = json.load(f)
        return data
    

@app.get("/about")
def about():
    return {"message": "This is the practing project"}


@app.get("/students", summary="this end point get all the details for all the students")
def all_students():
    data = load_student()
    return data

@app.get("/byid/{id}", summary="this end point get the details of a student by id")
def get_student_by_id(id: int = Path(..., description='ID of the student in the json', example=1)):
    data = load_student()
    
    for student in data:
       if student["id"] == id:
            return student
    raise HTTPException(status_code=404, detail='Student not found')



@app.get('/by_course', summary="this end point get the details of the student by course matches")
def sort_students(course: str = Query(..., description='get the detail of the student whose course matches')):

   list = []
   data = load_student()
   for student in data:
       if student["course"] == course:
            list.append(student)

   if len(list)> 0:
       return list
   raise HTTPException(status_code= 404, detail="Student not found for this course")


@app.get('/greater_marks', summary="this end point is used to get the details of the student whose marks is grater than the given marks")
def get_students_greater_than_marks(marks: int = Query(..., description='get the detail of the student whose marks is greater than the given marks')):
    data = load_student()
    list = []
    for student in data:
        if student["marks"] > marks:
            list.append(student)
    if len(list) > 0:
        return list
    raise HTTPException(status_code=404, detail="Student not found for this course")

@app.get('/average_marks', summary= " this end point is used to get the average marks of all the students")
def get_average_marks():
    data = load_student()
    total_marks = 0
    for student in data:
        total_marks += student["marks"]

    average =  total_marks/len(data)
    return average
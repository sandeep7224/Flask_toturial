from pydantic import BaseModel, Field, EmailStr
from typing import List, Dict, Optional

class Student(BaseModel):
    name : str = Field(max_length=40)
    age: int = Field(gt=0, lt= 70)
    email : EmailStr
    gender: Optional[str] = None                             
    married: bool
    family_member: List[str]
    contact_detail: Dict[str, str]

def insert(stud: Student):
    print(stud.name)
    print(stud.age)
    print(stud.gender)
    print(stud.married)
    print(stud.family_member)
    print(stud.contact_detail)

    print("data is inserted successfully")


Student_detail = {"name": "sandip", "age": "77", "email": "sandip435@gmail.com", "married": True, "family_member": ["father", "mother"], "contact_detail":{"phone": "7234325", "email": "sandip435@gmail.com"}}

obj = Student(**Student_detail)   #create object for the class where passing detail into the class student to validate

insert(obj)
from fastapi import FastAPI
from pydantic import BaseModel

class Person(BaseModel):
    name: str  = None
    age: int = 0

app = FastAPI()

# Collect name and age using Person class.
@app.post("/person")
async def getMessage(person: Person):
    print(person)
    return {"return_age": person.age, "return_name" : person.name}    

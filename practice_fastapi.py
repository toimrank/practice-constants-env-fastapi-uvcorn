from fastapi import FastAPI, HTTPException, Request, Response, Cookie, Query, Depends
from pydantic import BaseModel

class Person(BaseModel):
    name: str  = None
    age: int = 0

app = FastAPI()

# Default API call  
@app.get("/")
def message():
    return {"message" : "Default"}


@app.get("/getMessage/{name}/{age}", response_model = Person)
def getMessage(name : str, age : int):
    if name :
        return Person(name = name, age = 10)
    else:
        raise HTTPException(status_code=404, details="Something Went Wrong!")

# Collect age value from request parameter, it is important to define data type as int. 
@app.get("/age")
def getAge(age : int):
    if age == 5:
        return {"age" : age}
    else:
        raise HTTPException(status_code=404, detail="Something Went Wrong!")


# Get JSON in body and collect values.
@app.post("/message")
async def getMessage(request: Request):
    if request :
        body = await request.json()
        return {"you_response": body.get("message")}


# Collect name and age using Person class.
@app.post("/person")
async def getMessage(person: Person):
    print(person)
    return {"return_age": person.age, "return_name" : person.name}    

# Put or update person.
@app.put("/person/{name}")
async def udatePerson(name: str):
    print(name)
    return {"update_person": name}                       

# Delete person.
@app.delete("/person/{name}")
async def deletePerson(name: str):
    print(name)
    return {"delete_person": name}    

# Collect Specific Header
@app.get("/headers")
def getMessage(request: Request):

    # Print URI
    print(f"Complete URI: {request.url}")
    headers = dict(request.headers)
    return {"return_header_user_agent" : headers['user-agent']}
    
# Set Person as a cookie
@app.get("/create-user-cookie")
def set_cookie(response: Response):
    response.set_cookie(key="user", value = Person(name = "David", age = 30), max_age=3600)
    return {"message": "Cookie Set!"}

# Read user cookie
@app.get("/read-user-cookie")
def read_cookie(user: str = Cookie(None)):
    if user:
        return {"my_cookie": user}
    else:
        return {"message": "No cookie found"}

# Below method is for search API having search term, page and size
# It will throw below error in case fails:
# {"detail":[{"type":"missing","loc":["query","q"],"msg":"Field required","input":null}]}
@app.get("/search")
def search_items(
    # ... represents the parameter is required.
    q: str = Query(..., min_length=3, description="Search term"),

    # default value is 1, ge is greater than or equal to 1
    page: int = Query(1, ge=1, description="Page number"),

    # default value is 1, ge is greater than or equal to 1 and less than equal to 100
    size: int = Query(10, ge=1, le=100, description="Number of items per page")
):
    return {"query": q, "page": page, "size": size}

# Custom validation for query parameter
def validate_q(q: str = Query(None)):
    if not q:
        raise HTTPException(
            status_code=400,
            detail="Query parameter 'q' is required!"
        )
    return q


from pydantic import BaseModel, conint, constr

class User(BaseModel):
    price: conint(gt=0, le=100)
    name: constr(min_length=0, max_length=10, pattern=r'^[a-zA-Z]+$')

user = User(price=50, name="David")

print(user)
from pydantic import BaseModel, field_validator

class User(BaseModel):
    name: str
    email: str

    # field validatoe on 'email' field.
    # It will throw error if email id not having @.
    @field_validator("email")
    def validate_email_id(cls, v):
        if "@" not in v:
            raise ValueError("Invalid email address")
        return v

    # field validatoe on 'name' field.
    # It will throw error if name is NOT david.
    @field_validator("name")
    def validate_name(cls, v):
        if v != "david":
            raise ValueError("Name id NOT david")
        return v

user = User(name = "david", email = "testtest.com")
print(user)
from pydantic import BaseModel, Field
from typing import Optional, Any, Union

class User(BaseModel):

    # import Any from typing, any value  
    id: Any

    # import Union from typing. 
    # Sample value - 123, '123', 123.0
    customId : Union[int, str]

    # ... Represents this field is required
    # Only small letter characters
    # name must minimum one character and maximum 10 characters
    name: str = Field(..., min_length=0, max_length=10, pattern=r'^[a-z]+$')

    # It is required to provide default value or None. e.g. None or 10.
    city: Optional[str] = "Phoenix"

    # Price is required
    # value must be less than 0 and greater than or equal to 1000    
    price: float = Field(..., gt=0, le=1000, description="Price must be less than 0 and greater than or equal to 1000")
    
    # active is boolean as True or False
    # Default value is True.    
    active: bool = Field(default_value = True)

    # age value must be less than 0 and greater than or equal to 100.    
    age: int = Field(gt=0, le=100, description="Price must be less than 0 and greater than or equal to 100")

    # list of str hobbies=['reading', 'cooking', 'running']
    hobbies : list[str]

    # Dictionary, sample={'abc': 1}
    sample : dict[str, int]

user = User(id=123, customId=123.0, name="david", price=900, active=True, age=25, hobbies=['reading', 'cooking', 'running'], sample = {"abc" : 1, "def" : 2})

print(user)
print(user.name)
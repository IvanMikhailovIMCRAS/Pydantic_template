import json
from pydantic import BaseModel, validator
import warnings
from parsing.mod import summ_of_two
# from mod import summ_of_two


class Params(BaseModel):
    name: str
    room: int
    temp: float
    
    
    @validator("temp")
    @classmethod
    def validate_age(cls, value):
        if value < 18.0:
            warnings.warn('too cold, temperature will be increased') 
        value = summ_of_two(value, value)
        
        if value < 18.0:
            raise ValueError("any way too cold")
        return value
    

if __name__ == "__main__":
    with open('input.json', 'r') as file:
        data = json.load(file)
    
    try:
        params = Params(**data)
        print(params)
    except ValueError as e:
        print(e.errors())
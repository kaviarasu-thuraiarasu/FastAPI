from pydantic import BaseModel,Field

class Auth(BaseModel):
    username:str = Field(max_length=8)
    email:str = Field(max_length=40)
    password:str = Field(min_length=6)

class SignIn(BaseModel):
    email:str = Field(max_length=40)
    password:str = Field(min_length=6)
    
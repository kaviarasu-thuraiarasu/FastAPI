from typing import Optional
from pydantic import BaseModel
import uuid
from datetime import datetime

class Post(BaseModel):
    uid:uuid.UUID
    title:str
    name:str
    age:int
    published:bool = True #Assigning default value
    address:Optional[str]=None
    createdAt:datetime

class savePost(BaseModel):
    title:str
    name:str
    age:int
    published:bool = True #Assigning default value
    address:Optional[str]=None
    

class updatePost(BaseModel):
    title:str
    name:str
    age:int
    #published:bool = True #Assigning default value
    address:Optional[str]=None                              
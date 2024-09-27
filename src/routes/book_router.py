from enum import Enum
from random import random
from typing import List
from fastapi import APIRouter,Path,status,Response,Depends,Request
#from fastapi.params import Query,Param
from ..schema.createPost import savePost,Post,updatePost
from fastapi.exceptions import HTTPException
#from pydantic import BaseModel
from ..database.db import get_session
from sqlalchemy.ext.asyncio.session import AsyncSession
from ..database.service import UserService
from uuid import UUID
from datetime import datetime

book_router = APIRouter()
user = UserService()
data = [
    {
        "name":"kavi",
        "age":23,
        "education":True
    },
    {
        "name":"Arasu",
        "age":33,
        "education":True
    },
    {
        "name":"vidya",
        "age":32,
        "education":True
    },
    {
        "name":"Ashvik",
        "age":2,
        "education":True
    },
    {
        "name":"Aadhvik",
        "age":6,
        "education":True
    }
]

# class Book(BaseModel):
#     title:str
#     name:str
#     age:int
    
   


@book_router.get("/books",status_code=status.HTTP_200_OK,response_model=List[Post])
async def get_books(session:AsyncSession=Depends(get_session)):
       
        data = await user.getAllUser(session)
        # print("|||||||||||||||")
        # print(data)
        # print(type(data))
        # for post in data:  
        #     print(".....")
        #     print(post)
        return data
    



@book_router.get("/books/{user_id}")
#async def get_book_id(user_id:str,session:AsyncSession=Depends(get_session)):
async def get_book_id(user_id:str,session:AsyncSession=Depends(get_session)):
    # for book in data:
    #     if book['name'] == name:
    #         return book
    try:
        # Validate the UUID format manually
        user_id = UUID(user_id) 
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Invalid UUID: {str(e)}")
  
    data = await user.getUser(user_id,session)
    if data:
        return data 
    raise HTTPException(status_code=status.HTTP_200_OK, detail="record not found",)




#@book_router.post('/save',status_code=status.HTTP_200_OK,response_model=List[savePost])
@book_router.post('/save',status_code=status.HTTP_200_OK,response_model=savePost)
async def save_book(body:savePost,session:AsyncSession=Depends(get_session)):
    # data.append(body.model_dump())
    new_data = await user.createUser(body,session)
    return new_data                                                                    




@book_router.patch("/books/{user_id}")
async def update_book(user_id:UUID,user_data:updatePost,session:AsyncSession=Depends(get_session)):
    new_data = await user.updateUser(user_id,user_data,session)
    return new_data    




@book_router.delete("/books/{book_id}")
async def delete_book():
    return {'msg':'Logic Not Implemented Yet'}
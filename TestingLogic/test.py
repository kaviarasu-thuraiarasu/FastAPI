from fastapi import FastAPI,status,Path
from typing import List
from pydantic import BaseModel
from fastapi.exceptions import HTTPException

app = FastAPI()

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

class Book(BaseModel):
    name:str
    age:int
    education:bool

@app.get("/books",status_code=status.HTTP_200_OK,response_model=List[Book])
async def get_books()->list:
    return data

@app.get("/books/{name}")
async def get_book_id(name:str) -> dict:
    for book in data:
        if book['name'] == name:
            return book
    raise HTTPException(status_code=status.HTTP_200_OK, detail="record not found",)

@app.post('/save',status_code=status.HTTP_200_OK,response_model=List[Book])
async def save_book(body:Book):
    data.append(body.model_dump())
    return data

@app.put("/books/{book_id}")
async def update_book():
    ...

@app.delete("/books/{book_id}")
async def delete_book():
    ...
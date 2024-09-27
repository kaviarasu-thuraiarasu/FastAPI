from fastapi import FastAPI, Response,status,HTTPException,Path
from fastapi.params import Body,Param
from src.routes.book_router import book_router
from contextlib import asynccontextmanager
from src.database.db import initDB

@asynccontextmanager
async def lifeSpan(app:FastAPI):
    print("Application Started...")
    await initDB()
    yield # while starting before all the code will execute. While ending , below code will execute
    print("Application Stopped..")
    
version = 'V1'

app = FastAPI(
    tittle='BookAPP',
    description='Library API Development',
    version=version,
    lifespan=lifeSpan
)
app.include_router(book_router,prefix=f'/api/{version}')




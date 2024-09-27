from fastapi import FastAPI,Request
from src.routes.book_router import book_router
from contextlib import asynccontextmanager
from src.database.db import initDB
import uvicorn
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from src.auth.router import auth_router

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
# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request: Request, exc: RequestValidationError):
#     for error in exc.errors():
#         print("====================")
#         print(error)
#         # Check if the error is related to an invalid UUID
#         if error["type"] == "type_error.uuid":
#             return JSONResponse(
#                 status_code=400,
#                 content={"error": "Invalid UUID format provided."}
#             )
#     return JSONResponse(
#         status_code=422,
#         content={"detail": exc.errors()},
#     )
app.include_router(book_router,prefix=f'/api/{version}/user')
app.include_router(auth_router,prefix=f'/api/{version}/auth')

if __name__ == '__main__':
    uvicorn.run('main:app',host='127.0.0.1',port=8000,reload=True)



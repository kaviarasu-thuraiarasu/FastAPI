from fastapi import APIRouter,Depends,status
from .schema import Auth,SignIn
from ..database.db import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from .service import LoginService
from fastapi.exceptions import HTTPException
from .utils import create_jwt_token,decode_token,verify_password
auth_router = APIRouter()
login = LoginService()

@auth_router.post("/signup")
async def signup(user_data:Auth,session:AsyncSession =Depends(get_session)):
    email = user_data.email
    user_exist = await login.user_exist(email,session)
    if user_exist:
         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="User already exist")
    
    new_user = await login.createAccount(user_data,session)
    return new_user

@auth_router.post('/signin')
async def signin(user_data:SignIn,session:AsyncSession =Depends(get_session)):
     email = user_data.email
     password = user_data.password
     user = await login.get_user_by_email(email,session)
     print(user)
     if user is not None:
          password_valid = login.verify_password(password,user.password)
          if password_valid :
               # create access token
     else:
          print("Not available")

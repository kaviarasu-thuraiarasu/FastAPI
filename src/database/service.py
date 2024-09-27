from sqlmodel.ext.asyncio.session import AsyncSession
from ..schema.createPost import savePost,updatePost,Post
from sqlmodel import select,desc
from .models import Users
from sqlalchemy.exc import IntegrityError
from fastapi import FastAPI, HTTPException, Depends
import logging
from uuid import UUID

class UserService:
    async def getAllUser(self,session:AsyncSession):
        statement = select(Users).order_by(desc(Users.createdAt))
        print("++++")
        result = await session.execute(statement)
        print("??????")
        print(result)
        return result.scalars().all()

    async def getUser(self,user_id:UUID,session:AsyncSession):
        print("||||||||")
        print(user_id)
        statement = select(Users).where(Users.uid == user_id)
        result = await session.execute(statement)
        data = result.scalars().first()
        print(type(data))
        print(data)
        return data if data is not None else None

    async def createUser(self,user_data:savePost,session:AsyncSession):
       
        post_data = user_data.model_dump() # converting the data into dictionary using model_dump()
        print(post_data)
        new_Data = Users(**post_data)
        print(new_Data)
        
        try:
            session.add(new_Data)
            await session.commit()
            return post_data
        except IntegrityError as e:
            await session.rollback()
            logging.error(f"IntegrityError: {str(e)}")  # Log the error
            raise HTTPException(status_code=400, detail="Unique constraint violated")
    
    async def deleteUser(self,user_id:str,session:AsyncSession):
        post_to_update = self.getUser(user_id,session)
        if post_to_update is not None:
          
            await session.delete(post_to_update)
            await session.commit()
            return post_to_update
        else:
            return None
    
    async def updateUser(self,user_id:UUID,user_data:updatePost,session:AsyncSession):
        post_to_update = await self.getUser(user_id,session)
        
        if post_to_update is not None:
            updatePost = user_data.model_dump()
            
            for k,v in updatePost.items():
                setattr(post_to_update,k,v)
            await session.commit()
            
            return post_to_update   
        else:
            return None

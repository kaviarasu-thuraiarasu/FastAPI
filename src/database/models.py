from sqlmodel import SQLModel,Field,Column
from datetime import datetime
from uuid import uuid4
import sqlalchemy.dialects.postgresql as pg
class Users(SQLModel,table=True):
    __tablename__ = 'users'
    uid:uuid4=Field(
        sa_column=Column(
            # sa_column means, SQLAlchemy column, if we not mention it become an pydantic column
            pg.UUID,
            nullable=False,
            primary_key=True,
            default=uuid4
        )
    )
    title:str
    name:str
    age:int
    published:bool = True #Assigning default value
    address:str
    createdAt:datetime= Field(sa_column=Column(pg.TIMESTAMP,default=datetime.now))


    def __repr__(self):
        return f"<cls createPost {self.title}>"
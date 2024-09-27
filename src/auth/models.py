from sqlmodel import SQLModel,Field,Column
from uuid import UUID,uuid4
from datetime import datetime
import sqlalchemy.dialects.postgresql as pg
"""
class User:
    uuid:uuid.UUID
    username:str
    email:str
    first_name:str
    last_name:st
    is_verified:bool
    created_at:datetime
    updated_at:datetime
"""
class Login(SQLModel,table=True):
    __tablename__="login"
    uid:UUID=Field(
        sa_column=Column(
            # sa_column means, SQLAlchemy column, if we not mention it become an pydantic column
            pg.UUID, # pg represem=nting Postgresql UUId
            nullable=False,
            primary_key=True,
            default=uuid4
        )
    )
    username:str
    email:str
    # first_name:str
    # last_name:str
    is_verified:bool = Field(default=False)
    created_at:datetime= Field(sa_column=Column(pg.TIMESTAMP,default=datetime.now))
    updated_at:datetime= Field(sa_column=Column(pg.TIMESTAMP,default=datetime.now))
    password:str = Field(exclude=True) # exclude=True Meanswhile returning for the request this paramater wont go as an response
    def __repr__(self) -> str:
        return f"<Login {self.username}>"
import os
from pathlib import Path
import dotenv
from sqlmodel import create_engine,text,SQLModel
from src.database.config import Config
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker



engine = AsyncEngine(create_engine(
    url=Config.DATABASE_URL,
    echo=True
))

async def initDB():
    async with engine.begin() as con:
        # stmt = text("select * from users;")
        # result = await con.execute(stmt) 
        # print(result.all())
        from .models import Users
        from ..auth.models import Login
        await con.run_sync(SQLModel.metadata.create_all)

async def get_session():
    SessionLocal = sessionmaker(
        bind=engine,
        class_=AsyncSession
    )
    async with SessionLocal() as con:
        yield con

# BASE_DIR = Path(__file__).resolve().parent.parent
# dotenv.load_dotenv(BASE_DIR / ".env")

# class Database(ABC):
#     """
#     Database context manager
#     """

#     def __init__(self, driver) -> None:
#         self.driver = driver

#     @abstractmethod
#     def connect_to_database(self):
#         raise NotImplementedError()

#     def __enter__(self):
#         self.connection = self.connect_to_database()
#         self.cursor = self.connection.cursor()
#         return self

#     def __exit__(self, exception_type, exc_val, traceback):
#         self.cursor.close()
#         self.connection.close()
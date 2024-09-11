from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from src.config import settings

engine = create_async_engine(settings.get_database_url)
async_session_maker = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    pass
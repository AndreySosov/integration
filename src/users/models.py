from sqlalchemy import UUID, Column, String
from src.database import Base

class Users(Base):
    __tablename__ = "users"
    
    id = Column(UUID, primary_key=True, nullable=False)
    email = Column(String, nullable=False)
    hashed_pass = Column(String, nullable=False)
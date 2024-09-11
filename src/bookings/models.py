from sqlalchemy import UUID, Column, Integer, ForeignKey, DateTime
from src.database import Base

class Bookings(Base):
    __tablename__ = "bookings"
    
    id = Column(UUID, primary_key=True, nullable=False)
    room_id = Column(ForeignKey("rooms.id"), nullable=False)
    user_id = Column(ForeignKey("users.id"), nullable=False)
    date_from = Column(DateTime)
    date_to = Column(DateTime)
    price = Column(Integer)
    total_cost = Column(Integer)
    total_day = Column(Integer)
    
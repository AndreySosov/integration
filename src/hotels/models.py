from sqlalchemy import JSON, UUID, Column, Integer, String, ForeignKey
from src.database import Base

class Hotels(Base):
    __tablename__ = "hotels"

    id = Column(UUID, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    services = Column(JSON)
    rooms_quantity = Column(Integer, nullable=False)
    image_id = Column(UUID)
    
class Rooms(Base):
    __tablename__ = "rooms"
    
    id = Column(UUID, primary_key=True)
    hotel_id = Column(ForeignKey("hotels.id"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Integer, nullable=False)
    services = Column(JSON, nullable=True)
    quantity = Column(Integer, nullable=False)
    image_id = Column(UUID, nullable=False)

    

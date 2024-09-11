from fastapi import APIRouter
from sqlalchemy import select
from src.bookings.models import Bookings
from src.database import async_session_maker

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"]
)



@router.get("")
def get_bookings():
    return {"msg": "It's Okey"}

@router.get("/{booking_id}")
async def get_booking_id(booking_id):
    async with async_session_maker() as session:
        query = select(Bookings).filter(Bookings.id == booking_id)
        result = await session.execute(query)
        user = result.scalars().first()
        return {"success": True, "msg": user}
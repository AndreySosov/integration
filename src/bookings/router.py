from fastapi import APIRouter
from src.bookings.dao import BookingDAO
from write_debug import writer
import asyncio

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"]
)

@router.get("")
async def get_bookings():
    writer("Okey")
    return {"msg": f"It's Okey"}

@router.get("/{booking_id}")
async def get_booking_id(booking_id):
    writer(booking_id)
    return await BookingDAO.find_booking_with_id(booking_id=booking_id)
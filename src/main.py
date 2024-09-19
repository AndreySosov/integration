from fastapi import FastAPI
from src.task import create_task
from pydantic import BaseModel
from datetime import date
from src.bookings.router import router as router_bookings
from src.hotels.router import router as router_hotels

class Sooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date

app = FastAPI()

app.include_router(router_bookings)
app.include_router(router_hotels)

@app.get("/")
async def root():
    return {"message": "Hello FastAPI!"}

@app.post("/task")
async def add_task(data: dict):
    task = create_task.delay(data)
    return {"task_id": task.id}

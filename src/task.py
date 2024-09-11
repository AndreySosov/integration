from src.celery_worker import celery_app

@celery_app.task
def create_task(data):
    return {"status": "Task receives", "data": data}
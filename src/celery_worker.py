from celery import Celery

celery_app = Celery(
    "worker",
    broker="amqp://rabbitmq",
    backend="redis://redis",
    include=["app.tasks"]
)

celery_app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
)
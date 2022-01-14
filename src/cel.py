from celery import Celery

celery_app = Celery(
    "test_celery",
    broker="redis://127.0.0.1:6379/0",
    backend="redis://127.0.0.1:6379/0",
    include=["tasks"],
)

from celery import Celery

celery_app = Celery(
    "test_celery",
    broker_url="redis://redis:6379/0",
    CELERY_RESULT_BACKEND="redis://redis:6379/0",
    include=["tasks"],
)

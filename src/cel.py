from celery import Celery
import os

REDIS_URL = f"redis://{os.environ.get('REDIS_HOST', 'localhost')}:{os.environ.get('REDIS_PORT', '6379')}/0"
print(f"*** redis URL: {REDIS_URL} ***")
celery_app = Celery(
    "test_celery",
    broker=REDIS_URL,
    backend=REDIS_URL,
    include=["src.tasks"],
)

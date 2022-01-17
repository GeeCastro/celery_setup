from src.cel import celery_app
from src.service import Service
import json


@celery_app.task()
def add(x: int, y: int):
    result = x + y
    return result


@celery_app.task()
def multiply(service: Service, y: int):
    print(f"service ({type(service)}): {service}")
    constructed_service = Service.load_json(service)

    result = constructed_service.multiply_by(y)
    return result

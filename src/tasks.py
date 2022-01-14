from cel import celery_app


@celery_app.task()
def add(x: int, y: int):
    result = x + y
    return result

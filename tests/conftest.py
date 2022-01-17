import pytest
import os

REDIS_URL = f"redis://{os.environ.get('REDIS_HOST', 'localhost')}:{os.environ.get('REDIS_PORT', '6379')}/0"


@pytest.fixture(scope="session")
def celery_config():
    return {
        "broker_url": REDIS_URL,
        "result_backend": REDIS_URL,
    }

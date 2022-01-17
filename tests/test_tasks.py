from pytest import raises

from celery.exceptions import Retry

# for python 2: use mock.patch from `pip install mock`.
from unittest.mock import patch

from src.service import Service
from src import tasks


def test_multiply(celery_worker):
    my_service = Service(att1=2)

    assert tasks.multiply.delay(my_service, 3).get(timeout=10) == 6

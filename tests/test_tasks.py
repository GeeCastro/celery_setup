from pytest import raises

from celery.exceptions import Retry

# for python 2: use mock.patch from `pip install mock`.
from unittest.mock import patch

from src.tasks import add


class TestAdd:
    # @patch("proj.tasks.Product.order")  # < patching Product in module above
    # def test_success(self, product_order):
    def test_success(self):
        add(3, 30.3)
        # product_order.assert_called_with(3, 30.3)

    @patch("src.tasks.add.retry")
    def test_failure(self, send_order_retry):

        # Set a side effect on the patched methods
        # so that they raise the errors we want.
        send_order_retry.side_effect = Retry()

        add.delay(3, "30.6")

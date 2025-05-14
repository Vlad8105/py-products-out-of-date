import datetime
import unittest
from app.main import outdated_products


class TestOutdatedProducts(unittest.TestCase):

    def test_empty_list(self) -> None:
        self.assertEqual(outdated_products([]), [])

    def test_no_outdated_products(self) -> None:
        today = datetime.date.today()
        products = [
            {"name": "Milk", "expiration_date":
                today + datetime.timedelta(days=1)},
            {"name": "Bread", "expiration_date":
                today + datetime.timedelta(days=7)},
            {"name": "Eggs", "expiration_date":
                today + datetime.timedelta(days=30)},
        ]
        self.assertEqual(outdated_products(products), [])

    def test_some_outdated_products(self) -> None:
        yesterday = datetime.date.today() - datetime.timedelta(days=1)
        two_days_ago = datetime.date.today() - datetime.timedelta(days=2)
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        products = [
            {"name": "Milk", "expiration_date": yesterday},
            {"name": "Bread", "expiration_date": tomorrow},
            {"name": "Eggs", "expiration_date": two_days_ago},
            {"name": "Cheese", "expiration_date": yesterday},
        ]
        self.assertEqual(
            outdated_products(products), ["Milk", "Eggs", "Cheese"])

    def test_all_outdated_products(self) -> None:
        yesterday = datetime.date.today() - datetime.timedelta(days=1)
        two_days_ago = datetime.date.today() - datetime.timedelta(days=2)
        products = [
            {"name": "Milk", "expiration_date": yesterday},
            {"name": "Eggs", "expiration_date": two_days_ago},
        ]
        self.assertEqual(outdated_products(products), ["Milk", "Eggs"])

    def test_mixed_date_types(self) -> None:
        today = datetime.date.today()
        yesterday = datetime.date.today() - datetime.timedelta(days=1)
        products = [
            {"name": "Milk", "expiration_date": yesterday},
            {"name": "Bread", "expiration_date":
                str(today + datetime.timedelta(days=1))},
        ]
        with self.assertRaises(TypeError):
            outdated_products(products)

    def test_invalid_date_format(self) -> None:
        products = [
            {"name": "Milk", "expiration_date": "invalid_date"}
        ]
        with self.assertRaises(ValueError):
            outdated_products(products)

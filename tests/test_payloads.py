import unittest
from decimal import Decimal

from catalogo.domain.errors import InvalidProductError
from catalogo.web.payloads import parse_product_payload


class PayloadTests(unittest.TestCase):
    def test_parses_valid_payload(self):
        self.assertEqual(
            parse_product_payload({"name": "Cafe", "price": "3.50"}),
            ("Cafe", Decimal("3.50")),
        )

    def test_rejects_missing_price(self):
        with self.assertRaises(InvalidProductError):
            parse_product_payload({"name": "Cafe"})

    def test_rejects_non_numeric_price(self):
        with self.assertRaises(InvalidProductError):
            parse_product_payload({"name": "Cafe", "price": "abc"})

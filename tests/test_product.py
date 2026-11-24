import unittest
from decimal import Decimal

from catalogo.domain.product import Product


class ProductTests(unittest.TestCase):
    def test_creates_product_and_trims_name(self):
        product = Product("  Cafe  ", Decimal("3.50"))

        self.assertEqual(product.name, "Cafe")
        self.assertEqual(product.price, Decimal("3.50"))

    def test_rejects_empty_name(self):
        price = Decimal("3.50")

        with self.assertRaises(ValueError):
            Product("  ", price)

    def test_rejects_non_positive_price(self):
        for price in (Decimal("0"), Decimal("-1")):
            with self.subTest(price=price):
                with self.assertRaises(ValueError):
                    Product("Cafe", price)

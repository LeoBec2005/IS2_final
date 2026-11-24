import unittest
from decimal import Decimal

from catalogo.domain.product import Product
from catalogo.web.serializers import product_to_dict


class SerializerTests(unittest.TestCase):
    def test_serializes_product(self):
        self.assertEqual(
            {"id": 1, "name": "Cafe", "price": "3.50"},
            product_to_dict(Product("Cafe", Decimal("3.50"), id=1)),
        )

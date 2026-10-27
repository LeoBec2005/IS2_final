import unittest
from decimal import Decimal
from unittest.mock import Mock

from catalogo.application.product_service import ProductService
from catalogo.domain.product import Product
from catalogo.domain.repositories import ProductRepository


class ProductServiceTests(unittest.TestCase):
    def setUp(self):
        self.repository = Mock(spec=ProductRepository)
        self.service = ProductService(self.repository)

    def test_creates_product_using_repository(self):
        expected = Product("Cafe", Decimal("3.50"), id=1)
        self.repository.save.return_value = expected

        result = self.service.create_product("Cafe", Decimal("3.50"))

        self.assertEqual(expected, result)
        self.repository.save.assert_called_once_with(Product("Cafe", Decimal("3.50")))

    def test_returns_product_from_repository(self):
        expected = Product("Cafe", Decimal("3.50"), id=1)
        self.repository.get_by_id.return_value = expected

        result = self.service.get_product(1)

        self.assertEqual(expected, result)
        self.repository.get_by_id.assert_called_once_with(1)

    def test_raises_when_product_does_not_exist(self):
        self.repository.get_by_id.return_value = None

        with self.assertRaises(LookupError):
            self.service.get_product(99)

import unittest
from decimal import Decimal
from unittest.mock import Mock

from catalogo.application.product_service import ProductService
from catalogo.domain.errors import InvalidProductError, ProductNotFoundError
from catalogo.domain.product import Product
from catalogo.domain.repositories import ProductRepository


class DomainErrorsTests(unittest.TestCase):
    def test_invalid_price_raises_invalid_product_error(self):
        with self.assertRaises(InvalidProductError):
            Product("Cafe", Decimal("0"))

    def test_unknown_product_raises_not_found_error(self):
        repository = Mock(spec=ProductRepository)
        repository.get_by_id.return_value = None

        with self.assertRaises(ProductNotFoundError):
            ProductService(repository).get_product(99)

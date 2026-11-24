import sys
import unittest
from concurrent.futures import ThreadPoolExecutor
from decimal import Decimal

from catalogo.domain.product import Product
from catalogo.infrastructure.memory_repository import InMemoryProductRepository


class InMemoryProductRepositoryTests(unittest.TestCase):
    def test_save_assigns_unique_ids_under_concurrency(self):
        repository = InMemoryProductRepository()
        previous = sys.getswitchinterval()
        sys.setswitchinterval(1e-6)
        try:
            with ThreadPoolExecutor(max_workers=16) as pool:
                saved = list(
                    pool.map(
                        lambda i: repository.save(Product(f"p{i}", Decimal("1"))),
                        range(2000),
                    )
                )
        finally:
            sys.setswitchinterval(previous)

        self.assertEqual(2000, len({product.id for product in saved}))

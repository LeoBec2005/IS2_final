import unittest
from decimal import Decimal

from catalogo.domain.product import Product
from catalogo.infrastructure.memory_repository import InMemoryProductRepository


class InMemoryProductRepositoryTests(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryProductRepository()

    def test_save_assigns_incremental_ids(self):
        first = self.repo.save(Product("Cafe", Decimal("3.50")))
        second = self.repo.save(Product("Te", Decimal("2.00")))

        self.assertEqual((1, 2), (first.id, second.id))

    def test_get_by_id_returns_saved_product(self):
        saved = self.repo.save(Product("Cafe", Decimal("3.50")))

        self.assertEqual(saved, self.repo.get_by_id(saved.id))

    def test_get_by_id_returns_none_when_missing(self):
        self.assertIsNone(self.repo.get_by_id(99))

    def test_get_all_is_empty_at_start(self):
        self.assertEqual([], self.repo.get_all())

    def test_get_all_returns_every_saved_product(self):
        a = self.repo.save(Product("Cafe", Decimal("3.50")))
        b = self.repo.save(Product("Te", Decimal("2.00")))

        self.assertEqual([a, b], self.repo.get_all())

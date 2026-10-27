import unittest

from catalogo.infrastructure.memory_repository import InMemoryProductRepository
from catalogo.web.app import create_app


class ProductApiTests(unittest.TestCase):
    def setUp(self):
        self.repository = InMemoryProductRepository()
        self.client = create_app(self.repository).test_client()

    def test_create_and_get_product(self):
        response = self.client.post(
            "/products", json={"name": "Cafe", "price": "3.50"}
        )

        self.assertEqual(201, response.status_code)
        self.assertEqual(
            {"id": 1, "name": "Cafe", "price": "3.50"}, response.get_json()
        )
        self.assertEqual(
            response.get_json(), self.client.get("/products/1").get_json()
        )

    def test_rejects_product_with_invalid_price(self):
        response = self.client.post(
            "/products", json={"name": "Cafe", "price": "0"}
        )

        self.assertEqual(400, response.status_code)

    def test_rejects_non_numeric_price(self):
        response = self.client.post(
            "/products", json={"name": "Cafe", "price": "not-a-number"}
        )

        self.assertEqual(400, response.status_code)

    def test_rejects_missing_fields(self):
        response = self.client.post("/products", json={"name": "Cafe"})

        self.assertEqual(400, response.status_code)

    def test_rejects_non_string_name(self):
        response = self.client.post(
            "/products", json={"name": 42, "price": "3.50"}
        )

        self.assertEqual(400, response.status_code)

    def test_returns_not_found_for_unknown_product(self):
        response = self.client.get("/products/99")

        self.assertEqual(404, response.status_code)

    def test_lists_products(self):
        self.client.post("/products", json={"name": "Cafe", "price": "3.50"})

        response = self.client.get("/products")

        self.assertEqual(200, response.status_code)
        self.assertEqual(1, len(response.get_json()))

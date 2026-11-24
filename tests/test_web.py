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

        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            response.get_json(), {"id": 1, "name": "Cafe", "price": "3.50"}
        )
        self.assertEqual(
            response.get_json(), self.client.get("/products/1").get_json()
        )

    def test_rejects_product_with_invalid_price(self):
        response = self.client.post(
            "/products", json={"name": "Cafe", "price": "0"}
        )

        self.assertEqual(response.status_code, 400)

    def test_rejects_non_numeric_price(self):
        response = self.client.post(
            "/products", json={"name": "Cafe", "price": "not-a-number"}
        )

        self.assertEqual(response.status_code, 400)

    def test_rejects_missing_fields(self):
        response = self.client.post("/products", json={"name": "Cafe"})

        self.assertEqual(response.status_code, 400)

    def test_rejects_non_string_name(self):
        response = self.client.post(
            "/products", json={"name": 42, "price": "3.50"}
        )

        self.assertEqual(response.status_code, 400)

    def test_returns_not_found_for_unknown_product(self):
        response = self.client.get("/products/99")

        self.assertEqual(response.status_code, 404)

    def test_lists_products(self):
        self.client.post("/products", json={"name": "Cafe", "price": "3.50"})

        response = self.client.get("/products")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 1)

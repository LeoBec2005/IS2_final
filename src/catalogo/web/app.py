from flask import Flask, jsonify, request

from catalogo.application.product_service import ProductService
from catalogo.domain.errors import InvalidProductError, ProductNotFoundError
from catalogo.domain.repositories import ProductRepository
from catalogo.infrastructure.memory_repository import InMemoryProductRepository
from catalogo.web.payloads import parse_product_payload
from catalogo.web.serializers import product_to_dict


def create_app(repository: ProductRepository | None = None) -> Flask:
    app = Flask(__name__)
    service = ProductService(repository or InMemoryProductRepository())

    @app.get("/products")
    def list_products():
        return jsonify([product_to_dict(product) for product in service.list_products()])

    @app.post("/products")
    def create_product():
        try:
            name, price = parse_product_payload(request.get_json(silent=True))
            product = service.create_product(name, price)
        except InvalidProductError as error:
            return jsonify({"error": str(error)}), 400
        return jsonify(product_to_dict(product)), 201

    @app.get("/products/<int:product_id>")
    def get_product(product_id: int):
        try:
            product = service.get_product(product_id)
        except ProductNotFoundError as error:
            return jsonify({"error": str(error)}), 404
        return jsonify(product_to_dict(product))

    return app


if __name__ == "__main__":
    create_app().run(debug=True)

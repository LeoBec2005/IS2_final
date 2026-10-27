from decimal import Decimal

from catalogo.domain.product import Product
from catalogo.domain.repositories import ProductRepository


class ProductService:
    def __init__(self, repository: ProductRepository) -> None:
        self._repository = repository

    def create_product(self, name: str, price: Decimal) -> Product:
        return self._repository.save(Product(name=name, price=price))

    def get_product(self, product_id: int) -> Product:
        product = self._repository.get_by_id(product_id)
        if product is None:
            raise LookupError("Producto no encontrado.")
        return product

    def list_products(self) -> list[Product]:
        return self._repository.get_all()

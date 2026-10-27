from typing import Protocol

from catalogo.domain.product import Product


class ProductRepository(Protocol):
    def save(self, product: Product) -> Product:
        ...

    def get_by_id(self, product_id: int) -> Product | None:
        ...

    def get_all(self) -> list[Product]:
        ...

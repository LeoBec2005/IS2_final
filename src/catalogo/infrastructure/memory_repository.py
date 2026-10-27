from dataclasses import replace

from catalogo.domain.product import Product


class InMemoryProductRepository:
    def __init__(self) -> None:
        self._products: dict[int, Product] = {}
        self._next_id = 1

    def save(self, product: Product) -> Product:
        saved_product = replace(product, id=self._next_id)
        self._products[self._next_id] = saved_product
        self._next_id += 1
        return saved_product

    def get_by_id(self, product_id: int) -> Product | None:
        return self._products.get(product_id)

    def get_all(self) -> list[Product]:
        return list(self._products.values())

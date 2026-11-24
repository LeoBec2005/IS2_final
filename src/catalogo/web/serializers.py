from catalogo.domain.product import Product


def product_to_dict(product: Product) -> dict:
    return {"id": product.id, "name": product.name, "price": str(product.price)}

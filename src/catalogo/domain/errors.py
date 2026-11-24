class ProductError(Exception):
    """Base de los errores del dominio de productos."""


class InvalidProductError(ProductError, ValueError):
    """Los datos del producto no cumplen las reglas del dominio."""


class ProductNotFoundError(ProductError, LookupError):
    """No existe un producto con el identificador pedido."""

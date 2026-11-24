from decimal import Decimal, InvalidOperation

from catalogo.domain.errors import InvalidProductError


def parse_product_payload(data) -> tuple[str, Decimal]:
    if (
        not isinstance(data, dict)
        or not isinstance(data.get("name"), str)
        or "price" not in data
    ):
        raise InvalidProductError("Se requieren name y price.")
    try:
        return data["name"], Decimal(str(data["price"]))
    except InvalidOperation as error:
        raise InvalidProductError("El precio debe ser un numero.") from error

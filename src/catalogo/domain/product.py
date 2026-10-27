from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Product:
    name: str
    price: Decimal
    id: int | None = None

    def __post_init__(self) -> None:
        if not self.name or not self.name.strip():
            raise ValueError("El nombre del producto no puede estar vacio.")
        if not self.price.is_finite() or self.price <= 0:
            raise ValueError("El precio debe ser un numero positivo.")
        object.__setattr__(self, "name", self.name.strip())

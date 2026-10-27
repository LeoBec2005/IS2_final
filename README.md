# Catalogo Lab 05

Proyecto base pequeño para practicar las actividades del laboratorio de pruebas
unitarias, integración, dobles de prueba y cobertura.

## Requisitos

- Python 3.10 o superior
- `pip`

## Preparar el entorno

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

En Windows, activa el entorno con `.venv\Scripts\activate`.

## Ejecutar las pruebas

```bash
python -m unittest discover -s tests -v
```

## Generar cobertura

```bash
coverage run -m unittest discover -s tests
coverage report -m
coverage html
```

El reporte HTML queda en `htmlcov/index.html`.

## Ejecutar la API web

```bash
python -m catalogo.web.app
```

La API queda disponible en `http://127.0.0.1:5000`:

- `GET /products`: listar productos
- `POST /products`: crear producto con JSON `{"name": "Cafe", "price": "3.50"}`
- `GET /products/1`: consultar producto por ID

## Estructura y actividades

- `src/catalogo/domain/product.py`: entidad e invariantes del dominio.
- `src/catalogo/domain/repositories.py`: contrato del repositorio.
- `src/catalogo/application/product_service.py`: servicio de aplicación.
- `src/catalogo/infrastructure/memory_repository.py`: repositorio en memoria para el ejemplo.
- `src/catalogo/web/app.py`: API Flask y punto de composición.
- `tests/test_product.py`: pruebas unitarias de la entidad.
- `tests/test_product_service.py`: pruebas del servicio usando `unittest.mock`.
- `tests/test_web.py`: pruebas de integración de la API con el repositorio real en memoria.

Las pruebas son ejemplos iniciales: agrega casos, cambia el comportamiento siguiendo
TDD y registra las tareas/issues del equipo en GitHub Projects como pide la guía.
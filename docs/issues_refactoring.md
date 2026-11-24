# Práctica 07: Issues identificados y estrategia de refactoring

Proyecto: Catálogo de productos (API Flask). Repositorio: https://github.com/LeoBec2005/IS2_final

El reporte combina los issues detectados por SonarQube y los de la revisión manual de código.

| Smell o Bug o Vulnerabilidad | Módulo o Componente | Responsable | Prioridad (Alta, Media o Baja) | Estrategia de Refactoring | Categoría (Clean Code, SOLID o ...) | Descripción |
|---|---|---|---|---|---|---|
| Vulnerabilidad: modo debug activo | `web/app.py` | Leonardo Becerra | Alta | Reemplazar valor fijo por configuración (variable de entorno) | Seguridad | `app.run(debug=True)` habilita el depurador de Werkzeug, que permite ejecutar código de forma remota (SonarQube, regla S4507). |
| Bug: condición de carrera al generar ids | `infrastructure/memory_repository.py` | Leonardo Becerra | Alta | Encapsular el contador con un `Lock` | Confiabilidad | `save()` lee e incrementa `_next_id` sin sincronización; con el servidor de Flask multihilo dos productos pueden recibir el mismo id (revisión manual). |
| Code smell: excepciones genéricas | `domain/` y `application/` | Leonardo Becerra | Media | Extract Class (excepciones propias del dominio) | Clean Code | Se lanzan `ValueError` y `LookupError`, y la capa web depende de esos tipos genéricos (revisión manual). |
| Code smell: validación mezclada en la ruta | `web/app.py` (`create_product`) | Leonardo Becerra | Media | Extract Method | SOLID (SRP) | La ruta valida el JSON, convierte el precio y mapea errores, todo en una sola función (revisión manual). |
| Code smell: Feature Envy | `web/app.py` (`serialize`) | Leonardo Becerra | Baja | Move Method | Clean Code | `serialize` es una función anidada que solo manipula atributos de `Product`; debería vivir en un módulo propio (revisión manual). |

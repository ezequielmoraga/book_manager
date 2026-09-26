# Changelog

## [Ejercicio 3]
- Definición de la interfaz genérica IRepositorio[T] (crear, leer_por_id, leer_todos, actualizar, eliminar) y su implementación en memoria RepositorioGenerico.
- Definición de interfaces específicas IRepositorioStock e IRepositorioCotizacionDolar (con clave propia: libro_id, y tipo+fecha respectivamente) y sus implementaciones.

## [Ejercicio 2]
- Definición de las entidades del dominio: EntidadBase, Genero, Editorial, Moneda, TipoCotizacion, CotizacionDolar, Libro, Precio, Stock.
- Aplicación de encapsulamiento (atributos privados con `__`, properties con validación en los setters).
- Relaciones por composición entre entidades (Libro-Genero, Libro-Editorial, Precio-Libro, Precio-Moneda, Stock-Libro, CotizacionDolar-TipoCotizacion).

## [Ejercicio 1]
- Inicialización del repositorio y creación de la rama Sprint_1.
- Creación de la estructura de directorios del proyecto.
- Creación de paquetes Python (`__init__.py`) en cada módulo.
- Creación de la carpeta migrations/csv para los archivos de datos.
- Agregado de README.md con objetivo e introducción del Sprint 1.
- Agregado de .gitignore y requirements.txt.
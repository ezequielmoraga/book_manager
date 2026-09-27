import csv
from datetime import datetime

from book_manager.entities.entities import (
    Genero,
    Editorial,
    Moneda,
    TipoCotizacion,
    CotizacionDolar,
    Libro,
    Precio,
    Stock
)


def cargar_datos(
    repo_generos,
    repo_editoriales,
    repo_monedas,
    repo_tipos_cotizacion,
    repo_libros,
    repo_precios,
    repo_stock,
    repo_cotizaciones
):

    carpeta = "src/book_manager/migrations/csv/"

    generos = {}
    editoriales = {}
    monedas = {}
    tipos_cotizacion = {}

    # -----------------------------
    # DATOS BASE
    # -----------------------------

    with open(carpeta + "datos_base.csv", "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        id_genero = 1
        id_editorial = 1
        id_moneda = 1
        id_tipo = 1

        for fila in lector:

            if fila["tipo"] == "genero":

                genero = Genero(
                    id=id_genero,
                    nombre=fila["nombre"]
                )

                repo_generos.crear(genero)
                generos[fila["nombre"]] = genero
                id_genero += 1

            elif fila["tipo"] == "editorial":

                editorial = Editorial(
                    id=id_editorial,
                    nombre=fila["nombre"],
                    sede=fila["sede"]
                )

                repo_editoriales.crear(editorial)
                editoriales[fila["nombre"]] = editorial
                id_editorial += 1

            elif fila["tipo"] == "moneda":

                moneda = Moneda(
                    id=id_moneda,
                    codigo=fila["codigo"],
                    nombre=fila["nombre"]
                )

                repo_monedas.crear(moneda)
                monedas[fila["codigo"]] = moneda
                id_moneda += 1

            elif fila["tipo"] == "tipo_cotizacion":

                tipo = TipoCotizacion(
                    id=id_tipo,
                    nombre=fila["nombre"]
                )

                repo_tipos_cotizacion.crear(tipo)
                tipos_cotizacion[fila["nombre"]] = tipo
                id_tipo += 1

    # -----------------------------
    # LIBROS, PRECIOS Y STOCK
    # -----------------------------

    with open(carpeta + "libros.csv", "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        id_libro = 1
        id_precio = 1
        id_stock = 1

        for fila in lector:

            genero = generos[fila["genero"]]
            editorial = editoriales[fila["editorial"]]
            moneda = monedas[fila["moneda"]]

            libro = Libro(
                id=id_libro,
                isbn=fila["isbn"],
                titulo=fila["titulo"],
                autor=fila["autor"],
                genero=genero,
                editorial=editorial
            )

            repo_libros.crear(libro)

            fecha = datetime.strptime(
                fila["fecha_vigencia"],
                "%Y-%m-%d"
            ).date()

            precio = Precio(
                id=id_precio,
                libro=libro,
                moneda=moneda,
                monto=float(fila["precio"]),
                fecha_vigencia=fecha
            )

            repo_precios.crear(precio)

            stock = Stock(
                id=id_stock,
                libro=libro,
                cantidad=int(fila["stock"])
            )

            repo_stock.crear(stock)

            id_libro += 1
            id_precio += 1
            id_stock += 1

    # -----------------------------
    # COTIZACIONES
    # -----------------------------

    with open(carpeta + "cotizaciones.csv", "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        id_cotizacion = 1

        for fila in lector:

            tipo = tipos_cotizacion[fila["tipo"]]

            fecha = datetime.strptime(
                fila["fecha"],
                "%Y-%m-%d"
            ).date()

            cotizacion = CotizacionDolar(
                id=id_cotizacion,
                tipo_cotizacion=tipo,
                fecha=fecha,
                valor_compra=float(fila["valor_compra"]),
                valor_venta=float(fila["valor_venta"])
            )

            repo_cotizaciones.crear(cotizacion)

            id_cotizacion += 1
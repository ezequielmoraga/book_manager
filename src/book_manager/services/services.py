"""Servicios con la lógica de negocio de Book Manager."""

from book_manager.entities.entities import Stock, CotizacionDolar
from book_manager.repositories.repositories import (RepositorioGenerico,RepositorioStock,RepositorioCotizacionDolar)


class ServicioGenerico:
    """Servicio para las entidades que utilizan el repositorio genérico."""

    def __init__(self, repositorio: RepositorioGenerico) -> None:
        self.__repositorio = repositorio

    def crear(self, entidad):
        """Crea una nueva entidad."""
        return self.__repositorio.crear(entidad)

    def buscar_por_id(self, id: int):
        """Busca una entidad por su ID."""
        return self.__repositorio.leer_por_id(id)

    def listar(self):
        """Devuelve todas las entidades."""
        return self.__repositorio.leer_todos()

    def actualizar(self, entidad):
        """Actualiza una entidad existente."""
        return self.__repositorio.actualizar(entidad)

    def eliminar(self, id: int) -> bool:
        """Elimina una entidad por su ID."""
        return self.__repositorio.eliminar(id)


class StockService:
    """Servicio encargado de las operaciones relacionadas con el stock."""

    def __init__(self, repositorio: RepositorioStock) -> None:
        self.__repositorio = repositorio

    def crear(self, stock: Stock) -> Stock:
        """Crea un registro de stock."""
        return self.__repositorio.crear(stock)

    def buscar_por_libro(self, libro_id: int):
        """Busca el stock correspondiente a un libro."""
        return self.__repositorio.leer_por_libro(libro_id)

    def actualizar(self, stock: Stock) -> Stock:
        """Actualiza el stock de un libro."""
        return self.__repositorio.actualizar(stock)

    def eliminar(self, libro_id: int) -> bool:
        """Elimina el stock correspondiente a un libro."""
        return self.__repositorio.eliminar(libro_id)


class CotizacionDolarService:
    """Servicio encargado de las operaciones de cotización del dólar."""

    def __init__(self, repositorio: RepositorioCotizacionDolar) -> None:
        self.__repositorio = repositorio

    def crear(self, cotizacion: CotizacionDolar) -> CotizacionDolar:
        """Crea una nueva cotización."""
        return self.__repositorio.crear(cotizacion)

    def buscar_por_tipo_y_fecha(self, tipo_id: int, fecha):
        """Busca una cotización por tipo y fecha."""
        return self.__repositorio.leer_por_tipo_y_fecha(tipo_id, fecha)

    def listar_historico(self, tipo_id: int):
        """Devuelve el histórico de cotizaciones de un tipo."""
        return self.__repositorio.leer_historico_por_tipo(tipo_id)

    def actualizar(self, cotizacion: CotizacionDolar) -> CotizacionDolar:
        """Actualiza una cotización existente."""
        return self.__repositorio.actualizar(cotizacion)

    def eliminar(self, tipo_id: int, fecha) -> bool:
        """Elimina una cotización según su tipo y fecha."""
        return self.__repositorio.eliminar(tipo_id, fecha)
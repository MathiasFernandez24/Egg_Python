from . import Producto


class Libro(Producto):
    def __init__(self, codigo: int, nombre: str, precio_sin_impuesto: float, isbn:str, autor:str, stock: int = 0):
        super().__init__(codigo, nombre, precio_sin_impuesto, stock)
        self.isbn:str = isbn
        self.autor:str = autor
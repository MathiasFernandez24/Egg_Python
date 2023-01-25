from . import Producto


class Cafe(Producto):
    def __init__(self, codigo: int, nombre: str, precio_sin_impuesto: float, descripcion:str, proveedor:str, stock: int = 0):
        super().__init__(codigo, nombre, precio_sin_impuesto, stock)
        self.descripcion:str = descripcion
        self.proveedor:str = proveedor
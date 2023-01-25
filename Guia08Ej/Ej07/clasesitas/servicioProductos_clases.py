from .cafe_clase import Cafe
from .libro_clase import Libro


class ServicioProductos:
    def __init__(self):
        pass
        
    def listar_productos(self):
        print("---> mostrar lista desde servicio")
        for i in Cafe.lista_productos:
            print("")
            print("codigo: ", i.codigo)
            print("nombre: ",i.nombre)
            print("precio: ",i.precio_con_impuesto)
            print("stock: ",i.stock)
            if isinstance(i,Libro):
                print("autor: ", i.autor)
                print("isbn: ", i.isbn)
            if isinstance(i,Cafe):
                print("descripcion: ", i.descripcion)
                print("proveedor: ", i.proveedor)
from . import Administrador
# from . import Cafe
# from . import Libro


class Producto(Administrador):
    impuesto:float= 21.0
    lista_productos: list["Producto"]=[]

    def __init__(self, codigo:int, nombre:str, precio_sin_impuesto:float, stock:int= 0):
        self.codigo = codigo
        self.nombre = nombre
        self.precio_con_impuesto = self.funcion_precio_final(precio_sin_impuesto)
        self.stock = stock

    def funcion_precio_final(self, precio_sin_impuesto)->float:
        precio_final = precio_sin_impuesto*(1+self.impuesto/100)
        return precio_final

    def funcion_comprar(self, cantidad:int):
        if self.validar_accion():
            if cantidad>0:
                if self in Producto.lista_productos:
                    print(f"Tenemos {self.stock} {self.nombre} en Stock, se agregan {cantidad} , en total hay {self.stock+cantidad}")
                    self.stock+=cantidad
                else:
                    print(f"--> {self.nombre} No existe, lo agregaremos ahora")
                    self.stock+=cantidad
                    Producto.lista_productos.append(self)
            else:
                print("######## Hermano, no estoy pa esa.... plis, numeros positivos enteros")

    def funcion_vender(self, cantidad:int):
        if self.validar_accion():
            if cantidad>0:
                if self in Producto.lista_productos:
                    if cantidad < self.stock:
                        print(f"Venta realizada, Teniamos {self.stock}, vendimos {cantidad}, y ahora tenemos {self.stock-cantidad}")
                        self.stock-= cantidad 
                    elif cantidad == self.stock:
                        print(f"Vendimos todo el stock, que era {self.stock}")
                        Producto.lista_productos.remove(self)
                    elif cantidad>self.stock:
                        print(f"No puedes vender mas de {self.stock}") 
                else:
                    print(f"{self.nombre} No se encuentra en nuestra lista ") 
            else:
                print("######## Hermano, no estoy pa esa.... plis, numeros positivos enteros")

    # def listar_productos(self):
    #     print("---> mostrar lista desde", self.nombre)
    #     for i in Producto.lista_productos:
    #         print("")
    #         print("codigo: ", i.codigo)
    #         print("nombre: ",i.nombre)
    #         print("precio: ",i.precio_con_impuesto)
    #         print("stock: ",i.stock)
    #         if isinstance(i,Libro):
    #             print("autor: ", i.autor)
    #             print("isbn: ", i.isbn)
    #         if isinstance(i,Cafe):
    #             print("descripcion: ", i.descripcion)
    #             print("proveedor: ", i.proveedor)
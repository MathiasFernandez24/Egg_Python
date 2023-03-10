from typing import Optional


class Administrador:
    password: str = "admin"
    def validar_accion(self)->bool:
        print(Administrador.password)
        print(self.password)
        print("##Validar accion##")
        clave = input("ingresa password")
        if clave == self.password:
            print("*Clave exitosa VVVVV")
            return True
        else:
            print("*Clave erronea XXXXXX")
            return False

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

    def listar_productos(self):
        print("---> mostrar lista desde", self.nombre)
        for i in Producto.lista_productos:
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
            




class Cafe(Producto):
    def __init__(self, codigo: int, nombre: str, precio_sin_impuesto: float, descripcion:str, proveedor:str, stock: int = 0):
        super().__init__(codigo, nombre, precio_sin_impuesto, stock)
        self.descripcion:str = descripcion
        self.proveedor:str = proveedor

class Libro(Producto):
    def __init__(self, codigo: int, nombre: str, precio_sin_impuesto: float, isbn:str, autor:str, stock: int = 0):
        super().__init__(codigo, nombre, precio_sin_impuesto, stock)
        self.isbn:str = isbn
        self.autor:str = autor


p_tornillo = Producto(100,"TORNILLO", 1)
p_destornillador = Producto(101,"DESTORNILLADOR", 200)
p_alicate = Producto(102,"ALICATE", 350)
C_capuchino = Cafe(200,"Capuchino",400,"muy rico","Cabrales")
L_caperuza = Libro(300,"Capucita roja",900,"####999####","Maira lo hizo")

p_tornillo.funcion_comprar(1)
p_destornillador.funcion_comprar(1)
p_alicate.funcion_comprar(1)

C_capuchino.funcion_comprar(1)
L_caperuza.funcion_comprar(1)

L_caperuza.listar_productos()

L_caperuza.listar_productos()
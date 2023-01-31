class Empleado:
    def __init__(self, nombre_completo, nombre_proyecto):
        self.nombre_completo = nombre_completo
        self.nombre_proyecto = nombre_proyecto
    
    @staticmethod
    def tareas_a_realizar(nombre_ingresado):
        if nombre_ingresado=="Electromagnetismo":
            tareas=['tarea1','tarea2','tarea3']
        else:
            tareas=['tarea1']
        return tareas

    def trabajar(self):
        return Empleado.tareas_a_realizar(self.nombre_proyecto)

    # end def

empleado_01 = Empleado("Maira", "Electromagnetismo")
empleado_02 = Empleado("Mathi", "motores")

class Producto:
    def __init__(self, nombre: str, cantidad: int):
        self.nombre: str = nombre
        self.cantidad: int = cantidad
    def __add__(self, producto: "Producto"):
        suma_cantidades = self.cantidad + producto.cantidad
        return suma_cantidades
    def __radd__(self, otro):
        if otro == 0:
            return self
        else:
            return self.__add__(otro)


class Cafe(Producto):
    def __init__(self, nombre: str, cantidad: int, cm3:int):
        super().__init__(nombre, cantidad)
        self.cm3=cm3

class Libro(Producto):
    def __init__(self, nombre: str, cantidad: int, paginas:int):
        super().__init__(nombre, cantidad)
        self.paginas=paginas



p1 = Producto("Teclado", 3)
p2 = Producto("Mouse", 4)
p3 = Producto("monitor", 40)
c1 = Cafe("capuchino", 6, 350)
l1 = Libro("caperuza", 10, 1500)
total_cantidad_productos = p1 + l1
total_cantidad_productos_2 = c1+l1
lista=[p1,p3]
print(sum(lista))
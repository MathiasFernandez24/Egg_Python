class Empleado:
    def __init__(self, nombre_completo, salario_base):
        self.nombre_completo = nombre_completo
        self.__salario_base:int = salario_base
    
    @property
    def nombre(self):
        return self.nombre_completo

    @nombre.getter
    def nombre(self):
        print(f"{self.nombre_completo} es el nombre")
        return "x"
    
    @nombre.setter
    def nombre(self, valor_nuevo):
        print(f"{self.nombre_completo} fue cambiado por {valor_nuevo}")
        self.nombre_completo=valor_nuevo

    @nombre.deleter
    def nombre(self):
        print(f"{self.nombre_completo} ha sido eliminado (solo el nombre)")
        self.nombre_completo=""

empleado_01 = Empleado("Maira", 1000)
empleado_02 = Empleado("Mathi", 100)

empleado_01.nombre
empleado_01.nombre="Mathi"
empleado_01.nombre
del empleado_01.nombre
empleado_01.nombre
print(empleado_01.__dict__)



class Empleado:
    def __init__(self, nombre_completo, salario_base):
        self.nombre_completo = nombre_completo
        self.__salario_base:int = salario_base

    def _get_salario_base(self):
        return self.__salario_base
        

class Vendedor(Empleado):
    def __init__(self, nombre_completo, salario_base):
        super().__init__(nombre_completo, salario_base)
        self.sueldo:int = self._get_salario_base()*2


empleado_01 = Vendedor("Maira", 1000)
empleado_02 = Vendedor("Mathi", 100)

print(empleado_01.__dict__)
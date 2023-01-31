class Empleado:
    def __init__(self, nombre_completo, nombre_proyecto):
        self.nombre_completo = nombre_completo
        self.__nombre_proyecto = nombre_proyecto

    def get_nombre_proyecto(self):
        return self.__nombre_proyecto

    def set_nombre_proyecto(self, nuevo_nombre):
        self.__nombre_proyecto=nuevo_nombre


empleado_01 = Empleado("Maira", "Electromagnetismo")
empleado_02 = Empleado("Mathi", "motores")


print(empleado_01.get_nombre_proyecto())
print(empleado_01.__dict__)
empleado_01.set_nombre_proyecto("nuevo nombre1")
empleado_01.__nombre_proyecto="nuevo_nombre2"
# empleado_01.nueva_variable="soy nuevo"
print(empleado_01.__dict__)
# print(empleado_01._Empleado__nombre_proyecto)
# empleado_01._Empleado__nombre_proyecto="modificado"
# print(empleado_01._Empleado__nombre_proyecto)
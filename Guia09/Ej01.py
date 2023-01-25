class Estudiante:
    escuela="E.C.L.G.S.M."
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def mostrar(self):
        print(f"estudiante {self.name}, de  {self.age} años, escuela {Estudiante.escuela}")

    def cambiar_edad(self, nueva_edad):
        self.age=nueva_edad
    
    @classmethod
    def modificar_nombre_escuela(cls, nuevo_nombre):
        cls.escuela=nuevo_nombre


estudiante_mathi = Estudiante("Mathias", 29)
estudiante_maira = Estudiante("Maira", 36)
estudiante_maira.mostrar()
estudiante_mathi.mostrar()
estudiante_mathi.cambiar_edad(30)
estudiante_mathi.mostrar()
estudiante_mathi.modificar_nombre_escuela("Industrial")
estudiante_maira.mostrar()
estudiante_mathi.mostrar()
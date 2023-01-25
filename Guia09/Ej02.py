from datetime import date


class Estudiante:
    def __init__(self, name, age_constructor):
        self.name = name
        self.age = age_constructor
    
    def mostrar(self):
        print(f"estudiante {self.name}, de  {self.age} años")

    @classmethod
    def calcular_edad(cls,nombre_recibido, anio_nacimiento):
        edad_calculada = date.today().year-anio_nacimiento
        return cls(age_constructor=edad_calculada,name=nombre_recibido)
    
e1 = Estudiante("Mathi", 29)
e1.mostrar()

e2 = Estudiante.calcular_edad("Maira",1986)
e2.mostrar()
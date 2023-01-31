from dataclasses import dataclass, field, asdict
from typing import Any
from pprint import pprint


@dataclass
class Persona():
    sort_index: Any = field(init=False, repr=False)
    nombre:str
    apellido:str
    dni:int
    anio_nacimiento:int

    def __post_init__(self):
        self.sort_index=self.dni

@dataclass
class Estudiante(Persona):
    escuela:str
    curso:str
    materia:str
    anio_aprobado:bool

@dataclass(order=True)
class Profesor(Persona):
    sort_index: Any = field(init=False, repr=False)
    materia_dictada:str
    titular:bool
    sueldo:int
    sexo:str

    def __post_init__(self):
        super().__post_init__()
        self.sort_index=self.dni


e_01 = Estudiante("Mathi","Fernandez",37649242,1993,"E.C.L.G.S.M", "B", "Lengua", True)
e_02 = Estudiante("Mai","Julian",32447252,1986,"Maria Auxiliadora", "A", "Informatica", True)
e_03 = Estudiante("Mathi__2","Fernandez",37649242,1993,"E.C.L.G.S.M", "B", "Lengua", True)
e_04 = Estudiante("Mai__2","Fernandez",32447252,1986,"Maria Auxiliadora", "A", "Informatica", True)

p_01 = Profesor("Mathi_profe","Fernandez",37649242,1993,"React Native", False, 80_000, "M")
p_02 = Profesor("zzMai_profe","Julian",39447252,1986,"Full Stack", False, 95_000, "x")
p_03 = Profesor("Mathi_profe","Fernandez",37649242,1993,"React Native", False, 70_000, "M")
p_04 = Profesor("zzMai_profe","Julian",36447252,1986,"Full Stack", False, 150_000, "x")

profes = [p_03,p_02,p_01,p_04]
profes_ser=[]
for i in profes:
    profes_ser.append(asdict(i))

pprint(profes_ser)
estudiantes = [e_03,e_02,e_01,e_04]

# pprint(profes)
print("")
print("-------------------------------------")
print("")
# for i in  sorted(profes):
#     pprint(i)
































# from dataclasses import dataclass, asdict, astuple, field
# from typing import Any


# class Empleado:
#     def __init__(self, nombre_completo, salario_base):
#         self.nombre_completo = nombre_completo
#         self.__salario_base:int = salario_base
#     def __eq__(self, otro):
#         return "clase 1"

# class Empleado_02:
#     def __init__(self, nombre_completo, salario_base):
#         self.nombre_completo = nombre_completo
#         self.__salario_base:int = salario_base
#     def __eq__(self, otro):
#         return "clase 2"

# @dataclass
# class Empleado_2:
#     nombre:str
#     edad:int = field(init=False, repr=False)
#     def __post_init__(self):
#         self.edad=9


# @dataclass(order=True)
# class Empleado_comparador:
#     sort_index: Any = field(init=False, repr=False)
#     edad:int 
#     nombre:int
#     apellido:int

#     def __post_init__(self):
#         self.sort_index= self.edad, self.apellido

# e_01 = Empleado("Maira", 1000)
# e_02 = Empleado_02("Mathi", 100)
# # e_03 = Empleado_2("Mairaaaaa", 100099999)
# # e_04 = Empleado_2("Mathiiiiii", 10099999)
# e_05 = Empleado_2("Mairita")
# e_06 = Empleado_2("Mairita")

# e_07 = Empleado_comparador(8,23,1000)
# e_08 = Empleado_comparador(8,21,1001)
# e_09 = Empleado_comparador(7,21,1002)

# # print(e_07==e_08)
# arraicito=[e_07, e_08, e_09]

# for i in  sorted(arraicito):
#     print(i)

# print(f"{e_09.apellido:_}")
# print()

# # print(e_02.__eq__(e_01))
# # print(e_02==e_01)

# # e_05_tupla = astuple(e_05)
# # e_06_tupla = astuple(e_06)
# # print(e_05_tupla==e_06_tupla)
# # print(e_05_tupla)
# # print(e_06_tupla)


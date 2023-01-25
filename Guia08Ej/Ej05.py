from datetime import date

class ComportamientoUsuario:
    def comprar_en_3_cuotas(self):
        print("Compraste algo en 3 cuotas")
    def comprar_en_6_cuotas(self):
        print("Compraste algo en 6 cuotas")
    def comprar_en_12_cuotas(self):
        print("Compraste algo en 12 cuotas")

class Titular:
    def __init__(self, nombre:str, apellido:str, dni:int, fecha_nacimiento:date,domicilio:str,telefono:int):
        self.nombre:str = nombre
        self.dni:int = dni
        self.fecha_nacimiento:date = fecha_nacimiento
        self.apellido:str = apellido
        self.domicilio:str = domicilio
        self.telefono:int = telefono

class TarjetaDeCredito(ComportamientoUsuario):
    def __init__(self, titular:Titular, numero_tarjeta:int, vencimiento:date, codigo_seguridad:int):
        self.nombre:str = titular.nombre
        self.apellido:str = titular.apellido
        self.numero_tarjeta:int = numero_tarjeta
        self.vencimiento:date = vencimiento
        self.codigo_seguridad:int= codigo_seguridad




usuario_maira = Titular("Maira","Julia",32447252,date(1986,10,15),"Rivadavia, San Juan", 2645045367)

tarjeta_maira = TarjetaDeCredito(usuario_maira, 123123,date.today(),159)

print(tarjeta_maira.nombre)

tarjeta_maira.comprar_en_12_cuotas()
tarjeta_maira.comprar_en_6_cuotas()
tarjeta_maira.comprar_en_3_cuotas()

class Rueda:
    def __init__(self, tamanio:int, color:str):
        self.tamanio = tamanio
        self.color = color

class Pedales:
    def __init__(self, material:str, color:str):
        self.material:str = material
        self.color:str = color

class Asiento:
    def __init__(self, color:str, cuero:bool):
        self.color:str = color
        self.cuero:bool= cuero

class Manubrio:
    def __init__(self, cantidad_frenos:int, mango:str):
        self.cantidad_frenos:int = cantidad_frenos
        self.mango:str = mango

class Bicicleta:
    def __init__(self, rueda:Rueda, pedalin:Pedales, asiento:Asiento,manubrio:Manubrio):
        self.rueda:Rueda = rueda
        self.pedalin:Pedales = pedalin
        self.asiento:Asiento=asiento
        self.manubrio:Manubrio=manubrio

    def darUnaVueltita(self):
        print("5km recorridos!")
        


rueda_01 = Rueda(29,"negra")
pedal_01 = Pedales("plastico", "blanco")
asiento_01 = Asiento("amarillo", False)
manubrio_01= Manubrio(2,"plastiquito")

bici_de_Maira = Bicicleta(rueda_01,pedal_01,asiento_01,manubrio_01)

print(bici_de_Maira.rueda.__dict__)
bici_de_Maira.darUnaVueltita()
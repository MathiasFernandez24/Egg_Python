from typing import Optional

class Lugar:
    def __init__(self, localidad:str, distancia:float):
        self.localidad = localidad
        self.distancia = distancia

class Saldo:
    def __init__(self, balance:float=0) -> None:
        self.balance:float=balance

class Padre:
    super_mensaje="hola, soy un supérmensaje"
    def __init__(self,mensaje:str) -> None:
        self.mensaje= mensaje
    def imprimir_algo(self):
        return self.mensaje,

class Persona(Padre):
    estan_vivos= True

    def __init__(self,mensaje:str, nombre_recibido:str, edad_recibida:int, celular:str, trabajo_recibido: Optional[str]=None) -> None:
        super().__init__(mensaje)
        self.nombre = nombre_recibido
        self.edad = edad_recibida
        self.prueba = True
        self.trabajo = trabajo_recibido
        self.telefono = celular
        

    def esta_trabajando(self):
        if self.trabajo:
            situacion_laboral = "Tengo trabajo, hurra!!"
        else:
            situacion_laboral= "situacion de android"
        return situacion_laboral

class Hija(Persona, Lugar, Saldo):
    def __init__(self, mensaje: str, nombre_recibido: str, edad_recibida: int,celular:str,localidad:str, distancia:float, trabajo_recibido: Optional[str] = None,balance:float=0) -> None:
        Persona.__init__(self,mensaje, nombre_recibido, edad_recibida,celular, trabajo_recibido)
        Lugar.__init__(self,localidad,distancia)
        Saldo.__init__(self, balance)
        self.clave = self.generar_clave()

    def generar_clave(self):
        return self.nombre + self.telefono

class Cliente:
    def __init__(self, persona_recibida:Persona, cbu) -> None:
        self.persona_local: Persona= persona_recibida
        self.cbu=cbu

padre_01 = Padre("aaaa")
persona_01= Persona("bbbb","Mai", 36, "321" ,"Emicar... por ahora...")
hija_01= Hija("bbbb","Mai", 36, "321" ,"Rivadavia", 485.85,"Emicar... por ahora...",8)


# print(padre_01.__dict__)
# print(persona_01.__dict__)
# print(hija_01.__dict__)
# s = Saldo(45.56)
print(hija_01.__dict__)

cliente_01= Cliente(persona_01, 123456)


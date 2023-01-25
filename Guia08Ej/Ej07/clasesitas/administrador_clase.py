class Administrador:
    password: str = "admin"
    def validar_accion(self)->bool:
        print(Administrador.password)
        print(self.password)
        print("##Validar accion##")
        clave = input("ingresa password:  ")
        if clave == self.password:
            print("\n**Clave exitosa VVVVV")
            return True
        else:
            print("\n**Clave erronea XXXXXX")
            return False

def funcion_de_prueba_importacion():
    print("Importadita exitosa")
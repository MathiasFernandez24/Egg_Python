try:
    colores = {"blanco": "white", "verde": "green", "negro": "black"}
    colores["amarillo"]
except KeyError:
    print("Error--> Llave inexistente")
except Exception as e:
    print(type(e))

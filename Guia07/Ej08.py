
try:
    lista = [2, 4, 6, 8, 10]
    lista[10]
except IndexError:
    print("Error--> Indice inexistende")
except Exception as e:
    print(type(e))

monedas = {"Euro": "€", "Dólar": "$", "Yen": "¥"}

moneda_usuario = input("nombre de moneda: ")
respuesta = monedas.get(moneda_usuario)
if (respuesta != None):
    print("El Logo de su moneda es: ", respuesta)
else:
    print("No existe esa moneda en mi base de datos")

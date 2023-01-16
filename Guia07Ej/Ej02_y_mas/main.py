import funciones_mathi as f

while True:
    print("""puedes elegir una funcion: 
a- área_rectángulo
b- área_círculo
c- relación
d- intermedio
e- recortar
f- separar
g- tiempo
exit- salir
""")

    opcion = input("opcion: ").lower()
    if opcion=="a":
        f.area_rectangulo(f.inputcito(),f.inputcito())
    elif opcion=="b":
        f.area_circulo(f.inputcito())
    elif opcion== "c":
        f.relacion(f.inputcito(),f.inputcito())
    elif opcion== "d":
        f.intermedio(f.inputcito(),f.inputcito())
    elif opcion=="e":
        f.recortar(f.inputcito(),f.inputcito(),f.inputcito())
    elif opcion=="f":
        numeros=[]
        print("Cantidad de valores a agregar: ")
        cantidad_valores= f.inputcito()
        for i in range(cantidad_valores):
            print("valor", i+1, "-->")
            numeros.append(f.inputcito())
        f.separar(*numeros)
    elif opcion=="g":
        f.tiempo(f.inputcito(),f.inputcito(),f.inputcito())

    elif opcion=="exit":
        break




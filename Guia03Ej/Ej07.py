anio_1 = int(input("Primer Año: "))
anio_2 = int(input("Segundo Año: "))

for anio in range(anio_1, anio_2):
    validacion_01 = anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)
    if validacion_01 == True:
        print(f"{anio} es Bisciestro")

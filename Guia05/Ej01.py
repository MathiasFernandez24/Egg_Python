mi_diccionario = {
    "sal": 10.50,
    "pan": 20.00,
    "leche": 25.25,
    6: "Maira"
}
print(mi_diccionario)
print(type(mi_diccionario))


mi_diccionario_2 = dict(sal=20, pan=40, leche=35.25)
print(mi_diccionario_2)
print(type(mi_diccionario_2))

print(mi_diccionario[6])
print(mi_diccionario_2["leche"])

mi_diccionario[6] = "Mathi"
print(mi_diccionario[6])

mi_diccionario["jamon"] = "queso"
print(mi_diccionario)

del mi_diccionario["pan"]
print(mi_diccionario)

a, b, c, d = mi_diccionario
print(a, b, c, d)

mi_diccionario_3 = {**mi_diccionario, **mi_diccionario_2}

print("--->", mi_diccionario)
print("--->", mi_diccionario_2)
print("--->", mi_diccionario_3)

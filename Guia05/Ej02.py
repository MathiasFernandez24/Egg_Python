diccionario = {
    "nombre": "Mathi",
    "edad": "29",
    "apellido": "Fernandez",
}
diccionario2 = {
    "n": "M",
    "a": "F",
    "e": "2"
}
nom = diccionario.get("nombre")
print(diccionario)


diccionario.update({"nombre": "Mai"})
print(diccionario)

diccionario.popitem()
print(diccionario)

print(diccionario.setdefault("nombraae", "a ver"))
print(diccionario)

alfabeto = "abcdefghijklmnñopqrstuvwxyz"
mensaje = input("Ingrese mensaje paracodificar: ").lower()
codificacion = int(input("Indice codificacion: "))
mensaje_codificado = ""
for letra in mensaje:
    aux = (alfabeto.find(letra) + codificacion) % 27
    mensaje_codificado += alfabeto[aux]
print(mensaje_codificado)

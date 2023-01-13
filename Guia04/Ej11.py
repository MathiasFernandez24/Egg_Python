conjunto = {1, 2}
conjunto.add(3)  # agrega al final
print(conjunto)

conjunto2 = conjunto.copy()
print(conjunto2)
conjunto.clear()
print(conjunto)


datos1 = (1, 2, 3)
datos2 = {4, 5, 6}
datos3 = [7, 8, 9]

conjunto.update(datos1)
conjunto.update(datos2)
conjunto.update(datos3)
print(conjunto)

b = conjunto.pop()  # puede retornar el elemento eliminado
print(b)
print(conjunto)

c = conjunto.discard(55)
print(c)
print(conjunto)

aa = {1, 2, 3}
bb = {3, 2, 8, 9, 10, 15}
x = aa & bb
print(x)

y = aa | bb
print(y)

z = bb-aa
print(z)

w = aa ^ bb
print(w)

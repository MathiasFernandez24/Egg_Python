# sis = ("Windows", "Linux", "Mac")
# texto = "-".join(sis)
# print(texto)

sis1 = ["Windows", "Linux", "Mac"]
# texto1 = "-".join(sis1)
# print(texto1)

# sis2 = {"Windows", "Linux", "Mac"}
# texto2 = "-".join(sis2)
# print(texto2)

# sis3 = {"Windows": "ok", "Linux": "bueno", "Mac": "millo"}
# texto3 = "-".join(sis3)
# print(texto3)

# lista = texto.split("-")
# print(lista)

# sis4 = {"Windows": "ok", "Linux": "bueno", "Mac": "millo"}
# print("bueno" in sis4["Linux"])

# for i in range(len(sis1)):
#     print(i)

# for aux in sis1:
#     print(aux)

# for i, v in enumerate(sis1):
#     print(i, "-> ", v)

conjunto = {(1, 2), (4, 5), (6, 7), (2, 3)}
for x in conjunto:
    multiplicacion = x[0]*2
    cuadrado = x[1]**2
    print(cuadrado, multiplicacion)

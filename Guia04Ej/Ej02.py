lista_1 = [1, 12, 123]
lista_2 = ["Bye", "Ciao", "Agur", "Adieu"]

lista_1.extend([1234, "hola"])
print(f"a-> {lista_1}")

lista_2.extend(["chao", 4321])
print("b-> ", lista_2)

lista_3 = lista_1.copy()
lista_3.pop()
print("c-> ", lista_3)

lista_4 = lista_2
print(f"d-> {lista_4}")


# lista_4 = lista_2[1:len(lista_2)-1]
# print(f"d-> {lista_4}")

edad = int(input("Edad? "))
sexo = input("Sexo? ")

if (sexo == "m" and edad > 65) or (sexo == "f" and edad > 60):
    print("Le corresponde beneficio de jubilacion1")

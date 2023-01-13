var_1_global = 100
var_2_global = [200]


def sumarUno(numero):
    numero.append(2)


sumarUno(var_2_global)
print(var_2_global)

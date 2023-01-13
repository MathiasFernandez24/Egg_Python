usuario = input("Nombre: ")
password = input("Password: ")
password_02 = input("Repetir Password: ")
print("-----------")

validacion_01 = len(usuario) > 5
validacion_02 = not usuario[0].isdigit()
validacion_03 = len(password) < 4
validacion_04 = password == password_02
validacion_formulario = True

if not validacion_01:
    print("El nombre debe ser mayor a 5 caracteres")
    validacion_formulario = False
if not validacion_02:
    print("La primer letra del nombre no puede ser un numero")
    validacion_formulario = False
if not validacion_03:
    print("Password debe ser menor a 4 caracteres")
    validacion_formulario = False
if not validacion_04:
    print("No coinciden las Passwords ingresadas")
    validacion_formulario = False
if validacion_formulario == True:
    print("Formulario Exitoso")
else:
    print("Formulario Invalido")

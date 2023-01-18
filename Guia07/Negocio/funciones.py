# def crear_articulo(carrito):
#     while True:
#         try:
#             codigo = int(input("Ingrese Codigo: "))
#             if not codigo in carrito:
#                 if codigo > 0 and codigo<1000000:
#                     break
#             else:
#                 print(f"el codigo {codigo} ya está registrado")
#         except Exception as e:
#             print("     --debe ser un numero entre 0 y 1.000.000")
#     while True:
#         nombre = input("Ingrese Nombre: ")
#         if len(nombre)>=3 and len(nombre)<=100 and nombre.isdigit() == False:
#             break

#     while True:
#         try:
#             precio = float(input("Ingrese Precio: "))
#             if precio>0:
#                 break
#         except Exception as e:
#             print("     --debe ser un numero--")

#     while True:
#         try:
#             cantidad = int(input("Ingrese Cantidad: "))
#             if cantidad > 0 and cantidad<1000000:
#                 break
#         except Exception as e:
#             print("     --debe ser un numero entre 0 y 1.000.000--")
#     valor={
#         "nombre": nombre,
#         "precio":precio,
#         "cantidad": cantidad
#     }
    

#     return codigo,valor
    

#Corregir los errores sintácticos del siguiente programa:


# contraseña = input('Introduce la contraseña: ')
# if contraseña in ['sesamo']:
#   print('Pasa')
# else:
#   print('No pasa')



# Detectar y corregir los errores del siguiente programa que aplica el iva a una factura:

# def aplica_iva(base, iva = 0.18):
#     base = base * iva   
#     return base 
# base = int(input('Introduce la base imponible de la factura: '))
# print(aplica_iva(base))


# Detectar y corregir los errores del siguiente programa que calcula el producto escalar de dos 
# vectores:

# u = [1, 2, 3]
# v = [4, 5, 6]
# lista=[]
# def producto_escalar(u, v):
#     for i in range(len(u)):
#         lista.append(u[i]*v[i])
#     return sum(lista)
# print(producto_escalar(u, v))


# Detectar y corregir los errores del siguiente programa que devuelve y elimina el teléfono de un 
# listín telefónico a través del nombre del usuario:

# listin = {'Juan':123456789, 'Pedro':987654321}
# def elimina(listin, usuario):
#     if usuario in listin:
#         del listin[usuario]
#         return listin[usuario]
#     else:
#         print('La persona no se encuentra en la lista')
# print(elimina(listin, 'Pablo'))


# Detectar y corregir los errores del siguiente programa que multiplica dos matrices:

# a = ((1, 2, 3),
#      (3, 2, 1))
# b = ((1, 2),
#      (3, 4),
#      (5, 6))
# def producto(a, b):
#     producto = []
#     for i in range(len(a)):#3
#         fila = []
#         for j in range(len(b[0])):#3
#             suma = 0
#             for k in range(len(a[0])):
#                 suma += a[i][k] * b[k][j]
#             fila.append(suma)
#         producto.append(tuple(fila))
#     return tuple(producto)
# print(producto(a, b))
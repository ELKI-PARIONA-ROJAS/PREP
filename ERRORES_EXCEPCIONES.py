# Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el 
# programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:

# m=int(input('Escriba el numerador: '))
# n=int(input('Escriba el denominador: '))
# try:
#     resultado = m/n
# except ZeroDivisionError:
#     print('El denominador no puede ser un 0')
# else:
#     print('El resultado es %s' % (resultado))


# Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el 
# programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:

# lista = [1, 2, 3, 4, 5]
# i=int(input('Escriba el indice de la lista: '))
# try:
#     lista[i]
# except IndexError:
#     print('Se debe ocupar un indice de acuerdo a la lista')
# else:
#     print('El elemento con el indice %s es %s' % (i,lista[i]))


# Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el 
# programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:

# colores = { 'rojo':'red', 'verde':'green', 'negro':'black' }
# i=input('Escriba el indice del diccionario: ') 
# try:
#     colores[i]
# except KeyError:
#     print('Debe introducir una clave que se encuentre en el diccionario')
# else:
#     print('El valor de la clave %s en el diccionario es %s' % (i,colores[i]))


# Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el 
# programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:

# try:
#     resultado = 15 + '20'
# except TypeError:
#     print('Debe introducir valores numéricos')
# else:
#     print(resultado)


# Realiza una función llamada agregar_una_vez(lista, el) que reciba una lista y un elemento. 
# La función debe añadir el elemento al final de la lista con la condición de no repetir ningún 
# elemento. Además si este elemento ya se encuentra en la lista se debe invocar un error de tipo 
# ValueError que debes capturar y mostrar este mensaje en su lugar:

#Error: Imposible añadir elementos duplicados => [elemento].

# Cuando tengas la función intenta añadir los siguiente valores a la lista 10, -2, "Hola" y luego 
# muestra su contenido.
# Puedes utilizar la sintaxis "elemento in lista"
# import math
# listin = [1, 5, -2]
# def añadir(lista):
#     elemento=int(input('Escribe un elemento que desea agregar: '))
#     if elemento not in lista:
#         lista.append(elemento)
#         print(lista)
#     else:
#         try:
#             math.sqrt(-10)
#         except ValueError:
#             print('ValueError')
#         else:
#             print('Aqui no paso nada')
# añadir(listin)


    
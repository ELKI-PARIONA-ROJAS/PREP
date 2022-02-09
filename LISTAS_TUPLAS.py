# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, 
# Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado 
# en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has 
# sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una 
# de las correspondientes notas introducidas por el usuario.

# cursos=input('Ingrese sus asignaturas: ')
# notas=input('Ingrese su nota: ')
# lista=[]
# relacion=[]
# while True:
#     if cursos !='salir':
#         lista.append(cursos)
#         relacion.append(notas)
#         cursos=input('Ingrese sus asignaturas: ')
#         if cursos=='salir':
#             print('Muchas gracias')
#             break
#         notas=input('Cuanto de nota has sacado: ')
# for i in range(0,len(lista)):
#     print('Yo estudio %s y me saque una nota de %s' % (lista[i],relacion[i]))



# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
# los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

# ganadores=input('Ingrese el código de los ganadores: ')
# lista=[]
# while True:
#     ganadores!='salir'
#     lista.append(int(ganadores))
#     ganadores=input('Ingrese el código de los ganadores: ')
#     if ganadores=='salir':
#         print('Muchas gracias ')
#         break
# print(lista)
# lista.sort()
# print(lista)



# Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por 
# pantalla en orden inverso separados por comas.

# lista=[]
# for i in range(1,10+1):
#     lista.append(i)
# lista=lista[::-1]
# print(lista)



# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, 
# Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado 
# en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe 
# mostrar por pantalla las asignaturas que el usuario tiene que repetir.

# lista=[]
# relacion=[]
# decisión=input('Dese continuar: ')
# while decisión=='si':
#     cursos=input('Ingrese su asignatura: ')
#     notas=int(input('Cuanto de nota ha sacado: '))
#     if notas >= 10:
#         decisión=input('Desea continuar: ')
#         continue
#     elif notas < 10:
#         lista.append(cursos)
#         relacion.append(notas)
#         decisión=input('Desea continuar: ')
# for i in range(0,len(lista)):
#     print('Yo desaprobe %s porque tengo una nota de  %s' % (lista[i],relacion[i]))



# Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras 
# que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

# letras=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# lista=[]
# for i in range(0,len(letras)):
#     if i%3==0:
#         continue
#     elif i%3!=0:
#         lista.append(letras[i])
# print(lista)
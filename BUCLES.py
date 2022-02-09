#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos 
# los números impares desde 1 hasta ese número separados por comas.
# numero=int(input('Escriba un número: '))
# for i in range(numero+1):
#     if i%2!=0:
#         print(i,end=',')

#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la 
#cuenta atrás desde ese número hasta cero separados por comas.

# numero=int(input('Escribe un numero positivo: '))
# lista=[]
# for i in range(numero+1):
#     lista.append(i)
# lista=lista[::-1]
# print(lista)



#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el 
# número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la 
# inversión.

# capital=int(input('Cuanto dinero desea invertir: '))
# tasa=float(input('Cual es la tasa a la que invertirá: '))
# tiempo=int(input('Por cuantos años piensa invertir: '))
# for i in range(1,tiempo+1):
#     monto=capital*(1+tasa)**(i)
#     print('En el año %s tendrá un monto de %s Soles' % (i, round(monto,2)))



# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo 
# rectángulo como el de más abajo, de altura el número introducido.

# num=int(input('Introduce la altura del pino: '))
# for i in range(num+1):
#     print('*'*i)


#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
# for i in range(1,11):
#     print('La tabla de',i,'es: ')
#     for j in range(1,11):
#         if j<10:
#             print(i,'*',j,'=',i*j)
#         elif  j==10:
#             print(i,'*',j,'=',i*j)
#             print()



# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo 
# rectángulo como el de más abajo.

# num=int(input('Introduzca un número: '))
# lista=[]
# for i in range(1,num+1,2):
#     lista.append(i)
#     print(lista)



# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte 
# al usuario por la contraseña hasta que introduzca la contraseña correcta.

# contra='leo.fatima8agosto'
# contraseña=input('Introduzca una contraseña: ')
# while contraseña!=contra:
#     print('Contraseña incorrecta')
#     print('Volver escribir la contraseña')
#     contraseña=input('Introduzca una contraseña: ')
# print('Muy bien encontro la contraseña adecuada')



#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un 
#número primo o no.

# num=int(input('Introducir un numero entero: '))
# if num==1 or num==2:
#     print('Es un número primo')
# else:
#     for i in range(2,num):
#         if num%i==0:
#             print('No es un número primo')
#             break
#         else:
#             print('Es un número primo')
#             break


#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una 
# las letras de la palabra introducida empezando por la última.

# palabra=input('Escriba una palabra: ')
# lista=[]
# for i in palabra:
#     lista.append(i)
# lista=lista[::-1]
# for i in lista:
#     print(i)



#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre 
# por pantalla el número de veces que aparece la letra en la frase.

# frase=input('Escriba una frase: ')#hola queridos amigos
# letra=input('Escriba la letra: ')#s
# lista=[]
# contador=0
# for i in frase:
#     lista.append(i)
# while lista.count(letra)>0:
#     contador+=1
#     indice=lista.index(letra)
#     lista=lista[indice+1:]
# print('El total de veces que apareció la letra en la frase es de %s veces' % (contador))



#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el 
# usuario escriba “salir” que terminará.

# opinion=input('Escriba lo que desee: ')
# while opinion != 'salir':
#     opinion=input('Escriba lo que desee: ')
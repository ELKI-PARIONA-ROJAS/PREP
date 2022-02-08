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

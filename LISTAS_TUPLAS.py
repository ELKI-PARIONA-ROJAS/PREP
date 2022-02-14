# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, 
# Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado 
# en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has 
# sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una 
# de las correspondientes notas introducidas por el usuario.

cursos=input('Ingrese sus asignaturas: ')
notas=input('Ingrese su nota: ')
lista=[]
relacion=[]
while True:
    if cursos !='salir':
        lista.append(cursos)
        relacion.append(notas)
        cursos=input('Ingrese sus asignaturas: ')
        if cursos=='salir':
            print('Muchas gracias')
            break
        notas=input('Cuanto de nota has sacado: ')
for i in range(0,len(lista)):
    print('Yo estudio %s y me saque una nota de %s' % (lista[i],relacion[i]))



# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
# los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

ganadores=input('Ingrese el código de los ganadores: ')
lista=[]
while True:
    ganadores!='salir'
    lista.append(int(ganadores))
    ganadores=input('Ingrese el código de los ganadores: ')
    if ganadores=='salir':
        print('Muchas gracias ')
        break
print(lista)
lista.sort()
print(lista)



# Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por 
# pantalla en orden inverso separados por comas.

lista=[]
for i in range(1,10+1):
    lista.append(i)
lista=lista[::-1]
print(lista)



# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, 
# Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado 
# en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe 
# mostrar por pantalla las asignaturas que el usuario tiene que repetir.

lista=[]
relacion=[]
decisión=input('Dese continuar: ')
while decisión=='si':
    cursos=input('Ingrese su asignatura: ')
    notas=int(input('Cuanto de nota ha sacado: '))
    if notas >= 10:
        decisión=input('Desea continuar: ')
        continue
    elif notas < 10:
        lista.append(cursos)
        relacion.append(notas)
        decisión=input('Desea continuar: ')
for i in range(0,len(lista)):
    print('Yo desaprobe %s porque tengo una nota de  %s' % (lista[i],relacion[i]))



# Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras 
# que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

letras=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lista=[]
for i in range(0,len(letras)):
    if i%3==0:
        continue
    elif i%3!=0:
        lista.append(letras[i])
print(lista)

palabra=input('Introduzca la palabra: ')
lista=[]
for i in palabra:
    lista.append(i)
if len(lista)%2==0:
    num=len(lista)/2
    num=int(num)
    p1=lista[:num]
    print(p1)
    p2=lista[num:]
    p2=p2[::-1]
    print(p2)
    if p1==p2:
        print('es una palabra palíndroma')
    else:
        print('No es una palabra palíndroma')
elif len(lista)%2!=0:
    num=(len(lista)-1)/2
    num=int(num)
    p1=lista[:num]
    print(p1)
    p2=lista[num+1:]
    p2=p2[::-1]
    print(p2)
    if p1==p2:
        print('es una palabra palíndroma')
    else:
        print('No es una palabra palíndroma')



#Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces 
# que contiene cada vocal.

palabra=input('Escriba la palabra que desea: ')
palabra=palabra.lower()
lista=[]
for i in palabra:
    lista.append(i)
vocales=['a','e','i','o','u']
for i in vocales:
    print('El numero de veces que esta la vocal %s es de %s veces' % (i, lista.count(i)))



#Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 
# 65, 8, y muestre por pantalla el menor y el mayor de los precios.

lista=[50,75,46,22,80,65,8]
mayor=max(lista)
menor=min(lista)
print('El número mayor es %s y el número menor es %s' % (mayor, menor))



# Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre 
# por pantalla su producto escalar.

l1=[1,2,3]
l2=[-1,0,2]
lista=[]
for i in range(3):
    n=l1[i]*l2[i]
    lista.append(n)
print(lista)



# Escribir un programa que almacene las matrices en una lista y muestre por pantalla su producto.
# Para representar matrices mediante listas usar listas anidadas, representando cada vector fila 
# en una lista.

A=(1,2,5,8,5)
B=list(A)
print(B)



#Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde 
# en una lista y muestre por pantalla su media y desviación típica.

lista=[]
x=True
while x:
    n=int(input('introduce un numero: '))
    lista.append(n)
    x=input('Desea continuar con la operación: ')
    if x=='si':
        pass
    elif x=='no':
        x=False
print(lista)
suma=0
contador=0
for i in lista:
    contador+=1
    suma=+i 
promedio=suma/contador
sumatoria=0
for i in lista:
    m=(i-promedio)**2
    sumatoria=+m
varianza=sumatoria/contador
print('El promedio es %s y la varianza es %s' % (promedio,varianza))
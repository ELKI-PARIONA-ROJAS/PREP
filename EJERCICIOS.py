#Calcular la suma de los divisores de un número:
# numero=int(input('Escribe un numero natural entero positivo: '))
# suma=0
# for i in range(1,numero):
#     if numero%i==0:
#         suma+=i
#     elif numero%i!=0:
#         None
# print(suma)


#Cuales son y cuantos son los números primos comprendidos entre 1 y 1000:

# l_s=int(input('Escribe el límite superior: '))
# l_i=int(input('escribe el limite inferior: '))
# lista_primos=[]
# for i in range(l_i+1,l_s+1):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         lista_primos.append(i)
# print(lista_primos)


# Aproximar el valor de una exponencial dado un error minimo permitido
# def factorial(n):
#     x=n
#     y=1
#     while x>0:
#         y*=x
#         x-=1
#     return y
# x=int(input('Escriba la potencia de la función: '))
# e_1=1+x
# c=2
# while True:
#     if (x**(c)/factorial(c))>=0.00001:
#         e_1+=(x**(c)/factorial(c))
#         c+=1
#     else:
#         break
# print(e_1)


# Calcula el resultado de una progresión racional con signos intercambiados:

# def par(n):
#     if n%2==0:
#         return True
#     else:
#         return False
# n=int(input('Escribe el número: '))
# resultado=1
# c=2
# pares=2
# impares=3
# while c<= n:
#     if par(c):
#         resultado-=(1/(pares))
#         pares+=2
#     else:
#         resultado+=(1/(impares))
#         impares+=2
#     c+=1
# print(resultado)


# Invertir los digitos de un numero

# num=input('Ingresar un numero: ')
# lista=list(num)
# lista2=lista[::-1]
# cadena=''.join(lista2)
# print(cadena)


#Elaborar un algoritmo que devuelva el numero de ceros que tiene el número

# n=input('Escribe un número: ')
# num=list(n)
# cant=num.count('0')
# print('El número tiene %s ceros' % (cant))


# Determine de un conjunto de de n número ingresados cual es mayor o el menor

# N=int(input('Escriba cuantos numeros desea ingresar: '))
# lista_num=[]
# for i in range(N):
#     num=int(input('Escriba el numero que desea añadir: '))
#     lista_num.append(num)
# print('El número máximo es %s' % (max(lista_num)))
# print('El número mínimo es %s' % (min(lista_num)))


# Ingresar 50 caracteres e indicar cuantas vees se repite el caracter 'a'

# lista_valores=[]
# for i in range(50):
#     valor=input('Escriba un caracter: ')
#     lista_valores.append(valor)
# repetidas=lista_valores.count('a')
# print("El valor 'a' fue repetido %s veces" % (repetidas))


# Mostrar los 10 primero número pares junto con su potencia de 3

# lista_pares=[]
# lista_cubos=[]
# for i in range(1,20+1):
#     if i%2==0:
#         lista_pares.append(i)
#         lista_cubos.append(i**3)
#     else:
#         None
# print(lista_cubos)
# print(lista_pares)


# En una empresa con N empleados en donde se ingresa como dato el numero de orfen y el sueldo de cada 
# empleado, debe imprimirse el sueldo mayor junto con su numero de orden

# list_orden=[]
# lista_sueldo=[]
# n=int(input('Escribe cuantos empleados tiene: '))
# for i in range(1,n+1):
#     sueldo=int(input('Escribe el sueldo del empleado N°%s: ' %(i)))
#     lista_sueldo.append(sueldo)
# diccionario={}
# for i in lista_sueldo:
#     diccionario[i]=lista_sueldo.index(i)+1
# print(diccionario)

# Ahora asignarle un nombre a cada empleado
# diccionario={}
# num=int(input('Escribe cuantos empleados desea tener: '))
# for i in range(num):
#     clave=input('Escriba el nombre del empleado: ')
#     valor=int(input('Escribe el sueldo del empleado %s: ' % (clave)))
#     diccionario.setdefault(clave,valor)
# print(diccionario)


#hallar cuantos son superiores a la media de los valores

# lista_temperturas=[]
# n=int(input('Escriba el total de temperaturas: '))
# sumador=0
# for i in range(n):
#     valor=int(input('Escribe la temperatura del ambiente: '))
#     sumador+=valor
#     lista_temperturas.append(valor)
# promedio=sumador/n
# lista_mayores=[]
# c=0
# for i in lista_temperturas:
#     if i>=promedio:
#         lista_mayores.append(i)
#         c+=1
#     else:
#         None
# print(lista_mayores)
# print('El total de valores que superan al promedio es de: ', c)


# valores ordenados y no repetidos

# vector=[2,5,8,6,8,5,3,2,2,4,7,0,6,4,3,2,12,3,8]
# unicos=[]
# for i in vector:
#     if i not in unicos:
#         unicos.append(i)
# lista_m=unicos.sort()
# print(unicos)


# Sumar matrices de dos dimensiones

# A=[1,2,3,2,7,8]
# B=[3,4,8,2,1,0]
# suma=[]
# if len(A)==len(B):
#     for i in range(len(A)):
#         s=A[i]+B[i]
#         suma.append(s)
# print(suma)


# los registros de ventas de una empresa estan estructurados de la siguiente manera

# m=int(input('ingrese el total de años que opera la empresa: '))
# n=int(input('Ingrese el total de sucursales de la empresa: '))
# matriz=[]
# for i in range(m):
#     matriz.append([])
#     for j in range(n):
#         venta=int(input('Ingrese la venta para el año %s en la sucursal %s: ' % (i+1,j+1)))
#         matriz[i].append(venta)
# print(matriz)

# Hallar la sucursal que mas vendió
# max=0
# for j in range(n):
#     suma=0
#     for i in range(m):
#         suma+=matriz[i][j]
#         if suma>max:
#             max=suma
#             sucesion=j+1
# print('Sucursal que mas vendio es: ', sucesion)

# Hallar el promedio de ventas por año
# max=0
# for i in range(m):
#     suma=0
#     for j in range(n):
#         suma+=matriz[i][j]
#     promedio=suma/n
#     print('Promedio de ventas del año ', i+1,'es',promedio)
#     if promedio>max:
#         max=promedio
#         año=i+1
# print('El año con mayor promedio',año)


# calcular el producto escalar y vectorial de dos vectores de 3 elementos

# v1=3*[0]
# v2=[0]*3
# for i in range(3):
#     v1[i]=int(input('Escribe el elemento N° %s del 1er vector: '%(i+1)))  
# for i in range(3):
#     v2[i]=int(input('Escribe el elemento N° %s del 2do vector: '%(i+1))) 
# print(v1)
# print(v2)

# suma=0
# for i in range(3):
#     p=v1[i]*v2[i]
#     suma+=p
# print('El producto escalar es %s'%(suma))

# x=v1[1]*v2[2]-v1[2]*v2[1]
# y=-(v1[0]*v2[2]-v1[2]*v2[0])
# z=v1[0]*v2[1]-v1[1]*v2[0]
# prod_vector=[x,y,z]
# print(prod_vector)


# Revierta una lista sin utilizar otra lista

# cantidad=int(input('Ingrese la cantidad de elementos que desea: '))
# n=['']*cantidad
# for i in range(cantidad):
#     n[i]=input('Escribe el elemento que desea: ')
# n=n[::-1]
# for i in range(cantidad):
#     print(n[i])


# Ejecute la criba de Erastótenes a travéz de un algoritmo:

# numeros=[]
# for i in range(1,101):
#     numeros.append(i)
# booleanos=[True]*100
# booleanos[0]=False
# for i in range(1,99):
#     for j in range(i+1,100):
#         if numeros[j]%numeros[i]==0:
#             booleanos[j]=0
# for i in range(100):
#     if booleanos[i]:
#         print(numeros[i])



# Realizar un algoritmo que maneje un vector de enteros a travéz de un menú con seis opciones:


# class Directorio:
#     def __init__(self, lista):
#         self.lista=lista
#     def añadir(self, elemento):
#         self.lista.append(elemento)
#     def eliminar(self,elemento):
#         self.lista.remove(elemento)
#     def mostrar(self):
#         return self.lista
#     def contar(self,elemento):
#         return self.lista.count(elemento)
#     def media_max(self):
#         suma=0
#         conta=0
#         for i in self.lista:
#             suma+=i
#             conta+=1
#         promedio=suma/conta
#         maximo=max(self.lista)
#         return maximo, promedio
# listin=[3,5,7,8,2,3,5,6,7,3]
# iterables1=Directorio(listin)
#iterables1.añadir(100)
#iterables1.eliminar(5)
#print(iterables1.contar(7))
#print(iterables1.mostrar())
#print(iterables1.media_max())

    








































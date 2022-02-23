# Escribir una función que muestre por pantalla el saludo ¡Hola amiga! cada vez que se la invoque.

def imprimir():
    print('¡Hola amiga!')
imprimir()



# Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo 
# ¡hola <nombre>!.

def imp(nombre):
    print('Su nombre es: ', nombre)
imp('elki')



#Escribir una función que reciba un número entero positivo y devuelva su factorial.

def factorial(num):
    a=num
    b=1
    while a>0: 
        b*=a
        a-=1
    return b

print(factorial(5))


# Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir
#  la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca 
# la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

def calc(monto, impuesto):
    con_igv=monto*(1+impuesto)
    return con_igv
print(calc(1000,0.18))


# Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro 
# usando la primera función.

import math
def area(radio):
    result=round(math.pi*(radio**2),2)
    return result
def volumen(altura,radio):
    volumen=area(radio)*altura
    return volumen
print(volumen(1,1))


# Escribir una función que reciba una muestra de números en una lista y devuelva su media.

def promedio(lista):
    suma=0
    contador=0
    for i in lista:
        suma+=i
        contador+=1
    return round(suma/contador,2)
listado=[1,2,4,6,7,54,9]
print(promedio(listado))


# Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus
#  cuadrados.

def list_cua(lista1):
    lista2=[]
    for i in lista1:
        a=i**2
        lista2.append(a)
    return lista2
listado=[2,5,6,2,3,4,9]
print(listado)


# Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su 
# media, varianza y desviación típica. 

def datos(lista):
    suma=0
    contador=0
    for i in lista:
        suma+=i
        contador+=1
    media=round(suma/contador,2)
    lista2=[]
    for i in lista:
        n=((i-media)**2)/contador
        lista2.append(n)
    print(lista2)
    sum2=0
    cont2=0
    for i in lista2:
        sum2+=i
        cont2+=1
    varianza=round(sum2/cont2,2)
    desviacion_t=round((varianza)**(0.5),2)
    lista3=[media, varianza, desviacion_t]
    nombres=['media','varianza','desviacion_tipica']
    diccionario=dict(zip(nombres,lista3))
    return diccionario
listasa=[23,34,6,23,2,35,3,6,7,75,45,23,42]
print(datos(listasa))


# Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.

def maximocomundivisor(a,b):
    while b!=0:
        a,b=b,a%b
    return a
print(maximocomundivisor(3,12))

def minimocomunmultiplo(a,b):
    return a*b//maximocomundivisor(a,b)
print(minimocomunmultiplo(3,12))

# Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.


def binariotodecimal(binario):
    lista_b=str(binario)
    lista_c=list(lista_b)
    decimal=0
    for i in lista_c:
        decimal=decimal*2+int(i)
    return decimal
print(binariotodecimal(1001001))

def decimaltobinario(decimal):
    binario=''
    while decimal>0:
        binario=str(decimal%2)+binario
        decimal=decimal//2
    return binario
print(decimaltobinario(16))

# Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene 
# y su frecuencia. 
# Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la 
# palabra más repetida y su frecuencia.

def count_words(text):
    text = text.split()#lista
    words = {}
    for i in text:#va recorrer en esta lista
        if i in words:
            words[i] += 1
        else:
            words[i] = 1
    return words
def most_repeated(words):
    max_word = ''
    max_freq = 0
    for word, freq in words.items():
        if freq > max_freq:
            max_word = word
            max_freq = freq
    return max_word, max_freq
text = 'Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera'
print(count_words(text))
print(most_repeated(count_words(text)))


def minerales(*elementos):
    print('En el perú tenemos minerales como el: ', end='')
    for i in elementos:
        print(i, end=', ')
    return
print(minerales('cobre','oro','plata','hierro','zinc','estaño','plomo','uranio','litio'))
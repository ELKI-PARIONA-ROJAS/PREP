# Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con el nombre 
# tabla-n.txt la tabla de multiplicar de ese número, done n es el número introducido.

# num=int(input('Escribe la tabla de multipicar del numero que deseas: '))
# nombre_del_archivo='tabla del '+ str(num)+'.txt'
# f=open(nombre_del_archivo,'w')
# for i in range(1,11):
#     f.write('->'+str(i)+'*'+str(num)+'='+str(i*num)+'\n')
# f.close()



# Escribir una función que pida un número entero entre 1 y 10, lea el fichero tabla-n.txt con la tabla 
# de multiplicar de ese número, done n es el número introducido, y la muestre por pantalla. Si el 
# fichero no existe debe mostrar un mensaje por pantalla informando de ello.

# num=int(input('Escribe la tabla de multipicar del numero que deseas: '))
# nombre_del_archivo='tabla del '+ str(num)+'.txt'
# try:
#     f=open(nombre_del_archivo,'r')
# except FileNotFoundError:
#     print('Este archivo no pudimos encontrarlo')
# else:
#     print(f.read())



# Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero tabla-n.txt con la tabla 
# de multiplicar de ese número, y muestre por pantalla la línea m del fichero. Si el fichero no existe 
# debe mostrar un mensaje por pantalla informando de ello.

# n=int(input('Escribir el multiplicando1: '))
# m=int(input('Escribir el multiplicando2: '))
# nombre_del_archivo='tabla del '+ str(n)+'.txt'
# try:
#     f=open(nombre_del_archivo,'r')
# except FileNotFoundError:
#     print('Este archivo no pudimos encontrarlo')
# else:
#     lines=f.readlines()
#     print(lines[m-1])



# Escribir un programa que acceda a un fichero de internet mediante su url y muestre por pantalla el 
# número de palabras que contiene.

# def import_lib(url):
#     from urllib import request
#     from urllib.error import URLError
#     try:
#         f=request.urlopen(url)
#     except URLError:
#         print('No se pudo encontrar el archivo en la nube')
#     else:
#         lista=f.read()
#         return len(lista.split())

# print(import_lib('https://www.gutenberg.org/files/2000/2000-0.txt'))
# print(import_lib('https://no-existe.txt'))



# Escribir un programa que abra el fichero con información sobre el PIB per cápita de los países de la 
# Unión Europea 
# (url:https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true)
# , pregunte por las iniciales de un país y muestre el PIB per cápita de ese país de todos los años 
# disponibles.

# def import_data(url,pais):
#     from urllib import request
#     from urllib.error import URLError
#     try:
#         f=request.urlopen(url)
#     except URLError:
#         print('El archivo no existe')
#     else:
#         datos=f.read().decode('utf-8').split('\n')
#         datos=[i.split('\t') for i in datos]
#         datos=[list(map(str.strip,i)) for i in datos]
#         for i in datos:
#             i[0]=i[0].split(',')[-1]
#         datos[0][0]='años'
#         datos={i[0]:i[1:] for i in datos}
#         resultado={datos['años'][i]:datos[pais][i] for i in range(len(datos['años']))}
#         return resultado
# pais=input('Escribe el pais del que quieres los datos: ')
# print('Esta es la relacion de pbi/per-capita de %s' % (pais))
# for años, pbi in import_data('https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true',pais).items():
#     print(años,'\t',pbi)



# Escribir un programa para gestionar un listín telefónico con los nombres y los teléfonos de los clientes 
# de una empresa. El programa incorporar funciones crear el fichero con el listín si no existe, para 
# consultar el teléfono de un cliente, añadir el teléfono de un nuevo cliente y eliminar el teléfono de un 
# cliente. El listín debe estar guardado en el fichero de texto listin.txt donde el nombre del cliente y su 
# teléfono deben aparecer separados por comas y cada cliente en una línea distinta.

#funcion que devuelve el telefono de un cliente:

# def obt_telefono(file,cliente):
#     try:
#         f=open(file,'r')
#     except FileNotFoundError:
#         print('El archivo no se encuentra en el repo')
#     else:
#         registro=f.readlines()
#         f.close()
#         registro=dict([tuple(line.split(',')) for line in registro])
#         if cliente in registro:
#             return registro[cliente]
#         else:
#             return('El cliente %s no se encuentra registrado', (cliente))
# def agregar_fono(file, cliente, fono):
#     try:
#         f=open(file,'a')
#     except FileNotFoundError:
#         print('El archivo no se encuentra en el repo')
#     else:
#         f.write(cliente + ',' + fono +'\n')
#         f.close()
#         return('El telefono se ha añadido. \n')
# def borrar_fono(file, cliente):
#     try: 
#         f=open(file,'r')
#     except FileNotFoundError:
#         print('No se pudo encontrar el archivo')
#     else:
#         registro=f.readlines()
#         f.close()
#         registro=dict([tuple(line.split(',')) for line in registro])
#         if cliente in registro:
#             del registro[cliente]
#             f=open(file,'w')
#             for nombre, telefono in registro.items():
#                 f.write(nombre+','+telefono)
#             f.close()
#             return('El cliente se ha borrado!\n')
#         else:
#             return('El clinte '+cliente+' no existe')
# def crear_directorio(file):
#     import os
#     if os.path.isfile(file):
#         respuesta=input('El fichero '+file+' ya existe, desea vaciarlo?: ')
#         if respuesta=='N':
#             return 'Nose ha creado el fichero porque ya existe'
#     f=open(file,'w')
#     f.close()
#     return 'Se ha creado el fichero. \n'
# def menu():
#     print('Gestion del directorio telefonico')
#     print('=================================')
#     print('1. Consultar un telefono')
#     print('2. Añadir un telefono')
#     print('3. Eliminar un telefono')
#     print('4. Crear un listin')
#     print('0. Terminar')
#     option = input('Escriba el número de opcion deseado: ')
#     return option
# def directory():
#     file='listin.txt'
#     while True:
#         option = menu()
#         if option == '1':
#             cliente=input('Introduce el nombre del cliente: ')
#             print(obt_telefono(file,cliente))
#         elif option =='2':
#             cliente=input('Escribe el nombre del cliente: ')
#             fono=input('Escribe su numero de telefono: ')
#             print(agregar_fono(file,cliente,fono))
#         elif option =='3':
#             cliente=input('Escribe el nombre del cliente: ')
#             print(borrar_fono(file,cliente))
#         elif option =='4':
#             print(crear_directorio(file))
#         else:
#             break
#     return
# directory()



# El fichero cotizacion.csv contiene las cotizaciones de las empresas del IBEX35 con las siguientes 
# columnas: Nombre (nombre de la empresa), Final (precio de la acción al cierre de bolsa), 
# Máximo (precio máximo de la acción durante la jornada), Mínimo (precio mínimo de la acción durante 
# la jornada), Volumen (Volumen al cierre de bolsa), Efectivo (capitalización al cierre en miles de euros).

# Construir una función reciba el fichero de cotizaciones y devuelva un diccionario con los datos del 
# fichero por columnas.

# Construir una función que reciba el diccionario devuelto por la función anterior y cree un fichero en 
# formato csv con el mínimo, el máximo y la media de dada columna.


def protocolo(numero):
    numero=numero.replace('.','')
    numero=numero.replace(',','.')
    return float(numero)

def proceso1(file):
    try:
        f=open(file,'r')
    except FileNotFoundError:
        print('El documento no pudo ser encontrado')
        return

    lineas=f.readlines()#divide en listas de lineas 
    f.close()#cierra el documento
    claves=lineas[0]#establece al primer elem. como las claves
    claves=claves[:-1].split(';')#divide a las claves por ;
    cotizaciones={}#crea un diccionario
    for i in claves:#recorre a las claves
        cotizaciones[i]=[]#le da las llaves de claves al diccionario
    for linea in lineas[1:]:#recorre las lineas de datos menos el primero(claves)
        linea=linea[:-1].split(';')#divide los datos por;
        cotizaciones[claves[0]].append(linea[0])#asigna a la clave nombre el valor de nombre de empresas
        for i in range(1,len(cotizaciones)):# recorre el rango de elementos 
            cotizaciones[claves[i]].append(protocolo(linea[i]))# asigna a cada una de las llaves en el diccionario los valores de los datos
    return cotizaciones

def resumen_cotizacion(cotizaciones,file):
    del(cotizaciones['Nombre'])
    f=open(file,'w')
    f.write('Nombre')
    for clave in cotizaciones.keys():
        f.write(';'+clave)
    f.write('\nMinimo')
    for valores in cotizaciones.values():
        f.write(';'+str(min(valores)))
    f.write('\nMaximo')
    for valores in cotizaciones.values():
        f.write(';'+str(max(valores)))
    f.write('\nMedia')
    for valores in cotizaciones.values():
        f.write(';'+str(sum(valores)/len(valores)))
    f.close()
    return

cotizaciones=proceso1('cotizacion.csv')
resumen_cotizacion(cotizaciones,'resumen-cotizacion.csv')  






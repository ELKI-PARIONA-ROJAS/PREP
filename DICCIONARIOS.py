# Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 
# 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si 
# la divisa no está en el diccionario.

# diccionario={'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
# clave=input('Escribir la divisa que desea usar: ')
# print(diccionario.setdefault(clave,'La divisa no esta en el diccionario'))

# diccionario={'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
# clave=input('Escribir la divisa que desea usar: ')
# print(diccionario.setdefault(clave,'La divisa no esta en el diccionario'))



# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde
#  en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, 
# vive en <dirección> y su número de teléfono es <teléfono>.

# diccionario={}
# lista=['nombre','apellido','celular']
# for i in lista:
#     print('la clave es', i)
#     valor=input('Escriba el valor de la clave: ')
#     diccionario.setdefault(i,valor)
#     print('valor %s para la clave %s' % (valor,i))
#     print()
# print(diccionario)



# Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
# pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de 
# ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje 
# informando de ello.

# claves=['platano','manzana','pera','naranja']
# cantidad=[]
# precio=[]
# costo=[]
# for i in claves:
#     n=float(input('Escribir el precio de %s: ' % (i)))
#     precio.append(n)
# precio=list(precio)
# print(precio)
# for i in claves:
#     m=float(input('Escribir la cantidad de %s: ' % (i)))
#     cantidad.append(m)
# cantidad=list(cantidad)
# print(cantidad)
# for i in range(len(cantidad)):
#     costo_t=precio[i]*cantidad[i]
#     costo.append(costo_t)
# print(costo)
# datos=zip(precio,cantidad,costo)
# tupla=tuple(datos)
# combi=zip(claves,tupla)
# info=dict(combi)
# print(info)



# Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la 
# misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.

# mes={1:'enero',2:'febrero',3:'marzo',4:'abril',5:'mayo',6:'junio',7:'julio',8:'agosto',9:'setiembre',10:'octube',11:'noviembre',12:'diciembre'}
# fecha=input('Escribe la fecha en formato(dia/mes/año): ')
# ind1=fecha.find('/')
# ind2=fecha.rfind('/')
# d=fecha[0:ind1]
# m1=fecha[ind1+1:ind2]
# m2=mes.get(int(m1))
# a=fecha[ind2+1:]
# print('Hoy es el %s de %s de %s' % (d,m2,a))



# Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso 
# {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura 
# en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del 
# curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.

# num=int(input('Cuantos cursos llevas?: '))
# lista=[]
# for i in range(num):
#     m=input('Escribe los curso que deseas llevar: ')
#     lista.append(m)
# diccionario={}
# suma=0
# for i in lista:
#     ñ=int(input('Escribe los creditos de %s: ' % (i)))
#     suma+=ñ
#     diccionario.setdefault(i,ñ)
# for i in diccionario:
#     print('El curso de %s tiene un total de %s créditos' % (i,diccionario.get(i)))
# print('En total llevaras %s créditos' % (suma))



# Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona 
# (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que
#  se añada un nuevo dato debe imprimirse el contenido del diccionario.

# diccionario={}
# continuar=True
# while continuar:
#     llave=input('Introduce el tipo de dato que deseas agregar: ')
#     valor=input('Introduce el valor para el campo de %s : ' % (llave))
#     diccionario[llave]=valor
#     continuar=input('Deseas continuar?(si/no): ')=='si'
# print(diccionario)



# Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el 
# artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe 
# mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato

# diccionario={}
# costo=0
# continuar=True
# while continuar:
#     abarrote=input('Ingrese el producto que comprará: ')
#     precio=int(input('Ingreso su precio: '))
#     costo+=precio
#     diccionario[abarrote]=precio
#     continuar=input('Desea continuar(si/no): ')=='si'
# print(diccionario)
# print('La suma de todos los productos asciende a %s Soles'%(costo))



# Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras 
# en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa
#  debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará 
# el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin 
# traducir.

# diccionario={'hola':'hi','mis':'my','queridos':'dear','amigos':'friends'}
# claves=diccionario.keys()
# frase=input('Escribe una frase: ')
# separados=frase.split(' ')
# lista=[]
# for i in separados:
#     if i in claves:
#         traducido=diccionario.get(i)
#         lista.append(traducido)
#     else:
#         None
# traducido=' '.join(lista)
# print(traducido)



# Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán 
# en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. 
# El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. 
# Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. 
# Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. 
# Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y 
# la cantidad pendiente de cobro.

# diccionario={}
# suma=0
# continuar=True
# while continuar:
#     operacion=input('Que operacion realizará(añadir/pagar): ')
#     if operacion=='añadir':
#         clave=input('Escriba el numero de factura que desea agregar: ')
#         valor=int(input('Escriba el costo de la factura: '))
#         diccionario[clave]=valor
#         suma+=valor
#     elif operacion=='pagar':
#         clave=input('Escriba el numero de factura que desea eliminar: ')
#         suma-=diccionario[clave]
#         del diccionario[clave]
#     continuar=input('Desea continuar(si/no): ')=='si'
# print('El total de su deuda asciende a %s Soles' % (suma))
# print(diccionario)



# Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se guardarán
#  en un diccionario en el que la clave de cada cliente será su NIF, y el valor será otro diccionario con los datos 
# del cliente (nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el valor True si se trata 
# de un cliente preferente. El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir 
# cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes,
#  (6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:

# Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
# 1) Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
# 2) Preguntar por el NIF del cliente y mostrar sus datos.
# 3) Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
# 4) Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
# 5) Terminar el programa.


# diccionario_g={}
# suma=0
# continuar=True
# lista=['nombre','dirección','teléfono','correo','preferente']
# print('''Las operaciones que puede realizar son:
# 1) Añadir elementos
# 2) Eliminar facturas
# 3) Mostrar cliente
# 4) Listar todos los clientes
# 5) Listar los clientes preferentes
# 6) Terminar la operación''')
# while continuar:
#     operacion=input('Que operacion realizará(1/2/3/4/5/6): ')
#     if operacion=='1':
#         clave=input('Escriba el número de la factura que desea agregar: ')
#         diccionario_e={}
#         for i in lista:
#             valor_e=input('Escribe el/la % s: ' % (i))
#             diccionario_e.setdefault(i,valor_e)
#         diccionario_g[clave]=diccionario_e
#         continuar=input('Desea continuar(si/no): ')=='si'
#     elif operacion=='2':
#         clave=input('Escriba el numero de la factura que desea eliminar: ')
#         del diccionario_g[clave]
#         continuar=input('Desea continuar(si/no): ')=='si'
#     elif operacion=='3':
#         clave=input('Escriba el numero de la factura que desea ver: ')#0002
#         dicci=diccionario_g.get(clave)
#         print('El propietario de esta factura es %s' % (dicci.get('nombre')))
#         continuar=input('Desea continuar(si/no): ')=='si'
#     elif operacion=='4':
#         lista1=diccionario_g.keys()
#         for i in lista1:
#             dic=diccionario_g[i]
#             print('El cliente %s es dueño de la factura N° %s' % (dic.get('nombre'),i))
#         continuar=input('Desea continuar(si/no): ')=='si'
#     elif operacion=='5':
#         lista1=diccionario_g.keys()
#         for i in lista1:
#             dic=diccionario_g[i]
#             x=dic.get('preferente')
#             if x=='si':
#                 print('Es un cliente preferente %s ' % (dic['nombre']))
#             else:
#                 None
#         continuar=input('Desea continuar(si/no): ')=='si'
#     elif operacion=='6':
#         continuar=False



# El directorio de los clientes de una empresa está organizado en una cadena de texto como la de más abajo,
#  donde cada línea contiene la información del nombre, email, teléfono, nif, y el descuento que se le aplica. 
# Las líneas se separan con el carácter de cambio de línea \n y la primera línea contiene los nombres de los 
# campos con la información contenida en el directorio.

# Escribir un programa que genere un diccionario con la información del directorio, donde cada elemento corresponda 
# a un cliente y tenga por clave su nif y por valor otro diccionario con el resto de la información del cliente.
#  Los diccionarios con la información de cada cliente tendrán como claves los nombres de los campos y como valores
#  la información de cada cliente correspondientes a los campos. Es decir, un diccionario como el siguiente


datos_clientes = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

listas_generales=datos_clientes.split('\n')

lista_campos = listas_generales[0].split(';') 

diccionario={}

for i in listas_generales[1:]:
    valores={}
    lista_ind=i.split(';')
    for j in range(1,len(lista_campos)):
        valores[lista_campos[j]]=lista_ind[j]
    diccionario[lista_ind[0]]=valores
print(diccionario)
    







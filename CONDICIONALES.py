# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. 
# Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que 
# tributar o no.

# ingreso=float(input('Ingrese sus ingreso mensuales: '))
# edad=int(input('Ingrese su edad: '))

# if ingreso>1000.00 and edad >16:
#     print('Usted debe pagar sus tributos')
# else:
#     print('Usted no debe pagar ningún tributo')


#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con 
# un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al 
# usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

nombre=input('Introduzca su nombre: ')
sexo=input('Introduzca su sexo: ')
nombre=nombre.upper()
sexo=sexo.upper()
ind_nomb=nombre[0:1]
lista1=['A','B','C','D','E','F','G','H','I','J','K','L','M']
lista2=['N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
if ind_nomb in lista1 and (sexo == 'MUJER' or sexo == 'FEMENINO'):
    print('Pertence al grupo A')
elif ind_nomb in lista2 and (sexo == 'MUJER' or sexo == 'FEMENINO'):
    print('Pertenece al grupo B')
elif ind_nomb in lista2 and (sexo == 'VARON' or sexo == 'MASCULINO'):
    print('Pertenece al grupo A')
elif ind_nomb in lista1 and (sexo == 'VARON' or sexo == 'MASCULINO'):
    print('Pertenece al grupo B')
else:
    print('Error al ejecutar el codigo')





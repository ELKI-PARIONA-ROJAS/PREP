
# Mostrar solo la parte del numero de celular
##nombre=input('Introduzca el telefo con el formato (+XX-XXXXXXXXX-XX): ')
##indice_1=nombre.find('-')
##indice_2=nombre.rfind('-')
##
##n1=nombre[indice_1+1:indice_2]
##
##print(n1)


frase=input('Introducir una frase que llegue al bobo: ')#hola
lista=[]
for i in frase:
    letra=frase[-1]#a , l
    lista[-1]=letra
    cadena=','.join(lista)
print('la frase al volteado seria: ', cadena)

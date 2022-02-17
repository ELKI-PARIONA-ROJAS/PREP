# Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota 
# del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el 
# resultado de la nota y si ha aprobado o no.´

class Alumno:
    def __init__(self, nombre, nota):
        self.nota=nota
        self.nombre=nombre
    def iniciar(self):
        print('El nombre de la persona es %s' % (self.nombre))
        print('La nota que saco %s es de %s puntos' % (self.nota, self.nombre))
    def aprobado(self):
        if self.nota>=10:
            print('%s ha aprobado el curso satisfactoriamiente con %s' % (self.nombre, self.nota))
        elif self.nota <10:
            print('%s ha desaprobado el curso lamentablemente con %s' % (self.nombre, self.nota))
alumno1=Alumno('juan', 15)
alumno2=Alumno('pedro', 7)
alumno1.iniciar()
alumno1.aprobado()
alumno2.iniciar()
alumno2.aprobado()


# Realizar un programa que tenga una clase Persona con las siguientes características. La clase tendrá como
# atributos el nombre y la edad de una persona. Implementar los métodos necesarios para inicializar los 
# atributos, mostrar los datos e indicar si la persona es mayor de edad o no.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
    def mostrar(self):
        print('La persona en cuestión es %s y tiene %s años' % (self.nombre, self.edad)) 
    def adulto(self):
        if self.edad > 30:
            print('%s es una persona mayor de edad' % (self.nombre))
        elif self.edad <= 30:
            print('%s es una persona menor de edad' % (self.nombre))
persona1=Persona('elki', 24)
persona1.mostrar()
persona1.adulto()
        

# Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con los métodos para 
# inicializar los atributos, imprimir el valor del lado con un tamaño mayor y  el tipo de triángulo que es 
# (equilátero, isósceles o escaleno).

class Triangulo:
    def __init__(self, l1, l2, l3):
        self.l1=l1
        self.l2=l2
        self.l3=l3
    def mostrar(self):
        print('El lado 1 es % s' % (self.l1))
        print('El lado 2 es % s' % (self.l2))
        print('El lado 3 es % s' % (self.l3))
    def ladomayor(self, lista):
        lista=[self.l1,self.l2,self.l3]
    def ladomayor(self):
        lista=[self.l1,self.l2,self.l3]
        maximo=max(lista)
        print('El lado mayor es %s' % (maximo))
    def tipo(self):
        if self.l1==self.l2==self.l3:
            print('El triángulo es equilatero')
        elif self.l1==self.l2 or self.l1==self.l3 or self.l2==self.l3:
            print('El triángulo es isosceles')
        elif self.l1!=self.l2!=self.l3:
            print('El triángulo es escaleno')
triangulo1=Triangulo(4,4,4)
triangulo2=Triangulo(7,4,7)
triangulo3=Triangulo(5,6,7)
triangulo1.ladomayor()
triangulo1.tipo()
triangulo2.ladomayor()
triangulo2.tipo()
triangulo3.ladomayor()
triangulo3.tipo()


# Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__.
#  Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir 
# los resultados obtenidos. Llamar a la clase Calculadora.


class Calculadora:
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def suma(self):
        c=self.a+self.b
        print('La suma es: %s' % (c))
    def resta(self):
        c=self.a-self.b
        print('La resta es: %s' % (c))
    def multiplicacion(self):
        c=self.a*self.b
        print('La multiplicacion es: %s' % (c))
    def division(self):
        c=self.a/self.b
        print('La division es: %s' % (round(c,2)))
operacion1=Calculadora(2,6)
operacion1.suma()
operacion1.resta()
operacion1.multiplicacion()
operacion1.division()


# Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono 
# y el email. Además deberá mostrar un menú con las siguientes opciones

# Añadir contacto
# Lista de contactos
# Buscar contacto
# Editar contacto
# Cerrar agenda

class Agenda:
    def __init__(self):
        self.contactos=[]
    def menu(self):
        print()
        menu=[
            ['Agenda Personal'],
            ['1. Añadir contacto','añadir'],
            ['2. Lista de contacto'],
            ['3. Buscar contacto'],
            ['4. Editar contacto'],
            ['5. Cerrar agenda']
        ]
        for i in range(6):
            print(menu[i][0])
        opcion=int(input('Escriba la opción que quiere: '))
        if opcion==1:
            self.añadir()
        elif opcion==2:
            self.lista()
        elif opcion==3:
            self.buscar()
        elif opcion==4:
            self.editar()
        elif opcion==5:
            print('Saliendo del programa')
            exit()
        self.menu()
    def añadir(self):
        nombre=input('Introduzca su nombre: ')
        telefono=input('Escrie su telefono: ')
        correo=input('Escriba su correo: ')
        self.contactos.append({'nombre':nombre,'telefono':telefono,'correo':correo})
    def lista(self):
        if len(self.contactos)==0:
            print('No existen ningun registro')
        else:
            for i in range(len(self.contactos)):
                print(self.contactos[i]['nombre'])
    def buscar(self):
        nombre=input('Escriba el nombre del contacto: ')
        for i in range(len(self.contactos)):
            if nombre==self.contactos[i]['nombre']:
                print('Estos son sus datos')
                print('Nombre: ', self.contactos[i]['nombre'])
                print('Telefono: ', self.contactos[i]['telefono'])
                print('Correo: ', self.contactos[i]['correo'])
                return i
    def editar(self):
        data=self.buscar()
        condition=False
        while condition==False:
            print('1. Nombre')
            print('2. Telefono')
            print('3. Correo')
            print('4. Volver')
            option=int(input('Escriba la funcion: '))
            if option==1:
                nombre=input('Esbriba el nuevo nombre: ')
                self.contactos[data]['nombre']=nombre
            elif option==2:
                telefono=input('Esbriba el nuevo telefono: ')
                self.contactos[data]['telefono']=telefono
            elif option==3:
                correo=input('Esbriba el nuevo correo: ')
                self.contactos[data]['correo']=correo
            elif option==4:
                condition=True
agenda=Agenda()
agenda.menu()


# En un banco tienen clientes que pueden hacer depósitos y extracciones de dinero. El banco requiere también al final del día calcular 
# la cantidad de dinero que se ha depositado.
# Se deberán crear dos clases, la clase cliente y la clase banco. La clase cliente tendrá los atributos nombre y cantidad y los 
# métodos __init__, depositar, extraer, mostrar_total.
# La clase banco tendrá como atributos 3 objetos de la clase cliente y los métodos __init__, operar y deposito_total.

class Banco:
    def __init__(self):
        self.cliente1=Cliente('Elki')
        self.cliente2=Cliente('Ivan')
        self.cliente3=Cliente('Juan')
    def operacion(self):
        self.cliente1.depositar(300)
        self.cliente2.depositar(1200)
        self.cliente3.depositar(150)
    def depositos(self):
        total=self.cliente1.devolver_dinero()+self.cliente2.devolver_dinero()+self.cliente3.devolver_dinero()
        print('El total de dinero que hay en el banco es de: ', total)
        self.cliente1.imprimir()
        self.cliente2.imprimir()
        self.cliente3.imprimir()
class Cliente:
    def __init__(self, nombre):
        self.nombre=nombre
        self.cantidad=0  
    def depositar(self, cantidad):
        self.cantidad+=cantidad
    def devolver_dinero(self):
        return self.cantidad
    def imprimir(self):
        print(self.nombre, 'tiene', self.cantidad)
banco1=Banco()
banco1.operacion()
banco1.depositos()


# Desarrollar un programa que conste de una clase padre Cuenta y dos subclases PlazoFijo y CajaAhorro. Definir los atributos titular 
# y cantidad y un método para imprimir los datos en la clase Cuenta. La clase CajaAhorro tendrá un método para heredar los datos y uno 
# para mostrar la información.
# La clase PlazoFijo tendrá dos atributos propios, plazo e interés. Tendrá un método para obtener el importe del interés 
# (cantidad*interés/100) y otro método para mostrar la información, datos del titular plazo, interés y total de interés.
#Crear al menos un objeto de cada subclase.


class Cuenta:
	def __init__(self,titular,cantidad):
		self.titular=titular
		self.cantidad=cantidad
	def imprimir(self):
		print("Titular: ",self.titular)
		print("Cantidad: ", self.cantidad)
class CajaAhorro(Cuenta):
	def __init__(self,titular,cantidad):
		super().__init__(titular,cantidad)
	def imprimir(self):
		print("Cuenta de caja de ahorros")
		super().imprimir()

class PlazoFijo(Cuenta):
	def __init__(self,titular,cantidad,plazo,interes):
		super().__init__(titular,cantidad)
		self.plazo=plazo
		self.interes=interes
	def ganancia(self):
		ganancia=self.cantidad*self.interes/100
		print("El importe de interés es: ",ganancia)
	def imprimir(self):
		print("Cuenta a plazo fijo")
		super().imprimir()
		print("Plazo disponible en días: ",self.plazo)
		print("Interés: ",self.interes)
		self.ganancia()
caja1=CajaAhorro("Manuel",5000)
caja1.imprimir()
plazo1=PlazoFijo("Isabel",8000,365,1.2)
plazo1.imprimir()

class Vehiculo():

    def __init__(self, color, ruedas):
        self.color=color
        self.ruedas=ruedas
    
    def __str__(self):
        return 'color {}, {} ruedas'.format(self.color,self.ruedas)

class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):
        #Vehiculo.__init__(self,color,ruedas)
        super().__init__(color,ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        #z='color {}, {} km/h, {} ruedas, {} cc'
        return super().__str__() + '{} km/h, {} cc'.format(self.velocidad,self.cilindrada)#z.format(self.color, self.velocidad, self.ruedas, self.cilindrada)
    
y = Coche('rojo',4,120,1500)
print(y)
class Fraccion:
    def __init__(self, num=0, den=1):#especificamos los valores de atrib.
        if isinstance(num,int):
            self.num=num#Aqui definimos los atributos (caracteristicas)
        else:
            self.num=0#Aqui definimos los atributos (caracteristicas)
        if isinstance(den,int) and den!=0:
            self.den=den#Aqui definimos los atributos (caracteristicas)
        else:
            self.den=1

    # def __del__(self):
    #     print('Destruyendo el objeto', self.num, '/', self.den)

    def __str__(self):#Aqui estamos declarando los metodos (funcionalidad)
        return'{'+ str(self.num)+'/'+str(self.den)+'}'
    
    def __add__(self,obj):
        n=(self.num*obj.den)+(self.den*obj.num)
        d=self.den*obj.den
        x=Fraccion(n,d)
        return x
    
    def __sub__(self,obj):
        n=(self.num*obj.den)-(self.den*obj.num)
        d=self.den*obj.den
        x=Fraccion(n,d)
        return x
    
    def __mul__(self, obj):
        n=self.num*obj.num
        d=self.den*obj.den
        x=Fraccion(n,d)#
        return x
    
    def __div__(self,obj):
        n=self.num*obj.den   
        d=self.den*obj.num
        x=Fraccion(n,d)#
        return x

    def __eq__(self,obj):
        if self.num/self.den == obj.num/obj.den:
            return True
        else:
            return False

def main():
    a=Fraccion(1,2)
    b=Fraccion(1,2)
    print(a==b)


    # a= Fraccion(4,3)#Aqui asignamos a un objeto una clase
    # a.imprime()#Aqui asignamos el método a objeto
    # b= Fraccion(8,9)#Aqui asignamos a un objeto una clase
    # b.imprime()#Aqui asignamos el método a objeto
    # r=a.adicion(b)
    # r.imprime()
    # r=a.sustraccion(b)
    # r.imprime()
    # r=a.multiplicacion(b)
    # r.imprime()
    # r=a.division(b)
    # r.imprime()
if __name__=='__main__':
    main()






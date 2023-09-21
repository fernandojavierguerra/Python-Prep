class calculos:

    def __init__(self, lista_numeros) -> None:
        self.lista_numeros = lista_numeros

    def __verificarPrimo(self, numero):
        esPrimo = True
        num = numero
        while esPrimo and num>1:
            if numero%num == 0 and num!=numero:
                esPrimo=False
            num-=1
        if esPrimo and numero!=0:
            return True
        else:
            return False
        
    def verificarPrimo(self):
        for n in self.lista_numeros:
            if (self.__verificarPrimo(n)):
                print('El numero ',n ,' es primo')
            else:
                print('El numero ',n ,' no es primo')    
    
    def valorModal(self):
        numeros=[]
        repeticiones=[]
        mayorRepeticiones=0
        indiceMayor=0
        for e in self.lista_numeros:
            if e not in numeros:
                numeros.append(e)
                repeticiones.append(0)
            indice=numeros.index(e)
            repeticiones[indice]=repeticiones[indice]+1
            if repeticiones[indice]>mayorRepeticiones:
                mayorRepeticiones=repeticiones[indice]
                indiceMayor=indice
        return(numeros[indiceMayor], mayorRepeticiones)

    def celsiusFarenheit(self, grados):
        return (grados*9/5)+32

    def celsiusKelvin(self, grados):
        return grados+273.15

    def farenheitCelsius(self, grados):
        return (grados-32)*5/9

    def kelvinCelsius(self, grados):
        return grados-273.15

    def kelvinFarenheit(self, grados):
        valorIntermedio=self.kelvinCelsius(grados)
        return (self.celsiusFarenheit(valorIntermedio))

    def farenheitKelvin(self, grados):
        valorIntermedio=self.farenheitCelsius(grados)
        return (self.celsiusKelvin(valorIntermedio))

    def __conversionGrados(self,valor,origen,destino):
        if origen=='celsius' and destino=='farenheit':
            return(self.celsiusFarenheit(valor))
        if origen=='celsius' and destino=='kelvin':
            return self.celsiusKelvin(valor)
        if origen=='farenheit' and destino=='celsius':
            return(self.farenheitCelsius(valor))
        if origen=='kelvin' and destino=='celsius':
            return self.kelvinCelsius(valor)
        if origen=='kelvin' and destino=='farenheit':
            return self.kelvinFarenheit(valor)        
        if origen=='farenheit' and destino=='kelvin':
            return self.farenheitKelvin(valor)
        
    def conversionGrados(self, origen, destino):
        for n in self.lista_numeros:
            resultado = self.__conversionGrados(n, origen, destino)
            print(n, ' grados ',origen, 'son ', resultado,' grados ',destino)

    def factorial(self, numero):
        if numero == 0:
            return 1
        if numero <0:
            return 'Error: Debe ser positivo o 0'
        if numero>1:
            numero=numero*self.factorial(numero-1)
        return numero
    
    def factoriales(self):
        for n in self.lista_numeros:
            print('Factorial de ',n, ':', self.factorial(n))
        return
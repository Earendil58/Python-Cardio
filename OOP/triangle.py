import math


class Hipotenusa:

    def __init__(self, cat1:float, cat2:float):
        self.__cat1 = cat1
        self.__cat2 = cat2


    def calculo_hipotenusa(self) -> float:
        return math.sqrt(self.__cat1 ** 2 + self.__cat2 ** 2)



triangulo = Hipotenusa(3.14, 7)

resultado = triangulo.calculo_hipotenusa()

print(f'La hipotenusa del triangulo es: {resultado}')


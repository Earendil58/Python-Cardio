import math


class Hipotenusa:
    def __init__(self, cat1, cat2):
        self.__cat1 = cat1
        self.__cat2 = cat2

    def calcular_hipotenusa(self):
        return math.sqrt(self.__cat1 ** 2 + self.__cat2 ** 2)



def main():
    try:
        cateto_1 = float(input('Ingrese el valor del primer cateto: '))
        cateto_2 = float(input('Ingrese el valor del segundo cateto: '))

        triangulo = Hipotenusa(cateto_1, cateto_2)
        hipotenusa = triangulo.calcular_hipotenusa()

        print(f'La hipotenusa del triangulo es: {hipotenusa: .2f}')

    except ValueError:
        print('Error: Por favor, ingrese números válidos')


if __name__ == '__main__':
    main()

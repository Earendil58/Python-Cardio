from math import sqrt

class Hipotenusa:
    def __init__(self, lado1, lado2):
        self._lado1 = self.validador(lado1)
        self._lado2 = self.validador(lado2)
        self._hipotenusa = self.calcular_hipotenusa()


    @staticmethod
    def validador(lado):
        if not isinstance(lado, (int,float)):
            raise ValueError('Por favor introduce un número')
        elif lado <= 0:
            raise ValueError('Por favor ingresa un valor positivo')
        return lado


    def calcular_hipotenusa(self):
        return round(sqrt(self._lado1 ** 2 + self._lado2 ** 2), 2)

    def __str__(self):
        return (f'Los lados del triangulo ingresados son: \n'
                f'  - El primer lado es: {self._lado1} \n'
                f'  - El segundo lado es: {self._lado2} \n'
                f'  - La hipotenusa del triangulo es: {self._hipotenusa}')


def main():
    try:
        primer_lado = float(input('Ingresa el primer lado: '))
        segundo_lado = float(input('Ingresa el segundo lado: '))

        hipotenusa = Hipotenusa(primer_lado, segundo_lado)
        print(hipotenusa)

    except (ValueError, TypeError) as e:
        print(f'Error: {e}')

    except Exception as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    main()




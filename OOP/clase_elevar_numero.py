class ElevarNumero:
    def __init__(self, numero):
        self._numero = self.validar_numero(numero)

    @staticmethod
    def validar_numero(numero):
        if not isinstance(numero,(int, float)):
            raise TypeError('El valor debe ser un número')
        if numero <= 0:
            raise ValueError('El número debe ser positivo')
        return numero


    def elevar_cuadrado(self):
        return self._numero ** 2

    def elevar_cubo(self):
        return self._numero ** 3

    def __str__(self):
        return (f' - El número ingresado es: {self._numero} \n'
                f' - El cuadrado de ese número es: {self.elevar_cuadrado()} \n'
                f' - El cubo de ese número es: {self.elevar_cubo()}')


def main():
    try:
        numero = float(input('Ingrese un número: '))
        elevo_numero = ElevarNumero(numero)
        print(elevo_numero)

    except (ValueError, TypeError) as e:
        print(f'Error: {e}')

    except Exception as e:
        print(f'Ocurrió un error inesperado: {e}')




if __name__ == '__main__':
    main()

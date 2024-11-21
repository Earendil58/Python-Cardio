class OperacionesElementales:
    def __init__(self, num1, num2):
        self._num1 = self.validador_numero(num1)
        self._num2 = self.validador_numero(num2)

    @staticmethod
    def validador_numero(num):
        if not isinstance(num, (int, float)):
            raise ValueError('Error: Por favor, ingrese un número')
        return num


    def suma(self):
        return self._num1 + self._num2

    def resta(self):
        return self._num1 - self._num2

    def multiplicacion(self):
        return self._num1 * self._num2

    def division(self):
        if self._num1 != 0 and self._num2 == 0:
            raise ZeroDivisionError('No se puede dividir por 0')
        else:
            return self._num1 / self._num2

    def __str__(self):
        return(f'- {self._num1} + {self._num2} = {self.suma()}  \n'
               f'- {self._num1} * {self._num2} = {self.multiplicacion()} \n'
               f'- {self._num1} - {self._num2} = {self.resta()} \n'
               f'- {self._num1} / {self._num2} = {self.division()}')


def main():
    try:
        numero_1 = float(input('Ingrese el número 1: '))
        numero_2 = float(input('Ingrese el número 2: '))

        operaciones = OperacionesElementales(numero_1, numero_2)
        print(operaciones)

    except ValueError as e:
        print(f'Error: Entrada inválida: {e}')
    except ZeroDivisionError as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'Ocurrió un error: {e}')


if __name__ == '__main__':
    main()








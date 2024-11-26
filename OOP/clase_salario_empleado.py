class SalarioEmpleado:
    """
    Clase para calcular el salario neto de un empleado considerando horas trabajadas,
    tarifa por hora y deducciones.
    """

    ERROR_NOMBRE = 'El nombre del empleado debe ser una cadena no vacía y alfabética.'
    ERROR_NUMERO = 'Ingrese un valor numérico.'
    ERROR_VALOR_MINIMO = 'El valor debe ser mayor o igual a {minimo}.'
    ERROR_DEDUCCIONES = 'Las deducciones no pueden exceder el salario bruto.'

    def __init__(self, nombre_empleado, horas_trabajadas, tarifa_hora, total_deducciones):
        self._nombre_empleado = self.validador_nombre(nombre_empleado)
        self._horas_trabajadas = self.validador_numerico(horas_trabajadas, minimo=1)
        self._tarifa_hora = self.validador_numerico(tarifa_hora, minimo=1)
        self._total_deducciones = self.validador_numerico(total_deducciones, minimo=0)

    @staticmethod
    def validador_nombre(nombre):
        if not isinstance(nombre, str) or not nombre.strip() or not nombre.replace(' ', '').isalpha():
            raise ValueError(SalarioEmpleado.ERROR_NOMBRE)
        return nombre.strip()

    @staticmethod
    def validador_numerico(numero, minimo=0):
        if not isinstance(numero, (int, float)):
            raise ValueError(SalarioEmpleado.ERROR_NUMERO)
        if numero < minimo:
            raise ValueError(SalarioEmpleado.ERROR_VALOR_MINIMO.format(minimo=minimo))
        return numero

    def salario_empleado(self):
        salario_bruto = self._horas_trabajadas * self._tarifa_hora
        salario_neto = salario_bruto - self._total_deducciones
        if salario_neto < 0:
            raise ValueError(self.ERROR_DEDUCCIONES)
        return round(salario_neto, 2)

    def __str__(self):
        return (f'Empleado: {self._nombre_empleado}\n'
                f'Salario bruto: ${self._horas_trabajadas * self._tarifa_hora:.2f}\n'
                f'Deducciones: ${self._total_deducciones:.2f}\n'
                f'Salario neto: ${self.salario_empleado():.2f}')


def main():
    try:
        nombre_empleado = input('Ingrese el nombre del empleado: ')
        horas_trabajadas = int(input('Ingrese la cantidad de horas trabajadas: '))
        tarifa_hora = float(input('Ingrese la tarifa por hora: '))
        total_deduccion = float(input('Ingrese las deducciones correspondientes (0, si no hubo): '))

        empleado = SalarioEmpleado(nombre_empleado, horas_trabajadas, tarifa_hora, total_deduccion)
        print(empleado)

    except (ValueError, TypeError) as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'Error inesperado: {e}')


if __name__ == '__main__':
    main()

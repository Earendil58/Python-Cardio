class SalarioEmpleado:
    def __init__(self, nombre_empleado, horas_trabajadas, tarifa_hora, total_deducciones):
        self._nombre_empleado = self.validador_nombre(nombre_empleado)
        self._horas_trabajadas = self.validador_numerico(horas_trabajadas)
        self._tarifa_hora = self.validador_numerico(tarifa_hora)
        self._total_deducciones = self.validador_numerico(total_deducciones)


    @property
    def nombre_empleado(self):
        return self._nombre_empleado

    @nombre_empleado.setter
    def nombre_empleado(self, valor):
        self._nombre_empleado = self.validador_nombre(valor)

    @staticmethod
    def validador_nombre(nombre):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError('El nombre del empleado debe ser una cadena no vacía.')
        return nombre.strip()

    @property
    def horas_trabajadas(self):
        return self._horas_trabajadas

    @horas_trabajadas.setter
    def horas_trabajadas(self, valor):
        self._horas_trabajadas = self.validador_numerico(valor)

    @property
    def tarifa_hora(self):
        return self._tarifa_hora

    @tarifa_hora.setter
    def tarifa_hora(self, valor):
        self._tarifa_hora = self.validador_numerico(valor)

    @property
    def total_deducciones(self):
        return self._total_deducciones

    @total_deducciones.setter
    def total_deducciones(self, numero):
        self._total_deducciones = self.validador_numerico(numero, permitir_cero=True)


    @staticmethod
    def validador_numerico(numero, permitir_cero=False):
        if not isinstance(numero, (int, float)):
            raise ValueError('Ingrese un valor numérico')
        elif numero < 0 or (numero == 0 and not permitir_cero):
            raise ValueError('El número debe ser positivo o mayor que cero')
        return numero




    def salario_empleado(self):
        calculo_salario = (self._horas_trabajadas * self._tarifa_hora) - self._total_deducciones
        if calculo_salario < 0:
            raise ValueError('Las deducciones no pueden exceder el salario bruto')
        salario_redondeado = round(calculo_salario, 2)
        return salario_redondeado

    def __str__(self):
        return (f'El empleado: {self._nombre_empleado}, ganó en total ${self.salario_empleado()}')



def main():
    try:
        nombre_empleado = input('Ingrese el nombre del empleado: ')
        horas_trabajadas = int(input('Ingrese la cantidad de horas trabajadas: '))
        tarifa_hora = float(input('Ingrese la tarifa por hora: '))
        total_deduccion = float(input('Ingrese las deducciones correspondientes (0, si no hubo): '))

        empleado = SalarioEmpleado(nombre_empleado, horas_trabajadas, tarifa_hora, total_deduccion)
        print(empleado)

    except (ValueError, TypeError) as e:
        print(e)
    except Exception as e:
        print('e')


if __name__ == '__main__':
    main()

class FamiliaEdadPromedio:
    def __init__(self, edad_hijo, edad_padre, edad_madre):
        self._edad_hijo = self.validar_edad(edad_hijo)
        self._edad_padre = self.validar_edad(edad_padre)
        self._edad_madre = self.validar_edad(edad_madre)

    @staticmethod
    def validar_edad(edad):
        if (edad) < 0:
            raise ValueError(f'La edad debe ser un entero positivo')
        return edad

    def calcular_edad_promedio(self):
        promedio_edad = (self._edad_hijo + self._edad_padre + self._edad_madre) / 3

        return promedio_edad

    def __str__(self):
    # Representación legible del objeto
        return (f"Familia:\n"
            f" - Edad del hijo: {self._edad_hijo}\n"
            f" - Edad del padre: {self._edad_padre}\n"
            f" - Edad de la madre: {self._edad_madre}\n"
            f" - Promedio de edad: {self.calcular_edad_promedio():.2f}")


def main():
    try:
        edad_hijo_1 = int(input('Ingrese la edad del hijo: '))
        edad_padre_1 = int(input('Ingrese la edad del padre: '))
        edad_madre_1 = int(input('Ingrese la edad de la madre: '))

        promedio_familia_1 = FamiliaEdadPromedio(edad_hijo_1, edad_padre_1, edad_madre_1)

        print(promedio_familia_1)

    except ValueError:
        print('Por favor, ingresa datos validos')


if __name__ == '__main__':
    main()

class AreaTriangulo:
    def __init__(self, base, altura):
        self._base = self.validador(base)
        self._altura = self.validador(altura)

    @staticmethod
    def validador(medida):
        if not isinstance(medida, (int, float)):
            raise ValueError('Por favor ingrese un número')
        elif medida <= 0:
            raise ValueError('Por favor ingrese un número positivo')
        return medida


    def area_triangulo(self):
        area = (1/2) * self._base * self._altura
        area_redondeada = round(area, 2)
        return area_redondeada

    def __str__(self):
        return (f' - La base ingresada es: {self._base} \n'
                f' - La altura ingresada es: {self._altura} \n'
                f' - El area del triangulo es: {self.area_triangulo()}')


def main():
    try:
        base = float(input('Ingrese la base del triangulo: '))
        altura = float(input('Ingrese la altura del triangulo: '))

        triangulo = AreaTriangulo(base,altura)
        print(triangulo)

    except (ValueError, TypeError) as e:
        print(e)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()


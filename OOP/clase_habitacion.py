class Habitacion:

    ERROR_NUMERICO = 'Por favor ingrese un valor numérico'
    ERROR_VALOR_MINIMO = 'Por favor ingrese un número mayor'

    def __init__(self, largo, ancho, alto):
        self._largo = self.validador_numerico(largo)
        self._ancho = self.validador_numerico(ancho)
        self._alto = self.validador_numerico(alto)


    @staticmethod
    def validador_numerico(num, minimo=1):
        if not isinstance(num, (int, float)):
            raise ValueError(Habitacion.ERROR_NUMERICO)
        elif num < minimo:
            raise ValueError(Habitacion.ERROR_VALOR_MINIMO)
        return num


    @property
    def largo(self):
        return self._largo

    @property
    def ancho(self):
        return self._ancho

    @property
    def alto(self):
        return self._alto

    def area_alfombra(self):
        calculo_area = round(self._largo * self._ancho, 2)
        return calculo_area

    def area_papel_tapiz(self):
        return round(2 * (self._largo * self._alto + self._ancho * self._alto), 2)

    def __str__(self):
        return (f'Largo: {self.largo} \n'
                f'Ancho: {self.ancho} \n'
                f'Alto: {self.alto}')




def main():
    try:
        ingreso_largo = float(input('Ingrese el valor del largo de la hab: '))
        ingreso_ancho = float(input('Ingrese el valor del ancho de la hab: '))
        ingreso_alto = float(input('Ingrese el valor del alto de la hab: '))

        instancia_habitacion = Habitacion(ingreso_largo,ingreso_ancho,ingreso_alto)

        area_alfombra = instancia_habitacion.area_alfombra()
        print(f'El area de la alfombra es de: {area_alfombra}m2')

    except (ValueError, TypeError) as e:
        print(f'Error: {e}')

    except Exception as e:
        print(f'Error inesperado: {e}')



if __name__ == '__main__':
    main()

        

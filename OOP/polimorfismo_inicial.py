class Figura:
    def area(self):
        raise NotImplementedError('Este método debe ser implementado por la subclase')


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14 * self.radio ** 2


class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto


def mostrar_area(figura):
    print(f'El area de la figura es: {figura.area()}')



figura_1 = Circulo(5)

mostrar_area(figura_1)



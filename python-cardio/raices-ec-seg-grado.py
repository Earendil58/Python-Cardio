from math import sqrt


# DATOS:
a = float(input('ingrese el primer número de la ecuación: '))
b = float(input('ingrese le segundo número de la ecuación: '))
c = float(input('ingrese el tercer número de la ecuación: '))


# CALCULOS:

discriminante = ((b**2) - 4 * a * c)

if a != 0:
    if discriminante >= 0:
        x1 = (-b + sqrt(discriminante)) / 2 * a
        x2 = (-b - sqrt(discriminante)) / 2 * a
        print('Las raices de la ecuación son x1: {0} y x2: {1}'.format(x1, x2))
    else:
        print('No existen raices dentro se los reales.')
else:
    if b != 0:
        x = -c / b
        print('La ec no es de segundo grado,la sol es {0}'.format(x))
    else:
        if c != 0:
            print('La ec tiene infinitas sol')
        else:
            print('La ec no tiene sol.')

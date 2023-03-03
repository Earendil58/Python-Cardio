
a = float(input('Ingrese el primer número: '))
b = float(input('Ingrese el segundo número: '))
c = float(input('Ingrese el tercer número: '))
d = float(input('Ingrese el cuerto número: '))
e = float(input('Ingrese el quinto número: '))

menor_distancia_a_numero = a

a_b = a - b
a_c = a - c
a_d = a - d
a_e = a - e


if a_b < a_c:
    menor_distancia_a_numero = a_b

if a_c < menor_distancia_a_numero:
    menor_distancia_a_numero = a_c

if a_d < menor_distancia_a_numero:
    menor_distancia_a_numero = a_d

if a_e < menor_distancia_a_numero:
    menor_distancia_a_numero = a_e


print('El número más cercano al primero es {0}'.format(menor_distancia_a_numero))
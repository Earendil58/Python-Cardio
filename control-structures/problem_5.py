# Design a program that, given an integer, determines whether it is twice an odd number. 

number = float(input('Enter a number: '))

number_divided_for_two = number / 2

if number_divided_for_two % 2 != 0:
    print(f'El número {number} es el doble de un número impar')
else:
    print(f'El número {number} no es el doble de un número impar')
# Develop a program that loads an integer by keyboard, 
# and displays the last digit of the integer (on one side) 
# and the last two digits (on the other side).

integer = int(input('Enter an integer: '))

two_digits = integer%100

print(f'The number you have enter: {integer} has the last two digits: {two_digits} ')
# Design a program that, given an integer, displays the message "is even" when the number is even and the message "is not even" when it is odd.


number = float(input('Enter a number: '))

if number % 2 == 0:
    print('The number is even')
else:
    print('The number is not even')
# Design a program that reads a character from the keyboard and displays the message
# "Is parenthesis" only if the character read is an open or closed parenthesis.

character = input('Enter a character: ')

if character == '(' or character == ')':
    print('Is parenthesis')
else:
    print("It's not a parenthesis")
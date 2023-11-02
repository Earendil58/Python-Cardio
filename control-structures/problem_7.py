# Design a Python program that reads any character from the keyboard and
# displays the message "is uppercase" when the character is an uppercase 
# letter and the message "is lowercase" when it is a lowercase letter.

letra = input('Dame una letra: ')

if letra > 'a' and letra < 'z':
    print(f'La letra {letra} es minúscula')
    
elif letra > 'A' and letra < 'ZK5':
    print(f'La letra {letra} es mayúscula')
    
else:
    print('Esa no es una letra')





# Show me the maximum of 5 numbers entered by the user. 

number_1 = float(input('Give me the first number: '))
number_2 = float(input('Give me the second number: '))
number_3 = float(input('Give me the third number: '))
number_4 = float(input('Give me the fourth number: '))
number_5 = float(input('Give me the fifth number: '))


maximum = number_1

if number_2 > maximum:
    maximum = number_2
    
if number_3 > maximum:
    maximum = number_3
    
if number_4 > maximum:
    maximum = number_4
    
if number_5 > maximum:
    maximum = number_5


print(f'The max number is {maximum}')
    



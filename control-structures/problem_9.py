# Design a program that, given five integers, determines which of the last four numbers is closest to the first.

first_number = int(input('Enter the first number: '))
second_number = int(input('Enter the second number: '))
third_number = int(input('Enter the third number: '))
fourth_number = int(input('Enter the fourth number: '))
fifth_number = int(input('Enter the fifth number: '))

#Distance to the first
second_number_to_first = [abs(second_number - first_number), second_number]
thirth_number_to_first = [abs(third_number - first_number), third_number]
fourth_number_to_first = [abs(fourth_number - first_number), fourth_number]
fifth_number_to_first = [abs(fifth_number - first_number), fifth_number]

#the lowest number is the closest
minimum = second_number_to_first

if thirth_number_to_first[0] < minimum[0]:
    minimum = thirth_number_to_first
    
if fourth_number_to_first[0] < minimum[0]:
    minimum = fourth_number_to_first
    
if fifth_number_to_first[0] < minimum[0]:
    minimum = fifth_number_to_first


print(f'The closest number to the first is {minimum[1]}')
# Diseña un programa que lea la edad de dos personas y diga quién es más joven, la
# primera o la segunda. Ten en cuenta que ambas pueden tener la misma edad. En tal caso, hazlo
# saber con un mensaje adecuado.

first_person = int(input('Tell me your age: '))
second_person = int(input('Tell me your age: '))

if first_person > second_person:
    print('The first person is older')
    
elif first_person == second_person:
    print('The have the same age')
else:
    print('The second person is older')
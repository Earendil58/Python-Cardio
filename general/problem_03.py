# Develop a program that, knowing the value of the perimeter of a rectangle and the value of one of the sides of that rectangle, 
# calculates and displays the value of the area (or surface area) of that rectangle.

rectangle_perimeter = float(input('Give me the perimeter of a rectangle: '))
side_of_rectangle = float(input('Gime me the side of a rectangle: '))

missing_side = (rectangle_perimeter / 2) - side_of_rectangle

area_of_rectangle = missing_side * side_of_rectangle

print(f'The area of a rectangle is {area_of_rectangle}')


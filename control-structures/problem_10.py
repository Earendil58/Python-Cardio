# Design a program that, given three points in the plane, determines which of the last two points is closest to the first.
# A point will be represented by two variables: one for the x-axis and one for the y-axis.

from math import sqrt

first_point_x_axis = float(input('Enter the x1: ')) 
first_point_y_axis = float(input('Enter the y1: '))

second_point_x_axis = float(input('Enter the x2: '))
second_point_y_axis = float(input('Enter the y2: '))

third_point_x_axis = float(input('Enter the x3: '))
third_point_y_axis = float(input('Enter the y3: '))



second_to_first_point_hypotenuse = sqrt((second_point_x_axis - first_point_x_axis)**2 + (second_point_y_axis - first_point_y_axis)**2)
third_to_first_point_hypotenuse = sqrt((third_point_x_axis - first_point_x_axis)**2 + (third_point_y_axis - first_point_y_axis)**2)


if third_to_first_point_hypotenuse < second_to_first_point_hypotenuse:
    print('The point closest to the first one is the third one.')
else:
    print('The point closest to the first one is the second one.')
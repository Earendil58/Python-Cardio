

student_grade = int(input('Please, enter your grade: '))

if student_grade == 10: 
    print('Honor student')
    
elif student_grade < 10 and student_grade >= 8:
    print('Very good, your are awesome')
    
elif student_grade < 8 and student_grade >= 6 :
    print('remarkable')
    
elif student_grade < 6 and student_grade >= 3:
    print('You need to study more')
    
elif student_grade < 3 :
    print('Come on! study harder')
    
    
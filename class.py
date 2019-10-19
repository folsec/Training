
num_of_courses = int(input('HOW MANY COURSES ARE YOU OFFERING?'))
courses = []
grades = []
units = []
while num_of_courses >= 1:
    course = (input('enter course title: '))
    a = courses.append(course)
    num_of_courses -= 1
print(courses)
for course in courses:
    grade = input('enter grade for {}'.format(course))
    unit = int(input('enter unit for {}'.format(course)))
    p = units.append(unit)
    grade = grade.upper()

    if grade == 'A':
        calculated = unit * 5
        b = grades.append(calculated)
        print(calculated)
    elif grade == 'B':
        calculated = unit * 4
        b = grades.append(calculated)
        print(calculated)
    elif grade == 'C':
        calculated = unit * 3
        b = grades.append(calculated)
        print(calculated)
    elif grade == 'D':
        calculated = unit * 2
        b = grades.append(calculated)
        print(calculated)
    elif grade == 'F':
        calculated = unit * 1
        b = grades.append(calculated)
        print(calculated)
    else:
        print("YOU'VE NOT ENTERED ANY COURSE")
    print(grade)
    print(unit)
grades = tuple(grades)
print(grades)
unit = tuple(units)
print(units)
units = sum(units)
grades = sum(grades)
print('Your total grade score is ',grades)
GPA2 = grades / units
GPA2 = "%.2f" %GPA2
new_gp = sum(GPA,GPA2)
print('Your GP for this semester is ',GPA2)
print('YOUR TOTAL GPA FOR THIS SEMESTER IS ',new_gp)
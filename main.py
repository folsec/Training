courses = []
grades = []
units = []
def first_gp():

    return GPA

def first_semester():
    num_of_courses = int(input('HOW MANY COURSES ARE YOU OFFERING?'))
    while num_of_courses >= 1:
        course = (input('enter course title: '))
        a = courses.append(course)
        num_of_courses -= 1
    print(courses)
def grade():
    first_semester()
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
grade()
grades = tuple(grades)
print(grades)
unit = tuple(units)
print(units)
units = sum(units)
grades = sum(grades)
GPA = grades / units
print('Your total grade score is ',grades)
GPA = "%.2f" %GPA
print('YOUR TOTAL GPA FOR THIS SEMESTER IS ',GPA)

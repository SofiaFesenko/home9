group_of_students = {}
students = []


class Student:
    @staticmethod
    def update_student():
        students.append(student)
        print(students)

    @staticmethod
    def update_group():
        group_name = input('input a name of a group')
        group_of_students[student] = group_name
        if ans in group_of_students:
            print('your student is now in our group')
            print(group_of_students)
        else:
            print('your student is now the first in our group')
            print(group_of_students)

    @staticmethod
    def delete():
        del student
        print(students)


while True:
    student = input('input name of student or break(if you want to exit)')
    if student != 'break':
        if student in students:
            ans = input('your student is in our school. do you want to chose a new group or to go away? (n/g)')
            if ans == 'n':
                Student.update_group()
            else:
                Student.delete()
        else:
            print('we don`t have this student')
            Student.update_student()
    else:
        break

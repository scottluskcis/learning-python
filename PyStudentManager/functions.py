students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(name, student_id=-1):
    student = { "name": name, "student_id": student_id }
    students.append(student)


student_list = get_students_titlecase()

keep_adding_students = True
while keep_adding_students: 
    add_new_student = input("Do you want to add a student (yes/no): ")
    if(add_new_student.lower().startswith("y")):
        student_name = input("Enter student name: ")
        student_id = input("Enter student ID: ") 
        add_student(student_name, student_id)
    else:
        keep_adding_students = False

print_students_titlecase()
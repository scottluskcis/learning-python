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


def save_file(student):
    try:
        f = open("students.txt", "a") # append text to a file using access mode a 
        f.write(student + "\n")
        f.close()
    except Exception:
        print("Could not save file")


def read_file():
    try:
        f = open("students.txt", "r") # read text from a file using access mode r 
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print("Could not read file")


read_file()
print_students_titlecase()

keep_adding_students = True
while keep_adding_students: 
    add_new_student = input("Do you want to add a student (yes/no): ")
    if(add_new_student.lower().startswith("y")):
        student_name = input("Enter student name: ")
        student_id = input("Enter student ID: ") 
        add_student(student_name, student_id)
        save_file(student_name)
    else:
        keep_adding_students = False

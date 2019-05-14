students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student.get("name", "unknown").title()
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(name, student_id=-1):
    student = { "name": name, "student_id": student_id }
    students.append(student)


def var_args(name, *args):
    print(name)
    print(args)


def var_kwargs(name, **kwargs):
    print(name)
    print(kwargs["description"], kwargs["feedback"])


# named arguments
add_student(name="Mark", student_id=15)
print_students_titlecase()

# using variable args
var_args("Mark", "Loves Python", None, "Hello", True)

# using kwargs 
var_kwargs("Mark", description="Loves Python", feedback=None, pluralsight_subscriber=True)

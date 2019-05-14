students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student.get("name", "unknown").title())
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


# using named parameters and default values
def add_student(name, student_id=-1):
    student = { "name": name, "student_id": student_id }
    students.append(student)


# using args for variable number of arguments
def var_args(name, *args):
    print(name)
    print(args)


# using kwargs with dictionary 
def var_kwargs(name, **kwargs):
    print(name)
    print(kwargs["description"], kwargs["feedback"])


# nested functions
def get_students_nested():
    students = ["mark", "james"]
    def get_students_titlecase_names():
        students_titlecase = []
        for student in students:
            students_titlecase.append(student.title())
        return students_titlecase
    students_titlecase_names = get_students_titlecase_names()
    print("Nested Function Example: {0}".format(students_titlecase_names))

# named arguments
add_student(name="Mark", student_id=15)
print_students_titlecase()

# using variable args
var_args("Mark", "Loves Python", None, "Hello", True)

# using kwargs 
var_kwargs("Mark", description="Loves Python", feedback=None, pluralsight_subscriber=True)

# using nested functions
get_students_nested()
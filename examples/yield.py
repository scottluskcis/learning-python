students = []


def read_file():
    try:
        f = open("students.txt", "r") # read text from a file using access mode r 
        for student in read_students(f):
            students.append(student)
        f.close()
    except Exception:
        print("Could not read file")


# use generator with yield to read each line in the file
def read_students(f):
    for line in f:
        yield line


read_file()
print(students)
students = []


# example using a class in python
class Student:
    
    # class attributes
    school_name = "Springfield Elementary"

    # constructor 
    def __init__(self, name, student_id=-1):
        # assign instance attributes 
        self.name = name
        self.student_id = student_id
        # add to collection
        students.append(self)

    # str override
    def __str__(self):
        return "Student {0} is at school {1}".format(self.name, self.school_name)

    # method that access instance attributes
    def get_name_capitalize(self):
        return self.name.capitalize()

    # return a class attribute
    def get_school_name(self):
        return self.school_name
 

# class inheritance 
class HighSchoolStudent(Student):

    # override a class attribute
    school_name = "Springfield High School"

    # override get school name method
    def get_school_name(self):
        return "This is a High School student"

    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value + "-HS"


# to create a new instance of a class
mark = Student("Mark") 
print(mark)

# access class attribute
print(Student.school_name)

# create an instance of high school student
james = HighSchoolStudent("james")
print(james.get_name_capitalize())
#print(james.get_school_name())
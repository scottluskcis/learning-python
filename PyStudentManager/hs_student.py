from student import *

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
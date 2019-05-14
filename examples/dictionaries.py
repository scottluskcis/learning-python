student = {
    "Name": "Mark",
    "Age": 22,
    "Email": None
}

# access by key
print("Student Name: {0}".format(student["Name"]))

# access using get with a default value for a non existing property
print("Student last name: {0}".format(student.get("LastName", "Uknown")))

# see all the value that are part of dictionary
print("Values: {0}".format(student.values()))

# see all the keys that are part of the dictionary
print("Keys: {0}".format(student.keys()))

# remove a key
del student["Email"]
print("Keys after removing Email: {0}".format(student.keys()))

# add a key
student["LastName"] = "Smith"
print("Keys after adding LastName: {0}".format(student.keys()))

# exception handling
try:
    foo_key = student["foo"]
except KeyError:
    print("Error fiding foo key")

# chaining exceptions
try:
    foo_key = student.get("foo", "unknown") # cause a key error
    number_val = 3 + foo_key # cause a type error
except KeyError:
    print("Error fiding foo key")
except TypeError:
    print("I can't add these two together!")
except Exception:
    print("Unknown error")  # catch all for any type 

print("code outside of try/except")

# lots of other things are also possible, finally, custom exceptions, etc

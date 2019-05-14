students = ["John"]
#print(students)

# append
students.append("Fred")
students.append("Joe")
students.append("Wilma")
students.append("Rose")

#print(students)

# first element
first_student = students[0]
print("First Student: {0}".format(first_student))

# last element
last_student = students[-1]
print("Last Student: {0}".format(last_student))

# use len
print("{0} students in list".format(len(students)))
 
print("Count before removing an item: {0}".format(len(students)))
# remove an item
del students[-1]
print("Count after removing an item: {0}".format(len(students)))

# list slicing
print("[1:-1] is {0}".format(students[1:-1]))

# printing elements
for name in students: 
    print("Student name: {0}".format(name))

# range
x = 0
for index in range(10):
    x += 10
    print("x is currently {0} and index is {1}".format(x, index))

x = 0
for index in range(5, 10):
    x += 10
    print("x is currently {0} and index is {1}".format(x, index))

x = 0
for index in range(4, 10, 2):
    x += 10
    print("x is currently {0} and index is {1}".format(x, index))

# break
for name in students:
    if(name == "Wilma"):
        print("Found Wilma")
        break
    else:
        continue

# while
num = 10
while True:
    if num > 42:
        print("Existing loop, num is currently {0}".format(num))
        break
    else:
        num += 10


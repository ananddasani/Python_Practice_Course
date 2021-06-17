# Program to demonstrate List and Tuples

# to create lists use []
students = ["anand", "om", "meet"]
print(type(students))
print(len(students))

print(students[-1])  # getting last student
print(students[: 2])  # getting first 2 students

students[0] = "Ria"
print(students)

# use insert method to insert object into the list
# or use append mehtod if you want to add at the end of the list

print("\n")
print(students)
students.append("deep")
print(students)

print("\n")
print(students)
students.insert(0, "Anand")
print(students)


# use pop method to remove something form the list

print("\n")
students.pop()  # automatically remove the last indexed value
students.remove("om")
students.pop(1)
print(students)

# concate two lists using +
students2 = ["jay", "ram"]

print(students + students2)


# to create tuples use ()
# tuples are like lists but they are immutable :( [we can't change, remove, add elements]
months = ("jan", "feb", "mar")
print(type(months))

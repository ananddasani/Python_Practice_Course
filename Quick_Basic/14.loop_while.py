# program to demonstrate while loop

people = []  # empty list
x = 0
while x < 5:
    person = input("Enter name of the person :: ")
    people.append(person)
    x += 1
print(people)

#                       OR (Bit direct :) )

# people2 = []
# while len(people2) < 5:
#     person = input("Enter name of the person :: ")
#     people2.append(person)
# print(people2)

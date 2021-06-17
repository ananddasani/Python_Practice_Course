'''
create a program that asks the user for eight names and stored them in a list.

When all the names have been given.

Pick a random one and print it.
'''

import random

myList = []
print("hi there ! , you have to give 8 names , good luck :)")

for i in range(0, 8):
    myList.append(input("give name : "))

print("\nhere's a list you have given names ->")
print(myList)

key = random.randint(0, 7)
print("\npicking a random person :: ", (myList[key]))

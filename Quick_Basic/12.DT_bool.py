# Program to demonstrate boolean DT

'''
create a program to ask the user's age and and print whether 
-he's older than you 
-he's younger than you 
-you both are of same age 
(store your age in an variable)
'''

myAge = 18
userAge = int(input("Enter your age to compare with me :: "))

if(userAge > myAge):
    print("you're older then me :( ")
elif(userAge < myAge):
    print("you're younger then me :( ")
else:
    print("we both are of same age :) ")

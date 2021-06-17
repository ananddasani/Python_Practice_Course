'''
program will ask for any number 
if string is entered than instead of crashing 
program will throw an error message 
'''

number = input("Type a nubmer :: ")

try:
    number = float(number)
    print("number is :: ", number)
except:
    print("Not a nubmer :(")

'''
TEST CASE 1

Type a nubmer :: 12
number is ::  12.0

TEST CASE 2 

Type a nubmer :: anand 
Not a nubmer :(


'''

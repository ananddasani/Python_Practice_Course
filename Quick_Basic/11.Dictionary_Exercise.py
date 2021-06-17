'''
create a program with a predefine dictionary of a person includes 
name , gender , age , address 

ask the user what information he want to know about the person (for example :: name )
then print the value associated with that key or display the error message in case it 
is not found 
'''

people = {"name": "Anand", "gender": "male", "age": 18, "address": "PBR"}

# making the input of user lower because all of our key is in lower case
key = input("Enter the information you want of the person :: ").lower()

# if info is available then printed else error message set by me will be printed
print(people.get(key, "Invalid information"))

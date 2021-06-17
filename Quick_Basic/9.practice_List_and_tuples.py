# Take DOB from user as a format DD-MM-YYYY and print the name of month the user is born in

months = ["january", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]


# taking input as a string
DOB = input("Enter your DOB in DD-MM-YYYY formate :: ")


# calculated the index and converted into int because can't be string
index = int((DOB[3:5])) - 1  # index starts form 0 so substract one
bd_month = months[index]

print("You are born in ", bd_month)


'''
QUESTION 2 :: 
Ask user his name and append that name into the predefined list of names 
'''

people = ["Anand ", "jay", "Ria", " Karina"]

name = input("Enter your name to add it in the list :: ")
people.append(name)
print("here's the list : ", people)

# Proram to demonsterate the input function to take input form the user

# by default the input is in string so explicitly convert into the required data type
n1 = input("Enter 1st number :: ")
n2 = input("Enter 2nd number :: ")

print("Type of n1 and n2 :: ", type(n1))
print("Sum of ", n1, " and ", n2, " is :: ", (n1 + n2)
      )  # the output is 33 due to string :(


# we can take input form the user by using of input() function
# converting the input in float
num1 = float(input("Enter the first number :: "))
num2 = float(input("Enter the second number :: "))

print("Sum of ", num1, " and ", num2, " is :: ", (num1 + num2))

# Program to demonstrate number Data type

# python automatically converts int into float when there is decimals
import math
n1, n2 = 5, 2
print("n1 :: ", type(n1))

result = n1/n2
print("result :: ", type(result))
print(n1, " / ", n2, " = ", result)

# ** is power
print("5 ^ 2 :: ", 5**2)

# some built in functions

print(math.factorial(5))
print(math.ceil(5.5))
print(math.floor(5.5))
print(math.log(5.5))
print(math.log10(5.5))
print(math.pi)

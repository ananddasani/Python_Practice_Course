# Program to practice string data type

# string is a sequence of character
myString = "anand dasani"

# printing the type of DT
TYPE = type(myString)
print(TYPE)

# use double quotes inside single quotes like
myString1 = 'She said me "meet me at 5 tonight"'
print(myString1)

""" # else you  will get error
myString3 = "She said me ""meet me at 5 tonight ""  # error invaid syntax
print(myString3)
"""

# access index by using bracket (first character starts at index 0 and last at index -1)
print(myString1[0])
print(myString1[-1])

# printing length of the string
print("Length is :: ", len(myString1))


# slicing

myCity = "PBR360575"
# excluding 3 (3-1 = 2 so last index which is considered is 2 (R))
print(myCity[0:3])  # PBR
print(myCity[3:])  # 360575


# concatenation

# two strings only be concatenated by using of +
print("Anand " + "Dasani")

# myNameAndNumber = "Anand " + 12345 # to do this, type caste into string
myNameAndNumber = "Anand " + str(12345)
print(myNameAndNumber)

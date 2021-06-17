# using for loop in list

myList = ["Anand", "", "Dasani", "male", 18, "PBR"]

# printing list using for loop
for post in myList:
    if post == "":
        continue
    else:
        print(post)


# using for loop in string

print("---------------------------------------")
myString = "Anand is a python programmer "

for char in myString:
    print(char)


# using for loop in dict

print("---------------------------------------")
myDict = {"1": "Porbandar", "2": "Rajkot", "3": "Surat"}

for key in myDict:
    print(key, " : ", myDict[key])  # this is how it's gonna work

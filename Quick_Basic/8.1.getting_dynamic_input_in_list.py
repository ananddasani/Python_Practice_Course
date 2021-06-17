# program to get a list dynamically form the user

# first create an empty list
myList = []

# now take the size of the list
n = int(input("Enter the size of list :: "))

# now iterate through the limit given
for i in range(0, n):
    ele = int(input("Enter the element : "))

    myList.append(ele)  # adding the element

print(myList)

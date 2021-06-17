# Program to demmonstrate dictionary

# To create dictionary use {}
person_info = {"first_name": "Anand", "last_name": "Dasani",
               "DOY": 2001, "country": "India"}

print(type(person_info))
print(person_info)

print("First name :: ", person_info["first_name"])
print("\n")


# dict are mutable, we can change the elements like
person_info["DOY"] = 2000
print(person_info)
print("\n")


# keys are also called properties, so let's add a new property to our dict
person_info["marital_status"] = "Not married"
print(person_info)
print("\n")

# Adding a list as property
# add a property of children, (we have to add the list of children)
person_info["children"] = ["Ria", "Richard"]
print(person_info)
print("\n")


# Q. add a children named Roy to the list of children
person_info["children"].append("Roy")
print(person_info)
print("\n")


# if we try to access the key which doesn't exits then error will be given so instead use get function so that
# instead of getting error we will get the message which is already set by us

# here age doesn't exists so it will return the message
print(person_info.get("age", "Invalid key :("))
print("\n")

# children exists so it will return children
print(person_info.get("children", "Invalid key :("))
print("\n")


# this is also acceptable :)
key = "first_name"
print(person_info[key])  # OP = Anand


person_info.clear()  # erase everyting
print(person_info)

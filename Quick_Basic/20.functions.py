# program to demonstrate the functions in python

# function without args
def say_hello():
    print("Hello python :)")


say_hello()


# function with args
def say_hello_args(arg1, arg2):
    print("Hello " + arg1 + " how are you doing ? " +
          arg2 + " is waiting for you :)")


say_hello_args("anand", "om")


# different way of passing args
def say_hello_args1(arg1, arg2="jay"):
    print("Hello " + arg1 + " how are you doing ? " +
          arg2 + " is waiting for you :)")


say_hello_args1("anand")


def fah2celsius(fah):
    celsius = (5 * (fah - 32)) / 9
    return celsius


print("Celsius : ", round(fah2celsius(100), 2))
print("Kelvin : ", round(fah2celsius(100) + 273.5, 2))

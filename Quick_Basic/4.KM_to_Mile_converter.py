# Program to convert KM to miles

KM = float(input("Enter Kilometer to convert into miles :: "))
miles = (KM * 0.62137)
print(KM, " Kilometers = ", miles, " Miles :)")

# rounding to the four decimal places
print(KM, " Kilometers = ", round(miles, 4), " Miles :)")

'''
TEST CASE 

Enter Kilometer to convert into miles :: 10
10.0  Kilometers =  6.213699999999999  Miles :)
10.0  Kilometers =  6.2137  Miles :)
'''

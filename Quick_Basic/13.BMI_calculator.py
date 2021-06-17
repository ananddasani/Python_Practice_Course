# Program to create BMI calculator

weight = float(input("Enter your weight in KM (Ex. 55.4) :: "))
# weight *= 703  # converted into pounds

height = float(input("Enter your height in meters (Ex. 1.70) :: "))
# height *= 12  # converted into inches

BMI = weight / (height ** 2)

print("your BMI is ::", round(BMI, 2))

if(BMI <= 18.5):
    print("UNDERWEIGHT :(")
elif(BMI >= 24.9 or BMI <= 29.9):
    print("NORMAL WEIGHT :)")
elif(BMI >= 24.9 or BMI <= 29.9):
    print("OVER WEIGHT :(")
else:
    print("OBESITY :(")

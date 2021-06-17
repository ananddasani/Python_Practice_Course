# program to demonstrate error handling in reference of 18th program (grade system)
# for grade 1
data_valid = False
while data_valid == False:
    grade1 = input("Enter the grade 1 of student (1-10) :: ")

    try:
        grade1 = float(grade1)
    except:
        print("Grades must be integer or decimal (seperated by . )")
        continue

    if grade1 < 0 or grade1 > 10:
        print("Invalid grade entry !! grades must be in between 1 to 10")
        continue
    else:
        data_valid = True


# for grade 2
data_valid = False
while data_valid == False:
    grade2 = input("Enter the grade 2 of student (1-10) :: ")

    try:
        grade2 = float(grade2)
    except:
        print("Grades must be integer or decimal (seperated by . )")
        continue

    if grade2 < 0 or grade2 > 10:
        print("Invalid grade entry !! grades must be in between 1 to 10")
        continue
    else:
        data_valid = True


# for total classes
data_valid = False
while data_valid == False:
    total_classes = input("Enter total number of classes :: ")

    try:
        total_classes = int(total_classes)
    except:
        print("total classes must be integer ")
        continue

    if total_classes < 0:
        print("Invalid total class entry !! it must be greater than or equal to 0")
        continue
    else:
        data_valid = True


# for absence
data_valid = False
while data_valid == False:
    absence = input("Enter the number of absence of student :: ")

    try:
        absence = int(absence)
    except:
        print("Total absence must be an integer ")
        continue

    if absence < 0 or absence > total_classes:
        print("Invalid absence entry !! absence must be in between 0 to ", total_classes)
        continue
    else:
        data_valid = True


avg_grade = (grade1 + grade2) / 2
attendance = (total_classes - absence) / total_classes

if (avg_grade >= 6):
    if(attendance >= 0.80):
        print("student has been approved ")
    else:
        print("student has fail due to attendance is only ",
              str((round(attendance, 2) * 100)) + ' %', " :(")
else:
    print("student has fail due to average grades are only ",
          avg_grade, " which is lower than 80%")

'''
TEST CASE 

Enter the grade 1 of student (1-10) :: anand
Grades must be integer or decimal (seperated by . )
Enter the grade 1 of student (1-10) :: 8
Enter the grade 2 of student (1-10) :: 8
Enter total number of classes :: anand
total classes must be integer    
Enter total number of classes :: 20
Enter the number of absence of student :: anand
Total absence must be an integer 
Enter the number of absence of student :: 2 
student has been approved 

'''

'''
program to validate the data entry like grades must be in range of 0 - 10 
and so on 

still  program is not secured as if any sting entry is done than program will terminate 
this problem is solved in next program using try and except block :)
'''

# for grade 1
data_valid = False
while data_valid == False:
    grade1 = float(input("Enter the grade 1 of student (1-10) :: "))

    if grade1 < 0 or grade1 > 10:
        print("Invalid grade entry !! grades must be in between 1 to 10")
        continue
    else:
        data_valid = True


# for grade 2
data_valid = False
while data_valid == False:
    grade2 = float(input("Enter the grade 2 of student (1-10) :: "))

    if grade2 < 0 or grade2 > 10:
        print("Invalid grade entry !! grades must be in between 1 to 10")
        continue
    else:
        data_valid = True


# for total classes
data_valid = False
while data_valid == False:
    total_classes = int(input("Enter total number of classes :: "))

    if total_classes < 0:
        print("Invalid total class entry !! it must be greater than or equal to 0")
        continue
    else:
        data_valid = True


# for absence
data_valid = False
while data_valid == False:
    absence = int(input("Enter the number of absence of student :: "))

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

Enter the grade 1 of student (1-10) :: -10
Invalid grade entry !! grades must be in between 1 to 10
Enter the grade 1 of student (1-10) :: 30
Invalid grade entry !! grades must be in between 1 to 10
Enter the grade 1 of student (1-10) :: 8
Enter the grade 2 of student (1-10) :: 8
Enter total number of classes :: -5 
Invalid total class entry !! it must be greater than or equal to 0
Enter total number of classes :: 20
Enter the number of absence of student :: -5
Invalid absence entry !! absence must be in between 0 to  20
Enter the number of absence of student :: 25
Invalid absence entry !! absence must be in between 0 to  20
Enter the number of absence of student :: 5
student has fail due to attendance is only  75.0 %  :(
'''

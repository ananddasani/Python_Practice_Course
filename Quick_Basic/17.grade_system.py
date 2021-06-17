'''
ask for grades of two tests made by a student so Grade 1 and Grade 2.
ask for the number of absences and the total number of classes 
so we can calculate the attendance rate

calculate the average grade and the attendance

So the rules are grades are from 0 to 10 and students need an average grade of 6 or higher to get approval.
Students need an attendance rate of 80 percent or higher to get approval.

'''

grade1 = float(input("Enter the grade 1 of student (1-10) :: "))
grade2 = float(input("Enter the grade 2 of student (1-10) :: "))
absence = int(input("Enter the number of absence of student :: "))
total_classes = int(input("Enter total number of classes :: "))

avg_grade = (grade1 + grade2) / 2
attendance = (total_classes - absence) / total_classes

if (avg_grade >= 6):
    if(attendance >= 0.80):
        print("student has been approved ")
    else:
        print("student has fail due to attendance is only ",
              str((round(attendance, 2) * 100)) + ' %', " :(")
else:
    print("student has fail due to average grades are only ", avg_grade, " :(")

'''
TEST CASE

Enter the grade 1 of student (1-10) :: 7
Enter the grade 2 of student (1-10) :: 7
Enter the number of absence of student :: 2
Enter total number of classes :: 20
student has been approved 

'''

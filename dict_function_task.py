# **************************
# Dictionary Function Task
# **************************

no = int(input("Enter Students : "))
student={}

for i in range(0,no,1):
    roll_no = int(input("Enter Roll No: "))
    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))
    grade=None

    student["s{}".format(i+1)] = {'Roll_No':roll_no,'Name':name,
                                   'Marks':marks, 'Grade':grade}


print("Student data Without Grade : ",student)

dict_len = len(student)

for i in range(0, dict_len,1):

    a = student["s{}".format(i+1)]['Marks']

    if a <= 100:
        if a>=90 and a<=100:
            grade = "A"
        elif a>=80 and  a<90:
            grade = "B"
        elif a>=60 and a<80:
            grade = "C"
        elif a>=40 and a<60:
            grade = "D"
        else:
            grade="Fail"
    else:
        print("Invalid Marks")

    student["s{}".format(i + 1)]['Grade']=grade

print("Student With Grade: ",student)










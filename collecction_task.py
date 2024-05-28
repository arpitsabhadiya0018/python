# Task 1
#
# ls = [1, 2, 3, ['a', 'b', 'c'], 4, 5, 6, ['d', 'e', 'f'], 7, 'g', 8, 'h',
#        [9, 10, 'i', 'j'],11,'aansh']
#
# l = len(ls)
# for i in range(0,l,1):
#     a = ls[i]
#     a_str = str(a)
#
#     if a_str.isdigit():
#         print(a_str)
#     elif type(a)==type(ls):
#         for j in range(0,len(ls[i])):
#             b = a[j]
#             b_str = str(b)
#             if b_str.isdigit():
#                 print(b_str)
#             else:
#                 print("     ",b)
#     elif type(a)!=type(ls):
#         for k in a_str:
#             print("     ",k)

# Task 2
#
# student={}
# no = int(input("Enter Students : "))
#
# for i in range(0,no,1):
#     roll_no = int(input("Enter Roll No: "))
#     name = input("Enter Name: ")
#     marks = int(input("Enter Marks: "))
#
#     student["s{}".format(i + 1)] = {'Roll_no': roll_no, 'Name': name,
#                                     'Marks': marks}
#
#     # student['roll_{}'.format(i+1)] = roll_no
#
# print(student)





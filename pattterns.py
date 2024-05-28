
# Pattern 1

# for i in range(0, 5):
#     for j in range(0,5):
#         print("*", end=" ")
#     print()

# Pattern 2

# no = 6
# for i in range(1,no,1):
#     for j in range(0,i,1):
#         print("*", end=" ")
#     print()

# Pattern 3

# for i in range(0,6,1):
#     for j in range(i,5,1):
#         print("*", end=" ")
#     print()

# Pattern 4

# for i in range(1,7,1):
#     for j in range(1,i,1):
#         print(j, end=" ")
#     print()

# Pattern 5

# for i in range(0, 6, 1):
#     for j in range(0, i, 1):
#         print("*", end=" ")
#     print()
#
# for i in range(1,5,1):
#     for j in range(i,5,1):
#         print("*", end=" ")
#     print()

# Pattern 6

# for i in range(1,6,1):
#     for j in range(i,5,1):
#         print(" ",end=" ")
#     for k in range(i,0,-1):
#         print("*", end=" ")
#     print()

# Pattern 7

# for i in range(0,6,1):
#     for j in range(0,i,1):
#         print(" ", end=" ")
#     for k in range(5,i,-1):
#         print("*", end=" ")
#     print()

# Pattern 8

# for i in range(1,6,1):
#     for j in range(i,5,1):
#         print(" ", end=" ")
#     for k in range(i,0,-1):
#         print("*", end=" ")
#     for l in range(1,i,1):
#         print("*", end=" ")
#     print()

# Pattern 9

# for i in range(6,0,-1):
#     for j in range(i,6,1):
#         print(" ", end=" ")
#     for k in range(0,i,1):
#         print("*", end=" ")
#     for l in range(i,1,-1):
#         print("*", end=" ")
#     print()

# Pattern 10

# for i in range(1,6,1):
#     for j in range(i,5,1):
#         print("",end=" ")
#     for k in range(i,0,-1):
#         print("*", end=" ")
#     print()

# Pattern 11

# for i in range(0,6,1):
#     for j in range(0,i,1):
#         print("", end=" ")
#     for k in range(5,i,-1):
#         print("*", end=" ")
#     print()

# Pattern 12

# for i in range(0,6,1):
#     for j in range(0,i,1):
#         print("", end=" ")
#     for k in range(5,i,-1):
#         print("*", end=" ")
#     print()
# for i in range(1,6,1):
#     for j in range(i,5,1):
#         print("",end=" ")
#     for k in range(i,0,-1):
#         print("*", end=" ")
#     print()


# Pattern 13
# n=5
# for i in range(0,n,1):
#     for j in range(0,n-i-1,1):
#         print(" ", end=" ")
#     for j in range(0,2*i+1,1):
#         if i==0 or i==n-1:
#             print("*",  end=" ")
#         else:
#              if j==0 or j==2*i:
#                 print("*", end=" ")
#              else:
#                 print(" ", end=" ")
#     print()

# Pattern 14
#
# n=5
# for i in range(0,n,1):
#     for j in range(0,i,1):
#         print(" ", end=" ")
#     for j in range(n, i, -1):
#         if j==0 or j==n:
#             print("*", end=" ")
#         else:
#             if i==0 or i==n:
#                 print("*", end=" ")
#             else:
#                 print(" ", end=" ")
#     for j in range(n-1,i,-1):
#         if i==0:
#             print("*", end=" ")
#         else:
#             if i==n-1 or j==n-3:
#                 print("*", end=" ")
#             elif i==n-2 and j==n-1:
#                 print("*", end=" ")
#             elif i==n-3 and j==n-2:
#                 print("*", end=" ")
#             else:
#                 print(" ", end=" ")
#
#     print()

# Pattern 15

# n = int(input("Enter No: "))
# for i in range(0,n,1):
#     for j in range(n,i,-1):
#         print(" ", end=" ")
#     for j in range(0,i+1,1):
#         if i==0 or j==0:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     for j in range(0,i,1):
#         if j==i-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# for i in range(0,n+1,1):
#     for j in range(0,i,1):
#         print(" ", end=" ")
#     for j in range(n+1,i,-1):
#         if j==n+1:
#              print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     for j in range(i,n,1):
#         if j==n-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# Pattern 16

# no = int(input("Enter No: "))
# for i in range(0,no,1):
#     for j in range(no-1,i,-1):
#         print(" ",end=" ")
#     for j in range(0,1,1):
#         print("1",end=" ")
#     for j in range(0,1,1):
#         print(" ",end=" ")
#     for j in range(0,1,1):
#         if i==0:
#             print(" ",end=" ")
#         else:
#             print(i,end=" ")
#     for j in range(0, 1, 1):
#         print(" ", end=" ")
#     for j in range(-1,0,1):
#         if i==j+1:
#             print(" ", end=" ")
#         elif i==j+2:
#             print(" ", end=" ")
#         else:
#             print(i - 1, end=" ")
#     for j in range(0, 1, 1):
#         print(" ", end=" ")
#     for j in range(-1,0,1):
#         if i == j+1:
#             print(" ",end=" ")
#         elif i == j+2:
#             print(" ",end=" ")
#         elif i == j+3:
#             print(" ",end=" ")
#         else:
#             print(i-2, end=" ")
#     for j in range(0, 1, 1):
#         print(" ", end=" ")
#     for j in range(-1,0,1):
#         if i == j+1:
#             print(" ",end=" ")
#         elif i == j+2:
#             print(" ",end=" ")
#         elif i == j+3:
#             print(" ",end=" ")
#         elif i == j+4:
#             print(" ",end=" ")
#         else:
#             print(i-3, end=" ")
#     print()

# Pattern 17

# no = int(input("Enter No: "))
# for i in range(0,no,1):
#     for j in range(no,i,-1):
#         print(" ", end=" ")
#     for j in range(0,j,1):
#         print(i-j+1, end=" ")
#     for j in range(1,j+1,1):
#         print(j+1, end=" ")
#     print()
# for i in range(0,no,1):
#     for j in range(0,i+2,1):
#         print(" ",end=" ")
#     for j in range(no-1,i,-1):
#         print(j-i,end=" ")
#     for j in range(i+1,no-1,1):
#         print(j-i+1,end=" ")
#     print()


# Pattern 18

# n = int(input("Enter No: "))
#
# for i in range(0,n,1):
#     for j in range(n,i,-1):
#         print("*", end=" ")
#     for j in range(0,i,1):
#         print(" ", end=" ")
#     for j in range(0,i,1):
#         print(" ", end=" ")
#     for j in range(n,i,-1):
#         print("*", end=" ")
#     print()
# for i in range(0,n,1):
#     for j in range(0,i+1,1):
#         print("*", end=" ")
#     for j in range(n,i+1,-1):
#         print(" ", end=" ")
#     for j in range(n,i+1,-1):
#         print(" ", end=" ")
#     for j in range(0,i+1,1):
#         print("*", end=" ")
#     print()

# Pattern 19

# n = int(input("Enter No: "))
#
# for i in range(0,n,1):
#     for j in range(0,i+1,1):
#         print("*",end=" ")
#     for j in range(n,i+1,-1):
#         print(" ", end=" ")
#     for j in range(n,i+1,-1):
#         print(" ", end=" ")
#     for j in range(0,i+1,1):
#         print("*", end=" ")
#     print()
# for i in range(1,n,1):
#     for j in range(n,i,-1):
#         print("*",end=" ")
#     for j in range(0,i,1):
#         print(" ", end=" ")
#     for j in range(0,i,1):
#         print(" ", end=" ")
#     for j in range(n,i,-1):
#         print("*", end=" ")
#     print()

# Pattern 20

# n= int(input("Enter No: "))
#
# for i in range(0,n+1,1):
#     for j in range(0,i,1):
#         if i==n or j==0:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     for j in range(n,i,-1):
#         if i==0 or j==i+1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# Pattern 21

# n = int(input("Enter No: "))
# temp=1
# for i in range(0,n,1):
#     for j in range(0,i,1):
#         print(temp,end=" ")
#         temp = temp+1
#     print()

# Pattern 22

# n = 6
# for i in range(0,n,1):
#     for j in range(0,i,1):
#         if i%2==1 or j%2==0:
#             print("1", end=" ")
#         else:
#             print("0", end=" ")
#     print()

# Pattern : 23

# n = int(input("Enter No: "))
# for i in range(0,n,1):
#     for j in range(n,i,-1):
#         if j==i+1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     for j in range(0,i,1):
#         print(" ", end=" ")
#     for j in range(0,i,1):
#         if j==i-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     for j in range(n,i+1,-1):
#         print(" ", end=" ")
#     for j in range(n-1,i,-1):
#         if j==i+1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     for j in range(0,i,1):
#         print(" ", end=" ")
#     for j in range(0,i,1):
#         if j==i-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#
#     print()

# Pattern 24

# n = int(input("Enter No: "))
#
# for i in range(1,n+1,1):
#     for j in range(0,i,1):
#         if j==0 or j==i-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     for j in range(n,i,-1):
#         print(" ", end=" ")
#     for j in range(n,i,-1):
#         if j==i+1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     for j in range(1,i,1):
#         if j==i-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#
# for i in range(0,n,1):
#     for j in range(n,i,-1):
#         if j==n or j==i+1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     for j in range(0,i,1):
#         print(" ",end=" ")
#     for j in range(0,i,1):
#         if j==i-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     for j in range(n-1,i,-1):
#         if j == 0 or j == i+1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#
#     print()

# Pattern 25

# no = int(input("Enter No: "))
#
# for i in range(0,no+1,1):
#     for j in range(no,i,-1):
#         print(" ",end="")
#     for j in range(0, i, 1):
#         if i==no or j==0:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     for j in range(no,i,-1):
#         if i==0 or j==i+1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# Pattern 26

# no =  int(input("Enter No: "))
#
# for i in range(0,no,1):
#     for j in range(no,i,-1):
#         print(i+1,end=" ")
#     print()

# Pattern 27

no = 4
temp = 0
for i in range(0,no,1):
    for j in range(0,i+1,1):
        print(" ",end=" ")
    for j in range(no,i,-1):
        print(temp+1,end=" ")
        temp = temp + 1
    print()


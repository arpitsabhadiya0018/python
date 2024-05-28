
# [7,0,4,14,3,8,6]


# no_of_elements = int(input("Enter No of Element:"))
# print(no_of_elements)
#
# list_1 = []
#
# for i in range(0,no_of_elements,1):
#     element = int(input("Enter Elements: "))
#     list_1.append(element)
#
# print(list_1)
#
# total = 0
# for i in list_1:
#     total = total + i
#
# ls1 = []
# ls2 = []
# for i in list_1:
#     if i%2==0:
#         ls1.append(i)
#     else:
#         ls2.append(i)
#
#
# ls1_sum=0
# ls2_sum=0
# for i in ls1:
#     ls1_sum+=i
# for i in ls2:
#     ls2_sum+=i
#
# diff = ls1_sum-ls2_sum
#
# for i in list_1:
#     if i==diff/2:
#         ls2.append(i)
#         ls1.remove(i)
#         break
#
# sum_ls1=0
# sum_ls2=0
# for i in ls1:
#     sum_ls1 +=  i
# for i in ls2:
#     sum_ls2 +=  i
#
# print("ls1 : ", ls1)
# print("ls2 : ", ls2)
# if sum_ls1 == sum_ls2:
#     print("ls1 : ", ls1)
#     print("ls2 : ", ls2)
# else:
#     print("Both Sum is not Possible")
#
# print("Sum Of list 1",sum_ls1)
# print("Sum Of list 2",sum_ls2)
# **************************************************************************

no_of_elements = int(input("Enter No of Element:"))

list_1 = []

for i in range(0,no_of_elements,1):
    element = int(input("Enter Elements: "))
    list_1.append(element)

print(list_1)
list_1.sort(reverse=True)

list_1_sum = sum(list_1)

print(list_1_sum)

divide_sum = list_1_sum // 2

# for i in list_1:
#
#     if i > divide_sum:
#         print("List Impossible")
#         break
#     else:
#         print("List Possible")
#         break

list_2 = []
list_3 = []

c_sum = 0

for i in list_1:
    if c_sum+i<=divide_sum:
        list_2.append(i)
        c_sum += i
    else:
        list_3.append(i)

print("List 2: ",list_2)
print("List 3: ",list_3)
print()
print("Sum of List 2: ",sum(list_2))
print("Sum of List 3: ",sum(list_3))




















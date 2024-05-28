ls = [6,7,2,8,9,2,3,5,9,6,7,8]

# output: ls1=[[6,7],[2,8,9],[2,3,5,9],[6,7,8]]


# for i in ls:
#     j = i
#     sublist = []
#     if j>i:
#         sublist.append(j)
#     else:
#         sublist.append(j)
#     ls1.append(sublist)
#
# print(ls1)

# ls1=[]
# temp = 0
# for i in range(0,len(ls),1):
#     if ls[i]>=temp:
#         sublist = []
#         sublist.append(ls[i])
#         ls1.append(sublist)
#     else:
#         sublist=[]
#         sublist.append(ls[i])
#         ls1.append(sublist)
#     temp = ls[i]
#
# print(temp)
# print(ls1)

# ls1=[]
# temp = 0
#
# for i in ls:
#     # print(i)
#     if i>=temp:
#         sublist=[]
#         sublist.append(i)
#         ls1.extend(sublist)
#     else:
#         sublist=[]
#         sublist.append(i)
#         ls1.extend(sublist)
#     temp = i
# print(ls1)

ls1=[[]]

for i in range(0,len(ls),1):
    if i <len(ls)-1 and ls[i]< ls[i+1]:
        ls1.append(ls[i])
    else:
        ls1.append(ls[i])
    # print(ls[i])
print(ls1)
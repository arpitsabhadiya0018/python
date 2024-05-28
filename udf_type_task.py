# ******************
# TYPES OF UDF TASK
# ******************

# def all_list(no_ls):
#
#     ls = []
#     for i in range(0,no_ls,1):
#         element = int(input("How many Elements You want to Enter {}:".format(i+1)))
#         new_ls = []
#         for j in range(0,element,1):
#             ele = int(input("Enter Element {}:".format(j+1)))
#             new_ls.append(ele)
#         ls.append(new_ls)
#
#     return ls
#
#
#
#
# no_ls = int(input("Enter the number of lists: "))
# ls = all_list(no_ls)
# print("Lists created: ", ls)

def all_list(*a):
    if len(a)==1:
        print("List 1: ",ls1)
    elif len(a)==2:
        for i in range(0,len(ls2),1):
            ls1.append(ls2[i])
        print("Concated List 1 and 2: ",ls1)
        print("Minimum Element: ",min(ls1))
        print("Maximum Element: ", max(ls1))
    elif len(a)==3:
        for i in range(0,len(ls2),1):
            ls1.append(ls2[i])
        for i in range(0,len(ls3),1):
            ls1.append(ls3[i])
        print("Sum of all List: ",sum(ls1))


no = int(input("Enter No of Lists: "))

if no==1:
    ls1=[]
    ele = int(input("Enter No of Element: "))
    for i in range(0,ele,1):
        list_ele = int(input("Enter Element: "))
        ls1.append(list_ele)
    all_list(ls1)

elif no==2:
    ls1=[]
    ls2=[]

    ele1 = int(input("Enter No of Element: "))
    for i in range(0,ele1,1):
        list_ele = int(input("Enter Element: "))
        ls1.append(list_ele)

    ele2 = int(input("Enter No of Element: "))
    for i in range(0, ele2, 1):
        list_ele = int(input("Enter Element: "))
        ls2.append(list_ele)
    all_list(ls1,ls2)

elif no==3:
    ls1=[]
    ls2=[]
    ls3=[]

    ele1 = int(input("Enter No of Element: "))
    for i in range(0,ele1,1):
        list_ele = int(input("Enter Element: "))
        ls1.append(list_ele)

    ele2 = int(input("Enter No of Element: "))
    for i in range(0, ele2, 1):
        list_ele = int(input("Enter Element: "))
        ls2.append(list_ele)

    ele3 = int(input("Enter No of Element: "))
    for i in range(0, ele3, 1):
        list_ele = int(input("Enter Element: "))
        ls3.append(list_ele)
    all_list(ls1,ls2,ls3)


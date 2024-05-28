# ********
# Task
# ********


# Output
# dict_1 = {1:1,2:4,3:9,4:16,5:25}
# dict_2 = {1:1,2:8,3:27,4:64,5:125}
# dict_3 = {1:[1,1],2:[4,8],3:[9,27],4:[16,64],5:[25,125]}




no = int(input("Enter No: "))
list_dict_key = []
list_dict_value_1=[]
list_dict_value_2 =[]

for i in range(0,no,1):
    list_dict_key.append(i+1)

dict_1 = dict.fromkeys(list_dict_key)
dict_2 = dict.fromkeys(list_dict_key)

for i in dict_1:
    dict_1[i] = i*i

for j in dict_2:
    dict_2[j] = j*j*j

value_1 = dict_1.values()
for i in value_1:
    list_dict_value_1.append(i)

value_2 = dict_2.values()
for i in value_2:
    list_dict_value_2.append(i)


dict_3 = {}
for i in range(0,no,1):

    dict_3["{}".format(i+1)] = [list_dict_value_1[i],list_dict_value_2[i]]


print("Dict_1 : ",dict_1)
print("Dict_2 : ",dict_2)
print("Dict_3 : ", dict_3)


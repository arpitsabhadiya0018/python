#
# def data_write(no_of_line):
#     for i in range(0, no_of_line,1):
#         fo.seek(0,2)
#         data = input("Enter Line: ")
#         fo.write(data+"\n")
#
# def data_read():
#     fo.seek(0,0)
#     str = fo.read()
#     print("Data From File_1: ",str)
#     return str
#
# def fo_2_data_write(file_1):
#     file_1_dummy = file_1.split("\n")
#     file_1_dummy.pop()
#     file_1_dummy.reverse()
#     length = len(file_1_dummy)
#
#     for i in range(0,length,1):
#         fo_2.write(file_1_dummy[i]+"\n")
#
# def fo_2_data_read():
#     fo_2.seek(0, 0)
#     str_2 = fo_2.read()
#     print("Data From File_2(Reverse Data): ", str_2)
#     return str_2
#
# def word_replace(data_read):
#     a = input("Which Word you want to change: ")
#     b = input("Replace Word: ")
#     data_replace = data_read.replace(a,b)
#     print(data_replace)
#
#
# fo_path = "C:/Users/Arpit/PycharmProjects/pract/Task/file_io/demo_task_2.txt"
# fo = open(fo_path,"r+")
#
# no_of_line = int(input("Enter No of Lines: "))
#
# data_write(no_of_line)
# file_1 = data_read()
#
# fo_2_path = "C:/Users/Arpit/PycharmProjects/pract/Task/file_io/dummy.txt"
# fo_2 = open(fo_2_path,"r+")
#
# fo_2_data_write(file_1)
# data_read = fo_2_data_read()
#
# word_replace(data_read)


# line = input("How Many Lines You Want to Enter: ")

# fo_1_path = "C:/Users/Arpit/PycharmProjects/pract/Task/file_io/demo_task_2.txt"
# fo_2_path = "C:/Users/Arpit/PycharmProjects/pract/Task/file_io/dummy.txt"
# fo_1 = open(fo_1_path,"r+")
#
# fo_1.writelines("Hello java bhjkl \n hello python \n hello developer")
# fo_1.seek(0,0)
# data = fo_1.readlines()
# print(data)

def data_write(no_of_line):
    ls = []
    for i in range(0, no_of_line, 1):
        data = input("Enter Line: ")
        ls.append(data + "\n")
    fo.writelines(ls)

def data_read():
    fo.seek(0, 0)
    str_read = fo.readlines()
    str_read.reverse()
    for i in range(0, len(str_read), 1):
        fo_dummy.seek(0, 2)
        fo_dummy.writelines(str_read[i])
    fo_dummy.seek(0, 0)
    fo_dummy.readlines()


def replace_word():
    fo_dummy.seek(0, 0)
    str_2 = fo_dummy.readlines()
    for i in range(0, len(str_2), 1):
        fo_dummy.seek(0, 2)
        replace = str_2[i].replace("Hello", "Hi")
        fo_dummy.writelines(replace)
    fo_dummy.seek(0, 0)
    fo_dummy.readlines()


fo_1_path = "C:/Users/Arpit/PycharmProjects/pract/Task/file_io/demo_task_2.txt"
fo_2_path = "C:/Users/Arpit/PycharmProjects/pract /Task/file_io/dummy.txt"

fo = open(fo_1_path, "w+")
fo_dummy = open(fo_2_path, "w+")
no_of_line = int(input("Enter No of Lines: "))

data_write(no_of_line)
data_read()
replace_word()

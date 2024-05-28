
def data_write(lines):
    for i in range(0, lines, 1):
        data = input("Enter Data: ")
        file_object.seek(0, 2)
        file_object.write(data + "\n")

def data_read():
    file_object.seek(0, 0)
    str = file_object.read()
    print("Data From File: \n",str)
    return str

file_path =  "C:/Users/Arpit/PycharmProjects/pract/Task/file_io/demo.txt"
file_object = open(file_path,"r+")

lines = int(input("Enter No of lines: "))

data_write(lines)
read = data_read()

line = read.split("\n")
words = read.split()

wsc = read.split()
char = "".join(wsc)

print("No of Lines In file: ",len(line)-1)
print("Words In File: ",len(words))
print("Character With Space: ",len(read)-1)
print("Character Without Space: ", len(char))




# List Function Task
a = input("Enter Items: ")

b = [a]
intList = []
strList = []

c = a.split(',')

for i in c:
    str(i)
    if i.isdigit():
        intList.append(int(i))
    else:
        strList.append(i)

print("Int List:", intList)
print("String List:", strList)

print("Int List Min No: ",min(intList))
print("Int List Max No: ",max(intList))

strList.reverse()

print("Str List In Reverse: ", strList)
data = str(input())
list = []

length = len(data)

for i in range(length):
    list.append(ord(data[i]))

#print(list)

maximum = max(list)

#print(maximum)
count = 0

for i in range(length):
    if list[i] == maximum:
        count += 1

string = chr(maximum)

for k in range(count):
    print(string)
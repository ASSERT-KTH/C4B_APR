string = input()
list1 = []
num1 = "47"
for i in string:
    if (i in num1):
        list1.append(i)
        continue
    elif(i not in num1):
        break
if(len(list1) != len(string)):
    if(int(string)%47 == 0):
        print("YES")
    else:
        print("NO")
else:
    print("YES")
#Codeforces Beta Round #77
#Football

n = int(input())
temp = str(n)
count = 0
flag = 0
for i in range(len(temp)-1):    
    if temp[i] == temp[i+1]:
        count += 1
        if count>=6:
            flag = 1
            print("YES")
            break;
    if temp[i] != temp[i+1]:
        count = 0
if flag == 0:
    print("NO")
import math
n = int(input())
if n != 1:
    print(n,end=" ")
flag = True
while n > 1 and flag:
    flag = False
    for i in range(2,int(math.sqrt(n))+1) :
        if n%i == 0 :
            print(n//i,end=" ")
            n = n//i
            flag = True
            break  
print(1)
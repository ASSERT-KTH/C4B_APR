import math
def isTPrime(n):
    count = 0
    if n==2 or n==3: return False
   # print(2,math.ceil(int(n**0.5))+3)
    for i in range(2,math.ceil(int(n**0.5))+3):   # only odd numbers
        if i == n:
            break
        if n%i==0:
            count +=1
        if count == 2:
            break
    if count == 1:
        return True
    else:
        return False
n = int(input())
list = [int(n) for n in input().split()]

for num in list:
    if isTPrime(num):
        print("YES")
    else:
        print("NO")
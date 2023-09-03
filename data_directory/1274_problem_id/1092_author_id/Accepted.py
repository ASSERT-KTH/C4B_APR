k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
contador = -1
if k<=d and l<=d and m<=d and n<=d:
    for i in range(d+1):
        if (i%k==0) or (i%l==0) or (i%m==0) or (i%n==0):
            contador +=1
    print(contador)
else:
    print('0')
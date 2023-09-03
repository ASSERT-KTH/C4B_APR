k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
contador = 0
if k<=d and l<=d and m<=d and n<=d:
    for i in range(d):
        if (i%k!=0) and (i%l!=0) and (i%m!=0) and (i%n!=0):
            contador +=1
    print(d-contador)
else:
    print('0')
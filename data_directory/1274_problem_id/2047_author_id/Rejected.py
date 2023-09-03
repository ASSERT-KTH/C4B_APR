k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

i = 0
x = 0


if(k == 1 or l == 1 or m == 1 or n == 1):
    x = d

else:
    while(i<=d-1):
        if(i%k == 0):
            x += 1
        elif(i%l == 0):
            x += 1
        elif(i%m == 0):
            x += 1
        elif(i%n == 0):
            x += 1
        i += 1

print(x)
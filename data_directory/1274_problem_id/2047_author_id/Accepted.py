k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

i = 1
x = 0

while(i<=d):
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
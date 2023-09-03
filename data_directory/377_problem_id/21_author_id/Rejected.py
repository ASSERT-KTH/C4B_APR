a = int(input())
b = int(input())

c = 0

while a>0 and b>0 and a+b>2 :
    if a < b:
        a += 1
        b -= 2
    else:
        a -= 2
        b += 1
    c += 1

print(c)
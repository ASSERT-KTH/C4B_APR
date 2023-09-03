a = int(input())
b = int(input())
c = int(input())

count = 0

while a > 0 and b > 0 and c > 0:
    a -= 1
    b -= 2
    c -= 4
    count += 7

print(count-7)
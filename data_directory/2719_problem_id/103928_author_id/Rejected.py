def bigyears(a, b):
    n = 0
    while a <= b :
        a = a * 3
        b = b * 2
        n = n + 1
    return n

a = int(input())
b = int(input())
print(bigyears(a, b))
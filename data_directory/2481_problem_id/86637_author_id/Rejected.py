import math

n = int(input())
names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
def func1(n):
    i = 1
    j = 0
    while(i * 10 - 4 <= n):
        j = i * 10 - 4
        i = i * 2
    return (i, j)

def func2(n):
    a = func1(n)
    b = math.floor((n - a[1])/a[0])
    return b


name = func2(n)
print(names[name])
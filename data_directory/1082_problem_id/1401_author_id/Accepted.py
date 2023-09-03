k = int(input())
l = int(input())

n = 0
while k ** n <= l:
    if (k ** n == l):
        print("YES")
        print(n - 1)
        exit()
    n += 1
print("NO")
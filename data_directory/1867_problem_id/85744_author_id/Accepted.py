n = input()
n = int(n)
if n <= 2:
    print(-1)
elif n <= 50:
    result = [i for i in range(n, 0, -1)]
    for el in result:
        print(el, end=' ')
else:
    print(-1)
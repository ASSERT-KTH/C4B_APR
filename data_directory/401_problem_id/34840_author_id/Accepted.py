n = int(input())
if n >= 13:
    print(8092 * 2 ** (n - 13))
else:
    print(2 ** n)
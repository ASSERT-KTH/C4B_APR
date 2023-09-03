string = input()
n, a, b = map(int, string.split())
def check(p, q):
    return p % n != 0 and q < n
if check(a, b) or check(b, a):
    print(-1)
else:
    print(a // n + b // n)
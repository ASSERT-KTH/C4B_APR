n, a, b, c = map(int, input().split())

mod = n % 4
if mod == 0:
    print(0)
elif mod == 1:
    print(min(3 * a, c, a + b))
elif mod == 2:
    print(min(2 * a, b, 2 * c))
elif mod == 3:
    print(min(a, 3 * c, b + c))
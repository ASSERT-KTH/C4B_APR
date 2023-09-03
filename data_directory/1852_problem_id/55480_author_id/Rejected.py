n = input()
a = int(n[0])
l = len(n)
d = 1 << (l - 1)

def f(a, i):
    global n, l
    if i == l: return 0
    b = int(n[i])
    i += 1
    d = 1 << (l - i)
    if a > b: return b * d + g(a, b, i)
    if a == b: return b * d + f(a, i)
    return (b - 1) * d + g(a, b, i) + 9 * (d >> 1)
        
def g(a, b, i):
    if i == l: return 0
    c = int(n[i])
    d = 1 << (l - i - 1)
    if a > b: a, b = b, a
    if c < a: return 0
    if c == a: return g(a, b, i + 1)
    if c < b: return d
    if c == b: return d + g(a, b, i + 1)
    return 2 * d

print(a * (9 * d - 8) + 72 * (d - l) + f(a, 1))
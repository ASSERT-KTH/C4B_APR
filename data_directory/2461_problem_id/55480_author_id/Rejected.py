def f(a, b):
    k = min(a, 2)
    return a - k, b - 22 + 10 * k

def g(a, b):
    if b > 21: return a, b - 22
    if b > 11: return a - 1, b - 12
    if b > 1: return a - 2, b - 2

def main():
    a, b = map(int, input().split())
    k = min(a // 2, b // 24)
    a -= 2 * k
    b -= 24 * k
    
    while a > 0:
        a, b = f(a, b)
        if a < 0 or b < 0: return 0
        a, b = g(a, b)
        if a < 0 or b < 0: return 1
    if a == 0: return (b // 22) % 2

print(['Hanako', 'Ciel'][main()])
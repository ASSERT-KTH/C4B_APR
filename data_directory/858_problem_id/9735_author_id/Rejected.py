import math
def main():
    n, a, b, c = map(int, input().split())
    n = (4 - (n%4)) % 4
    if n == 0:
        print(0)
    elif n == 1:
        print(min(a, 3*c))
    elif n == 2:
        print(min(2*a, b, 2*c))
    elif n == 3:
        print(min(3*a, c, a + b))

main()
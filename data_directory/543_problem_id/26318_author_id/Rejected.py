def main():
    n = int(input())
    p = funct(n)
    if p == 1:
        print("YES")
    else:
        print("NO")


def funct(n):
    a = 0
    while a <= n:
        b = 0
        while b <= n - a:
            #print("a = {}, b = {}".format(a, b))
            if (n - a - b) % 1234 == 0:
                print("True")
                return 1
            else:
                b += 123456
        a += 1234567
    return 0

main()
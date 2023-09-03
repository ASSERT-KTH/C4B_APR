if __name__ == '__main__':
    n = int(input())
    if n < 3:
        print(n)
    elif n % 2 > 0:
        print(n * (n - 1) * (n - 2))
    elif n % 3 > 0:
        print(n * (n - 1) * (n - 3))
    else:
        print((n - 1) * (n - 2) * (n - 3))
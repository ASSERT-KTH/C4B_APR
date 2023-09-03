def gcd(num1, num2):
    i = min(num1, num2)
    while i > 0:
        if num1 % i == 0 and num2 % i == 0:
            return i
        i -= 1

if __name__ == "__main__":
    [a, b, n] = [int(x) for x in input().split()]
    turn = 's'

    while True:
        if turn == 's':
            simon = gcd(a, n)
            if n - a >= 0:
                n -= simon
                turn = 'a'
            else:
                print("1")
                exit()
        else:
            anti_simon = gcd(b, n)
            if n - b >= 0:
                n -= anti_simon
                turn = 's'
            else:
                print("0")
                exit()
def main():
    x = list(map(int, input()))

    i = 0
    while x[i] == 9 and i < len(x) - 2:
        i += 1

    if x[i] == 0:
        i -= 1

    sum1 = x[i] - 1 + 9 * (len(x) - 1)
    sum2 = sum(x)

    y1 = int('9' * i + str(x[i] - 1) + '9' * (len(x) - i - 1))
    y2 = int(''.join(map(str, x)))

    if sum1 > sum2:
        print(y1)
    elif sum2 > sum1:
        print(y2)
    else:
        print(max(y1, y2))


if __name__ == '__main__':
    # import sys
    # sys.stdin = open("B.txt")
    main()
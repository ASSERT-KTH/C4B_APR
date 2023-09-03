if __name__ == '__main__':
    n = int(input())
    flag = False
    num4 = num7 = 0
    while n >= 0:
        if n % 4 == 0:
            num4 = n // 4
            break
        else:
            n -= 7
            num7 += 1
    if n < 0:
        print('-1')
    else:
        print('4' * num4 + '7' * num7)
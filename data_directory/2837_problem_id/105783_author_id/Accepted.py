n = int(input())


def happy(n):
    numbers = [0] * 10
    while n != 0:
        mod = n % 10
        numbers[mod] += 1
        n //= 10
    count = 0
    for i in range(1, 10):
        if numbers[i] > 0:
            count += numbers[i]
            if count > 1:
                return False
                break
    return True


def isHappy(n):
    if len(str(n)) == 1:
        return 1
    if happy(n) == True:
        return 10 ** (len(str(n)) - 1)
    else:
        return 10 ** (len(str(n)) - 1) - n % (10 ** (len(str(n)) - 1))

print(isHappy(n))
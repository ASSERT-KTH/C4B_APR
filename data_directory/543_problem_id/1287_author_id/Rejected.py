if __name__ == '__main__':
    n = int(input())
    na = n // 1234567 + 1
    nb = n // 123456 + 1
    flag = False
    for a in range(na):
        for b in range(nb):
            if (n - a * 1234567 - b * 123456) % 1234 == 0:
                flag = True
                break
        if flag:
            break
    print('YES') if flag else print('NO')
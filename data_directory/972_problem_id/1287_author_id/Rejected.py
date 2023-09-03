if __name__ == '__main__':
    a, b = str(input()).split()
    a, b = int(a), int(b)
    if -1 <= a - b <= 1:
        print('YES')
    else:
        print('NO')
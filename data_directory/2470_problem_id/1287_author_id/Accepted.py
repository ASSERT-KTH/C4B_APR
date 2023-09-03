if __name__ == '__main__':
    refer = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
    n, m = str(input()).split()
    n, m = int(n), int(m)
    if refer[refer.index(n) + 1] == m:
        print('YES')
    else:
        print('NO')
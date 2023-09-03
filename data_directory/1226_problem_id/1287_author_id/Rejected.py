if __name__ == '__main__':
    n = int(input())
    line = str(input()).split()
    line = [int(it) for it in line]
    n %= sum(line)
    if n == 0:
        n = sum(line)
    else:
        temp = 0
        for i in range(7):
            temp += line[i]
            if temp >= n:
                print(i + 1)
                break
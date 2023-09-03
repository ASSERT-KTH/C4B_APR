if __name__ == '__main__':
    line0 = str(input()).split()
    line0 = [int(it) for it in line0]
    line1 = str(input()).split()
    line1 = [int(it) for it in line1]
    line = [it0 - it1 for it0, it1 in zip(line0, line1)]
    num = 0
    flag = False
    for it in line:
        if it > 1:
            flag = True
        num += it * (1 if it > 0 else 2)
    if flag and not num < 0:
        print('Yes')
    else:
        print('No')
if __name__ == '__main__':
    ff = list(map(int, input().split()))
    tt = list(map(int, input().split()))
    foo = too = 0
    for i in range(3):
        if ff[i] < tt[i]:
            too += tt[i] - ff[i]
        else:
            foo += (ff[i] - tt[i]) // 2
    print('No') if foo < too else print('Yes')
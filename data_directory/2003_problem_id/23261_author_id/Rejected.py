n = input()
for i in range(int(n) + 1, 9001):
    tmp = str(i)
    if tmp[0] != tmp[1] and tmp[0] != tmp[2] and tmp[0] != tmp[3] and tmp[1] != tmp[2] and tmp[1] != tmp[3] and tmp[2] != tmp[3]:
        print(tmp)
        break
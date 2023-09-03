b = [0] * 4
b[0] = int(input())
b[1] = int(input())
b[2]= int(input())
b[3] = int(input())
d = int(input())
if 1 in b:
    print(d)
else:
    l = 0
    for i in range(1, d + 1):
        for j in range(4):
            if i % b[j] == 0:
                l += 1
                break
    print(l)
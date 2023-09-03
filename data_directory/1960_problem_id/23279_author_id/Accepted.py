for i in range(5):
    s = [int(i) for i in input().split()]
    for j in range(5):
        if s[j] == 1:
            x = i
            y = j
            break
print(abs(x-2)+abs(y-2))
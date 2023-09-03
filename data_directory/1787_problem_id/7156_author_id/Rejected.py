n = int(input())

if(n % 2 > 0) :
    print(-1)
else :
    list = []

    for i in range(1, n + 1) :
        if(i % 2 > 0) :
            list.append(i - 1)
        else :
            list.append(i + 1)

    print(*list)
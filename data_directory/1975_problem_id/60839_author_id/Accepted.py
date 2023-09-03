n,t = map(int,input().split())
line = list(input())
i = 0
while t > 0 and n > 1:
    if line[i] == 'B' and line[i+1] == 'G':
        line[i],line[i+1] = line[i+1],line[i]
        i += 2
        if i >= len(line)-1:
            t -= 1
            i = 0
    else:
        i += 1
        if i >= len(line)-1:
            t -= 1
            i = 0
print(''.join(list(line)))
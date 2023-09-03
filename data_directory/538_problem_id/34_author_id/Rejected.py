l = list(map(int, input().split()))
l.append(0)
l.sort(reverse = True)
if l[0] == l[2]: 
    print(sum(l[3:]))
    exit(0)
elif l[1] == l[3]: 
    print(sum(l[0], l[4]))
    exit(0)
elif l[2] == l[4] and l[0] == l[1]: 
    print(min(sum(l[:2]), sum(l[2:])))
    exit(0)
elif l[2] == l[4]:
    print(l[0] + l[1])
    exit(0)
else:
    for i in range(4): 
        if l[i] == l[i + 1]:
            l.pop(i)
            l.pop(i)
            print(sum(l))
            exit(0)
print(sum(l))
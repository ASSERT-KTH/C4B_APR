l = sorted(list(map(int,input().split())))
p = l[len(l)//2]
sh = 0
for i in l:
    sh += abs(i-p)
print(sh)
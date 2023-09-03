l = list(map(int,input().split()))
p = sum(l)//len(l)
sh = 0
for i in l:
    sh += abs(i-p)
print(sh)
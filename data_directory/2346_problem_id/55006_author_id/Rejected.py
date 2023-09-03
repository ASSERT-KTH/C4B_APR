a,b,c,d = map(int,input().split())
l = [a,b,c,d]
k = max(l)
for x in l:
    if x == k:
        l.remove(x)
        break
if ((l[0] + l[1] > k) or (l[0] + l[2] > k) or (l[1] + l[2] > k)):
    print("TRIANGLE")
elif ((l[0] + l[1] == k) or (l[0] + l[2] == k) or (l[1] + l[2] == k)):
    print("SEGMENT")
else:
    print("IMPOSSIBLE")
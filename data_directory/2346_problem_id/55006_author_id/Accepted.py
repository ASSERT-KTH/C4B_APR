a,b,c,d = map(int,input().split())
l = [a,b,c,d]
l = sorted(l)
if ((l[0] + l[1] > l[3]) or (l[0] + l[2] > l[3]) or (l[1] + l[2] > l[3]) or (l[0] + l[1] > l[2])):
    print("TRIANGLE")
elif((l[0] + l[1] == l[3]) or (l[0] + l[2] == l[3]) or (l[1] + l[2] == l[3]) or (l[0] + l[1] == l[2])):
    print("SEGMENT")
else:
    print("IMPOSSIBLE")
n = int(input())
ans = n%4
if n == 0:
    print (1)
elif ans == 1:
    print (8)
elif ans == 2:
    print (4)
elif ans == 3:
    print (2)
else:
    print (6)
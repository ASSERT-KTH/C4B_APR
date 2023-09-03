l1 ,r1, l2, r2, k = map(int, input().split())
if l2 > r1 or l1 > r2:
    print(0)
elif l2 >= l1 and r2 <= r1:
    print(r2 - l2 + 1 - (k >= l2 and k <= r2))
elif l1 >= l2 and r1 <= r2:
    print(r1 - l1 + 1 - (k >= l1 and k <= r1))
elif l2 >= l1:
    print(r1 - l2 + 1 - (k >= l2 and k <= r1))
elif l1 >= l2:
    print(r2 - l1 + 1 - (k >= l1 and k <= r2))
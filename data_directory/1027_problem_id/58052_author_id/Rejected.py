import sys
f = sys.stdin
#f = open("input.txt", "r")
a = f.readline().strip()
c = set(i*2 for i in a)
a1 = a
for i in range(len(a)-1):
    if a[i] == a[i+1]:
        a1 = a1.replace(a[i], "", 2)

print(*a1, sep="")

# def cntIt(i):
#     global a
#     return a.count(i)
#
# def cd():
#     global c
#     cnt = {}
#     pool = Pool()
#     cs = pool.map(cntIt, c)
#     for i, k in zip(c, cs):
#         if k > 0:
#             cnt[i] = k
#     return cnt
#
# def solve(ex=cd()):
#     global a
#     for i in ex:
#         a = a.replace(i, "", ex[i])
#     if cd() == {}:
#         return a
#     else:
#         return solve(cd())
# print(solve())
"""
DO NOT ASSUME THAT  K<=L
"""

k = int(input())
l = int(input())
count = 0
res = True
if k>l:
    res = False
while l>=k and res:
    if l%k != 0:
        res = False
        break
    l//= k
    count += 1

if res:
    print("YES")
    print(count-1)
else:
    print("NO")
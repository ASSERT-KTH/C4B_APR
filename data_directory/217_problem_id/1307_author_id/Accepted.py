n = int(input())
i = 0

def bsearch(l,r,v):
    mid = (l + r)//2
    if l > r:
        return r
    if ((mid *(mid + 1))//2)<= v:
        return bsearch(mid +1,r,v)
    return bsearch(l, mid - 1,v)
r = bsearch(1,10 ** 14,n)
x = (r * (r+1))//2;
if x == n:
    print(r)
else:
    print(n - x)
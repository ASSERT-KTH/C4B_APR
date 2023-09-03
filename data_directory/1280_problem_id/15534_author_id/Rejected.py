k=int(input())
A=[int(i) for i in input().split()]
A.sort()
num=-1
need=0
while need<k:
    need+=A[num]
    num-=1
    if abs(num)>len(A):
        break
if abs(num)>len(A):
    print(-1)
else:
    print(abs(num)-1)
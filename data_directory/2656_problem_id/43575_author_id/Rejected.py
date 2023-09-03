import sys

n,k = input().split()
k = int(k)
cnt = cnt_zero =  0
if len(n) < k and '0' in n:
    print(len(n)-1)
else:
    for i in range(len(n)-1,-1,-1):
        if n[i] == '0':
            cnt_zero += 1
        else:
            if k > cnt_zero:
                cnt += 1
    print(cnt)
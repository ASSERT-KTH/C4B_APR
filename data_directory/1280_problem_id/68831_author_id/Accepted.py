k = int(input())
a = [int(i) for i in input().split()]
if k==0: print('0')
else:
    a.sort(reverse=True)
    for i in range(12):
        if sum(a[0:i+1])>=k:
            print(i+1);break
    else: print('-1')
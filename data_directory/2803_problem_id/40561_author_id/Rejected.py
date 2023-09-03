n,k = list(map(int,input().strip().split(' ')))
p = n
flag = True
while p>0 :
    if p*(int(n/p)) == n and k <= int(n/p) - int((k*(k-1))/2):
        for i in range(1,k) :
            print(p*i,end=' ')
        print(p*(int(n/p) - int((k*(k-1))/2)))
        flag = False
        break
    p-=1
if flag :
    print(-1)
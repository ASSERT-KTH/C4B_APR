n, k= input().split()

n=int(n)
k=int(k)
nn =n
arr = []
for i in range(k):
    arr.append(n)
    n-=1;
for i in range(nn-k):
    arr.append(i+1)

for i in range(nn):
    print(arr[i],end=" ")
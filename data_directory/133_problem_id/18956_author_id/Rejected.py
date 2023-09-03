a = list(map(int, input().split()))
b = list(map(int, input().split()))

sum1=sum2 = 0
for i in range(0,3):
    if a[i]>b[i]:
        sum1+=(a[i]-b[i])//2
    else:
        sum2+=b[i]-a[i]
if(sum1>sum2):
    print ("Yes")
else:
    print ("No")
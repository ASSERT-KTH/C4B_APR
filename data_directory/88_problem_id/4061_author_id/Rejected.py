n=int(input())
M=[list(map(int,input().split())) for i in range(n)]
a=-1
for i in range(n) :
    for j in range(n) :
        if M[i][0]!=M[j][0] and M[i][1]!=M[j][1] :
            a=([M[i][0],M[i][1]])
            b=([M[j][0],M[j][1]])
if a==-1 :
    print(1)
else :
    c=[a[0],b[1]]
    d=[b[0],a[1]]
    q1=((c[0]-a[0])**2+(c[1]-a[1])**2)**(0.5)
    q2=((c[0]-b[0])**2+(c[1]-b[1])**2)**(0.5)
    print(round(q1*q2))
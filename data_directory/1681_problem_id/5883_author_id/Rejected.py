n,m = map(int, input().split())
a = 0
c = 0
while(a<=m):
    t = pow((n - a*a),2)
    if(t == (m-a)):
        c+=1
    a = a+1
print(c)
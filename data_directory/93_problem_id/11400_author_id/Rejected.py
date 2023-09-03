n,a,b=list(map(int, input().split()));
if a>=0 and b>=0 :
    print(b//n - (a-1)//n);
elif a<0 and b<0 :
    print(-b//n - (-a-1)//n);
else :
    print(b//n + -a//n + 1);
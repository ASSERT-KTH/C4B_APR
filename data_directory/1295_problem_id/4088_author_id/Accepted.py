n,k,l,c,d,p,nl,np=map(int,input().split())
l=k*l
c=d*c
print(min(p//np,c,l//nl)//n)
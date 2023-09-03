n,k,l,c,d,p,nl,np=map(int,input().split())
l=k*l
c=d*c
print(min(l//(nl*n),c,p//(np*n*2)))
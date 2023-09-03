n,k,l,c,d,p,nl,np=map(int,input().split())
S=(k*l)/nl
S1=c*d
S2=p/np
print('%.0f'%(min(S,S1,S2)/n))
A=input()
k=0
while A[k]!='H' and A[k]!='Q' and A[k]!='9' and k<len(A)-1:
    k+=1
if k<len(A)-1:
    print('YES')
else:
    if k==len(A)-1 and (A[k]=='Q' or A[k]=='H' or A[k]=='9'):
        print('YES')
    else:
        print('NO')
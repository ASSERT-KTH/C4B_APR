n=int(input())
e=10**9+7
print((pow(2,n-1,e)+pow(2,n*2-1,e))%e)
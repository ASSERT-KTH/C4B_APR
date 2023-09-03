a=list(map(int,input().split()))
if a[1]>a[0]:print(-1)
else:print('ab'*((a[0]+2-a[1])//2)+'a'*((a[0]-a[1])%2)+''.join(map(lambda x:chr(ord('c')+x),range(a[1]-2))))
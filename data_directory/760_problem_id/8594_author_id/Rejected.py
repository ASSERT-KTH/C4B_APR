n=int(input())
hh,mm=[int(i) for i in input().split(':')]
if mm>59: mm%=10
if n==24:
    if hh>23:
        hh%=10
else:
    if hh>12:
        hh%=10
    elif hh==0:
        hh=1
hh=str(hh)
mm=str(mm)
print(('0' if len(hh)==1 else'')+hh+':'+('0' if len(mm)==1 else '')+mm)
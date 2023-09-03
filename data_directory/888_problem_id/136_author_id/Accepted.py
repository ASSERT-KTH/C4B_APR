a=int(input())
b=int(input())
c=int(input())
cc=c//4
bb=b//2
print(min(cc,bb,a)+2*min(a,bb,cc)+4*min(a,bb,cc))
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
n=0
for i in range(1,e+1):
    if i%a==0 or i%b==0 or i%c==0 or i%d==0:
        n+=1
print(n)
#print(' '.join([str(i) for i in a]))
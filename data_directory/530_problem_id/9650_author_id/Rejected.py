l=input()
l=l.split(' ')
q=int(l.pop())
p=int(l.pop())
b=int(l.pop())
a=int(l.pop())
n=int(l.pop())
somme=0
if p>q:
    somme+=p*(n//a)
    for j in range(1,(n//b)+1):
            if (b*j)%a!=0:
                somme+=q
else:
    somme+=q*(n//b)
    for j in range(1,(n//a)+1):
            if (a*j)%b!=0:
                somme+=p
print(somme)
a,b,c=map(int,input().split())

gem=(a+b+c)//3

afstand=abs(gem-a)+abs(gem-b)+abs(gem-c)

print(afstand)
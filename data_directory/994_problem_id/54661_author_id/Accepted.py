m,n,a = map(int,input().split())
nvag =int(n/a);
mvag=int(m/a);
if n%a!=0:
    nvag+=1
if m%a!=0:
    mvag+=1
print(nvag*mvag)
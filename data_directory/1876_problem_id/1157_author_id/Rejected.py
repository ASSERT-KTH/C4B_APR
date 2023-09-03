n = int(input());
ti = 1;

if(n<=2):
    print(-1);
    exit(0);

n-=2;
while(n):
    n-=1;
    ti*=10;

if(ti%21):
    ti//=21;
    ti+=1;
    ti*=21;
ti*=10;
print(ti);
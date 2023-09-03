import sys;
n=int(input())
for i in range(1,n+1,1):
    if( i*(i+1)/2 == n):
        print("YES");
        sys.exit();
print("NO");
sys.exit();
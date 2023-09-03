[h1, h2] = list(map(int, input().split()))
[a, b] = list(map(int, input().split()))               

if h1+8*a >= h2:
    print(0)
    exit(0)
elif a <= b:
    print(-1)
    exit(0)

d = h1+8*a;
res = int( (h2-d)/(12*(a-b)) );
print(res)
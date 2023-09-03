n, a, b, c = list(map(int, input().split()))
f =[0] +  [50000] * 5000
for i in range(1, n + 1):   
    f[i] = min(f[i - a], f[i - b], f[i - c]) + 1
print(f[n])
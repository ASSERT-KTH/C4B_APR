k, a, b = map(int, raw_input().split())

ans = a // k + b // k
if (a < k and b % k) or (b < k and a % k): 
    ans = -1;

print(ans)
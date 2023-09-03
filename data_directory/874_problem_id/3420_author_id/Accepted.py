def solve(position, size, level):
    if position ==size//2:
        return level
    return solve(abs(position - size//2),size//2,level-1)
n, k = map(int,input().split())
Size = 2**n

print(solve(k,Size,n))
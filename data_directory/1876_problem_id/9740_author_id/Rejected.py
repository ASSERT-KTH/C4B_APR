n = int(input())

cur = 10 ** (n - 1)

ans = 2 * 3 * 5 * 7

nex = cur//ans

print(ans * (nex + 1))
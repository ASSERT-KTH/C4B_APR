import string


n, k = map(int, input().split())

use = string.ascii_lowercase[: k]

for i in range(n):
    print(use[i % k], end='')

input()
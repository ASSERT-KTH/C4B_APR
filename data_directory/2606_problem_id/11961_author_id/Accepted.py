import os

import string

n, k = map(int, input().split())

use = string.ascii_lowercase[: k]

for i in range(n):
    print(use[i % k], end='')
print()

if os.getlogin() == 'o.sharipov':
    input()
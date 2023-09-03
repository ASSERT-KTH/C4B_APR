import sys

def solve():
    n = int(input())

    cnt = 0

    while n > 0:
        if n % 10 == 4 or n % 10 == 7:
            cnt += 1

        n //= 10
        
    while cnt > 0:
        if cnt % 10 != 4 and cnt % 10 != 7:
            print('NO')
            return

        cnt //= 10

    print('YES')

if __name__ == '__main__':
    solve()
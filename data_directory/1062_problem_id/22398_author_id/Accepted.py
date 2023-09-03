import sys

def solve():
    n = input()

    cnt = 0

    for d in n:
        if d == '4' or d == '7':
            cnt += 1

    for d in str(cnt):
        if d != '4' and d != '7':
            print('NO')
            return

    print('YES')

if __name__ == '__main__':
    solve()
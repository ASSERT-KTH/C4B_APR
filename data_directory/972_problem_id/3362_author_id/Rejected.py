#!/usr/bin/env python3

if __name__ == '__main__':
    a, b = map(int, input().split())

    if abs(a - b) > 1:
        print('NO')
    else:
        print('YES')
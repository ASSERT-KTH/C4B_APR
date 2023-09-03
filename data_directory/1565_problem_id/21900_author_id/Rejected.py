a, b, r = map(int, input().split())

w = a // r // 2
h = b // r // 2

print('First' if w * h % 2 else 'Second')
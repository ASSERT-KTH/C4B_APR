n, t = map(int, raw_input().split())
m = raw_input().strip()
m = m + '0'
while t > 0:
    t = t - 1
    for i in range(n):
        if m[i] == 'B' and m[i+1] == 'G':
            m = m[0:i] + m[i+1] + m[i] + m[i+2:]
print(m[0:n])
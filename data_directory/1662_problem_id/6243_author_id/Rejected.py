def check(s):
    for i in s:
        ok = False
        for j in range(26):
            if i == chr(ord('a') + j):
                ok = True
        for j in range(10):
            if i == chr(ord('0') + j):
                ok = True
        if i == '_':
            ok = True
        if not ok:
            return False
    return True

s = input().split()[0]
t = s.split('@')
if (len(t) != 2):
    print("NO")
    exit(0)
if len(t[0]) == 0 or len(t[0]) > 16 or (not check(t[0])):
    print("NO")
    exit(0)
t = s.split('@')[1].split('/')
if (len(t) > 2):
    print("NO")
    exit(0)
if len(t[0]) > 32 or len(t[0]) == 0:
    print("NO")
    exit(0)
for i in t[0].split('.'):
    if len(i) == 0 or len(i) > 16 or (not check(i)):
        print("NO")
        exit(0)
for i in t[1:]:
    if len(i) == 0 or len(i) > 16 or (not check(i)):
        print("NO")
        exit(0)
print("YES")
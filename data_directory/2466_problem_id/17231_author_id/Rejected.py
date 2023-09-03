a, b, c = input(), input(), input()

def check(a):
    i, j = 0, 0

    for x in a:
        if i < len(b):
            if x == b[i]:
                i += 1
            else:
                i = 0
        elif j < len(c):
            if x == c[j]:
                j += 1
            else:
                j = 0
        else:
            break
    
    return j == len(c)

f = check(a)
b = check(reversed(a))

if f and b:
    print("both")
elif f:
    print("forward")
elif b:
    print("backward")
else:
    print("fantasy")
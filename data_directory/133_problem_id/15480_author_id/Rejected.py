a, b, c = map(int, input().split())
x, y, z = map(int, input().split())

need = max(x-a,0) + max(y-b,0) + max(z-c,0)

extra = max(a-x,0) + max(b-y,0) + max(c-z,0)

if need * 2 <= extra:
    print("YES")
else:
    print("NO")
a, b, c = map(int, input().split())
x, y, z = map(int, input().split())

need = max(x-a,0) + max(y-b,0) + max(z-c,0)

extra = max(a-x,0)//2*2 + max(b-y,0)//2*2 + max(c-z,0)//2*2

if need * 2 <= extra:
    print("Yes")
else:
    print("No")
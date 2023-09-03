x, y, z = map(int, input().split())

print(4*int(((x*y//z)**.5 + (x*z//y)**.5 + (z*y//x)**.5)))
s1, s2, ss = [int(x) for x in input().split()]
a = s1 + ss + s2
b = 2*s1 + 2*s2
c = 2*s2 + 2*ss
d = 2*s1 + 2*ss

print(min(a, b, c, d))
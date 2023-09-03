##n = int(input())
##a = list(map(int, input().split()))
##print(" ".join(map(str, res)))

def calc(x, y):
    return int(x/y+1)

[a, ta] = list(map(int, input().split()))
[b, tb] = list(map(int, input().split()))
[hh, mm] = list(map(int, input().split(':')))

bs = 5*60
be = 23*60+59
s = hh*60+mm
e = hh*60+mm+ta

a = calc(max(s-tb, bs-1), b)-calc(bs-1, b)
b = calc(min(e-1, be), b)-calc(bs-1, b)
print(b-a)
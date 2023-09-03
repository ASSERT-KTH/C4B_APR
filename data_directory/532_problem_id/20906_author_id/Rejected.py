import math

def f(m):
    if m < 8: return (m,m)
    c = math.floor(m**(1.0/3))
    if not (c**3 <= m and m < (c+1)**3):
        if ((c+1)**3 <= m and m < (c+2)**3):
            c = c+1
        elif ((c-1)**3 <= m and m < c**3):
            c = c-1
        else:
            assert False
    if m-c**3 >= c**3-1-(c-1)**3:
        X, ans = f(m-c**3)
        return(c**3 + X, 1 + ans)
    else:
        X, ans = f(c**3 - 1 - (c-1)**3)
        return((c-1)**3 + X, 1 + ans)

if __name__ == '__main__':
    m = int(input())

    X, ans = f(m)
    print(ans, X)
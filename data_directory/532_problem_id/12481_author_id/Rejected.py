MAX = 100005

def big_pow3(n):
    l = 0; p = MAX
    while p-l != 1:
        mid = (p+l+1)//2
        if (mid*mid*mid <= n):
            l = mid
        else:
            p = mid
    return l

def f(n):
    if n < 8:
        return [n, n]
    a = big_pow3(n)
    r1 = f(n-a**3)
    r1 = [r1[0] + 1, r1[1] + a**3]
    r2 = f(a**3-1)
    return max(r1, r2)
        

if __name__ == "__main__":
    m = int(input()) 
    print(*f(m))
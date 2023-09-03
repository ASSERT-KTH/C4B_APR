def main():
    a, b, x, y = map(int,input().split())
    lo, hi = 0, int(2*1e9)
    while lo!=hi:
        mid = (lo+hi+1)//2
        if mid*x<=a and mid*y<=b: lo = mid
        else: hi = mid-1
    print(lo*x,lo*y)

if __name__=="__main__":
    main()
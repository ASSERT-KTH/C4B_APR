def compute():
    n, a, b, p, q = map(int,input().split())
    return (n//a)*p + (n//b)*q - (n//(a*b))*min(p,q)

if __name__=="__main__":
    print(compute())
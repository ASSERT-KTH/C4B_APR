def compute():

    def gcd(a,b):
        return a if b==0 else gcd(b,a%b)

    def lcm(a,b):
        return a*(b//gcd(a,b))

    n, a, b, p, q = map(int,input().split())
    return (n//a)*p + (n//b)*q - (n//(lcm(a,b)))*min(p,q)

if __name__=="__main__":
    print(compute())
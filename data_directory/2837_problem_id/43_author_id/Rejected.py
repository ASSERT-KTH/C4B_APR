def fun(n):
    cnt = 0
    while n>0:
        now = n % 10
        ##print(n,now)
        n = n / 10
        if now>0:
            cnt+=1
        n = int(n)
    if cnt>1:
        return 0;
    else:
        return 1


if __name__ == "__main__":
    n = input()
    n = int(n)
    i = n+1
    while fun(i)!=1:
        i+=1
    print(i-n)
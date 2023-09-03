if __name__=="__main__":
    n,m=list(map(int,input().split()))
    if(n<=m):
        print(n)
        exit()
    l=0
    r=10**18


    while(r>l+1):
        k=(l+r)//2
        if(n-((k-1)*k)/2-(m+k)>0):
            l=k
        else:
            r=k
    print(m+k)
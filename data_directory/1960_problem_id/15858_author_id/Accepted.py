for i in range (0,5):
    s=input().split()
    a="".join(s)
    j=a.find("1")
    if(j>=0):
        n=abs(2-i)
        k=abs(2-j)
        print( n+k)
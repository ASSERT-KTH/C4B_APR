def main():
    mode="filee"
    if mode=="file":f=open("test.txt","r")
    get = lambda :[int(x) for x in (f.readline() if mode=="file" else input()).split()]
    [a,b,r]=get()
    r*=4
    x = a//r
    y = b//r
    ans = x * y
    if ans == 0 and (r//2) <=a and (r//2) <=b:ans=1
    #print(x,y,ans)
    print("First" if ans%2 == 1 else "Second")
    


    if mode=="file":f.close()


if __name__=="__main__":
    main()
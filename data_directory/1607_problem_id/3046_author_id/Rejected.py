def get_count(n):
    lenn = len(str(n))
    if lenn==1:
        return n
    if lenn==2:
        return 9 + n//10
    total=0
    for i in range(1,lenn):
        total+=(max(1,10**(i-2))*9)
    while str(n)[-1]!=str(n)[0]:
        n-=1
    total+=(int(str(n)[1:-1]))
    total+=((int(str(n)[0])-1)*10**(lenn-2))
    return total

def main():
    mode="filee"
    if mode=="file":f=open("test.txt","r")
    #f.readline()
    #input()
    get = lambda :[int(x) for x in (f.readline() if mode=="file" else input()).split()]
    [l,r] = get()
    print(get_count(r)-get_count(l)+1 - (1 if len(str(l))>2 and str(l)[0]!=str(l)[-1] else 0))

    if mode=="file":f.close()


if __name__=="__main__":
    main()
prime=[2,3,5,7,11,13]

def create_list(n):
    global prime
    for x in range(15,n+1,2):
        notPrime=False
        hold=int(x**0.5)+1
        for j in prime:
            if j>hold:
                break
            if x%j==0:
                notPrime=True
                break
        if notPrime==False:
            prime.append(x)
    #print(len(prime))

def main():
    mode="filee"
    if mode=="file":f=open("test.txt","r")
    #f.readline()
    #input()
    get = lambda :[int(x) for x in (f.readline() if mode=="file" else input()).split()]
    create_list(60)
    [x,y]=get()
    if y not in prime or prime[prime.index(x)+1]!=y:
        print("NO")
        return
    print("YES")

    if mode=="file":f.close()


if __name__=="__main__":
    main()
def dragon_injurd(k,l,m,n,d):
    dragon=[0]*d
    r=0
    injurd=[k,l,m,n]
    # return dragon
    for i in range(4):
        r=0
        while r<=d-1:
            if (r+1)%injurd[i]==0:
                dragon[r]=1
            r+=1
    # return injurd
    return sum(dragon)
    # return dragon
def main():
    k=int(input())
    l=int(input())
    m=int(input())
    n=int(input())
    d=int(input())
    print(dragon_injurd(k,l,m,n,d))



if __name__=='__main__':
    main()
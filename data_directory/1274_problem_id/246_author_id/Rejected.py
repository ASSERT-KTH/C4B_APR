def dragon_injurd(k,l,m,n,d):
    dragon=[0]*(d+1)
    r=0
    injurd=sorted([k,l,m,n])



    for i in range(4):
        if dragon[injurd[i]]!=11:
            dragon[injurd[i]]=11
            for j in range(injurd[i],d+1,injurd[i]):
                dragon[j]=11
    return dragon.count(11)






    # for i in range(4):
    #     r=0
    #     while r<=d-1:
    #         if (r+1)%injurd[i]==0:
    #             dragon[r]=1
    #         r+=1
    # # return injurd
    # return sum(dragon)
    # # return dragon
def main():
    k=int(input())
    l=int(input())
    m=int(input())
    n=int(input())
    d=int(input())
    print(dragon_injurd(k,l,m,n,d))



if __name__=='__main__':
    main()
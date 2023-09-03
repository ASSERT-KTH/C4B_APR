a,b=map(int,input().split())
cnt=1
while(1):
    if(cnt&1):
        a-=cnt
    else: 
        b-=cnt
    if(a<0):
        print("Vladik")
        quit()
    elif(b<0):
        print("Valera")
        quit()
    else:
        cnt+=1
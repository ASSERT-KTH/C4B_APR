a, b = map(int,input().split())
cnt = 1
while True :
    if cnt % 2 == 1 :
        a -= cnt
    else :
        b -= cnt
    if(b < 0) : 
        print("Valera")
        break
    if(a < 0) :
        print("Vladik")
        break
    cnt += 1
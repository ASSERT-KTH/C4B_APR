x = int(input())
a,b,c,d,e,f,g,h,i,j,k,l = map(int,input().split())
lst = [a,b,c,d,e,f,g,h,i,j,k,l]
lst.sort(reverse=True)
z = 0
if(x==0):
    print("0")
else:
    for i in range(len(lst)):
        z += lst[i]
        if(z >= x):
            a = i + 1
            break
        else:
            a = -1
    print(a)
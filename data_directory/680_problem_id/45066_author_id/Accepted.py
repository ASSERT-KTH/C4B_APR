x=int(input())
if x<3:
    print(-1)
else:
    b=int(x/2)
    if(x%2):
        print(2*b*(b+1),2*b*(b+1)+1)
    else:
        print(b*b-1,b*b+1)
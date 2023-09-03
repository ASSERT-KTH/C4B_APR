x=int(input())
y=int(input())
if x-y>1 :
    print(min(x,y),int((x-y)/2))
elif y-x>1:
    print(min(x,y),int((y-x)/2))
else:
    print(min(x,y),0)
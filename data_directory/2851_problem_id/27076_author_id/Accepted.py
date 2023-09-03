x=1
step=1
a,b=map(int,input().split())
while True:
    if step==1:
        if x>a: break
        a-=x
        x+=1
        step=0
    else:
        if x>b: break
        b-=x
        x+=1
        step=1
if step==1:
    print("Vladik")
else:
    print("Valera")
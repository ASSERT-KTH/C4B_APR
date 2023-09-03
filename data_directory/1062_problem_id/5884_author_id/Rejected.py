a=str(input(""))
s=int(a.count("7"))
f=int(a.count("4"))
summ=int(s)+int(f)
sum1=str(summ)
length=len(sum1)
count=0
for i in range(len(sum1)):
    if summ>0:
            
        if summ%10==7 or summ%10==4:
            summ=summ/10
            count=count+1;
        else:
            print("NO")
        
if count==length:
    print("YES")
else:
    print("NO")
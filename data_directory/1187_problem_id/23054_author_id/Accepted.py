x= input()
y= x.capitalize()
caps = x.upper()
first=x[0]
last=x[1:]
nocaps = x.lower()
if(x!=caps) and (x!=nocaps):
    if(x==y) or (first==first.lower() and last==last.upper()):
        print(y)
    else:
        print (x)
elif(len(x)==1 and x==nocaps):
    print (caps)
elif(len(x)==1 and x==caps):
    print (nocaps)
elif(x==caps):
    print (nocaps)
elif(x==nocaps):
    print (x)
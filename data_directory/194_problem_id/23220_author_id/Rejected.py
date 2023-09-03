def read(s=""):
    return [int(e) for e in input(s).split()]
x =read()
counter=0
while x>0:
    if x>4:
        x =x-5
    elif x>3:
        x = x-4
    elif x>2:
        x = x-3
    elif x>1:
        x=x-2
    elif x>0:
        x=x-1
    counter =counter +1
print (counter)
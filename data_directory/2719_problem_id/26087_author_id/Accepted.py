a,b=input().split()
a=int(a)
b=int(b)
def c(a,b) :
    counter =0
    while(True) :
        if(a>b):
            return counter
        a=a*3
        b=b*2
        counter = counter + 1
print(c(a,b))
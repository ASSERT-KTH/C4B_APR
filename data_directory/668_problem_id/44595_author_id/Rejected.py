def f(x):
    if x==1:
        return "I hate it"
    else:
        if x%2==0:
            return f(x-1)+" I love it"
        else:
            return f(x-1)+" I hate it"
a=int(input())
print (f(a))
def ch(a):
    for i in range(0,1):
        if a[i]=='H' or a[i]=='Q' or a[i]=='9' :
            return "YES"
    return "NO"

a=input()
print(ch(a))
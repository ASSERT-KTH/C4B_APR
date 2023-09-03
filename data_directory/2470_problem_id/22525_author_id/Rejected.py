l=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47 ,53]

m=int(input())
n=int(input())

if m not in l:
    print("NO")
elif n not in l:
    print("NO")
else:

    for i in range(len(l)):
        if l[i]==m:
            if l[i+1]==n:
                print("YES")
                break
            else:
                print( "NO")
                break
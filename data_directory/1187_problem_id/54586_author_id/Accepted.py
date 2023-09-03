a = input()
if a.upper() == a:
    print(a.lower())
else:
    for i in range(len(a)):
        if ord(a[i])>95 and ord(a[i])<122 and i!=0:
            print(a)
            break
    else:
        print(a[0].upper()+a[1:].lower())
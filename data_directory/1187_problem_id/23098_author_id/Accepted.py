n = input()
if n[1:] == n[1:].upper():
    if n[0] == n[0].upper():
        print(n.lower())
    else:    
        print(n[0].upper() + n[1:].lower())
else:
    print(n)
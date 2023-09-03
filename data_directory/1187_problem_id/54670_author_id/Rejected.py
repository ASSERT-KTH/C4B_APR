n = input()
n_1 = n[1:]
if n.isupper() == True:
    print(n.lower())
elif n_1.isupper() == True and n[:1].islower() == True:
    print(n.capitalize())
else:
    print(n)
a=input()
if ((a[0].islower()) and (a[1:].isupper())) or (a.islower()):
    print(a[0].upper()+a[1:].lower())
elif (a.isupper()):
    print(a.lower())
else:
    print(a)
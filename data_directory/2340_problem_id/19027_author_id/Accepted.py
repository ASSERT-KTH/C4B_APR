x = input()
capital,small,i = 0,0,0
while i<len(x):
    if x[i].isupper()== True:
        capital+=1
    else:
        small+=1
    i+=1

if small >=capital:
    print(x.lower())
else:
    print(x.upper())
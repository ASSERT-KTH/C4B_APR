x = input()
capital,small = 0,0
if x[0].isupper()== True:
    capital+=1
else:
    small+=1

if small >capital:
    print(x.lower())
else:
    print(x.upper())
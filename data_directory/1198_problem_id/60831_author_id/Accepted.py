p = str(input())

a = False

for i in range (len(p)):
    if p[i] == 'H' or p[i] == 'Q' or p[i] == '9':
        a = True
        break

if a == True:
    print ("YES")
else:
    print ("NO")
n = "aiouey"
ss = input()
s = ss.lower()
for c in s :
    if not c in n :
        print('.'+c,end = ' ')
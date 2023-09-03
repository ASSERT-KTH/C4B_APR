s = input()
b = False
if s[0] == "-":
    s = s[1:]
    b = True
if "." in s:
    i,j = s.split(".")
    if len(j) > 2:
        j1 = j[:2]
    elif len(j) == 2:
        j1 = j
    elif len(j) == 1:
        j1 = j+"0"
    elif len(j) == 0:
        j1 = "00"
else:
    i = s
    j1 = "00"
li = []
for k in range(len(i)):
    li.append(s[k])
n = len(i) // 3
m = -3; p = 0
for i in range(n):
    li.insert(m-p,',')
    m = m-3
    p +=1
l1 =(''.join(map(str, li)))
if b:
    print("("+"$"+l1+"."+j1+")")
else:
    print("$"+l1+"."+j1)
word = []
word = list(input())
toggle = False

if "Q"  in word:
    toggle = True
if "9"  in word:
    toggle = True
if "H"  in word:
    toggle = True
if "+" in word:
    toggle = True
if toggle == True:
    print("YES")
else:
    print("NO")
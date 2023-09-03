entered = input()
list(entered)
h = entered.count("H")
q = entered.count("Q")
nine = entered.count("9")
plus = entered.count("+")
if(h>0 or q>0 or nine>0 or plus>0):
  print("YES")
else:
  print("NO")
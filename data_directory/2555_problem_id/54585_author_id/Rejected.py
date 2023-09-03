import re
string=input()
pattern1=r"1?000000001?"
pattern2=r"0?111111110?"
if re.search(pattern1,string):
 print("YES")
elif re.search(pattern2,string):
 print("YES")
else:
 print("NO")
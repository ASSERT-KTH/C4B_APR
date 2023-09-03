import re
string=input()
pattern1=r"1?00000000*1?"
pattern2=r"0?11111111*0?"
if re.search(pattern1,string):
 print("YES")
elif re.search(pattern2,string):
 print("YES")
else:
 print("NO")
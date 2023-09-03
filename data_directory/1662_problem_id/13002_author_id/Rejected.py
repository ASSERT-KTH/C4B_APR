import re
if re.compile('(\w){1,16}@((\w{1,16}\.)*)\w{1,16}(/){1}\w*$').match(input()) != None:
    print("YES")
else:
    print("NO")